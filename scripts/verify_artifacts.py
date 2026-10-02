"""Audit output tersimpan, cakupan PDF, checksum data, dan versi dependency."""
from pathlib import Path
from datetime import datetime, timezone
from importlib.metadata import version
import hashlib
import json
import re

import nbformat
from IPython.core.inputtransformer2 import TransformerManager

ROOT = Path(__file__).resolve().parents[1]


def main():
    coverage = json.loads((ROOT / "reports/coverage.json").read_text())
    executions = json.loads((ROOT / "reports/execution.json").read_text())
    manifest = json.loads((ROOT / "data/manifest.json").read_text())
    assert len(coverage) == 119
    assert len({(e["chapter"], e["title"]) for e in coverage}) == 119
    audit = {"checked_utc": datetime.now(timezone.utc).isoformat(), "notebooks": {}}
    for chapter in range(1, 5):
        name = f"Chapter_{chapter:02d}.ipynb"
        path = ROOT / name
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        code_cells = [c for c in notebook.cells if c.cell_type == "code"]
        assert [c.execution_count for c in code_cells] == list(range(1, len(code_cells) + 1)), name
        assert executions[name]["status"] == "passed", name
        assert executions[name]["code_cells"] == len(code_cells)
        outputs = [o for c in code_cells for o in c.outputs]
        assert not any(o.output_type == "error" for o in outputs), name
        for cell in code_cells:
            compile(TransformerManager().transform_cell(cell.source), name, "exec")
        markdown = "\n".join(c.source for c in notebook.cells if c.cell_type == "markdown")
        assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", markdown), name
        rows = [e for e in coverage if e["chapter"] == chapter]
        for entry in rows:
            assert f'id="{entry["anchor"]}"' in markdown, entry
            assert f'## {entry["title"]}' in markdown, entry
            assert entry["pdf_page"] == entry["page"] + 18, entry
            assert entry["status"] in ["Teori selesai", "Kode lulus"], entry
        audit["notebooks"][name] = {
            "code_cells": len(code_cells),
            "mapped_sections": len(rows),
            "figures": sum("image/png" in o.get("data", {}) for o in outputs),
            "errors": 0,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    for filename, expected in manifest["files"].items():
        actual = hashlib.sha256((ROOT / "data" / filename).read_bytes()).hexdigest()
        assert actual == expected["sha256"], filename
    audit["datasets_verified"] = len(manifest["files"])
    dependencies = {}
    for line in (ROOT / "requirements.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        package, pinned = line.split("==")
        assert version(package) == pinned, package
        dependencies[package] = pinned
    audit["dependencies"] = dependencies
    audit["status"] = "passed"
    (ROOT / "reports/validation.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
