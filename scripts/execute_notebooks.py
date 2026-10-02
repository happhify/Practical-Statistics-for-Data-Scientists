"""Jalankan notebook berurutan, tiap notebook memakai kernel baru interpreter aktif."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import json
import os
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))
os.environ.setdefault("IPYTHONDIR", str(ROOT / ".cache/ipython"))
os.environ.setdefault("JUPYTER_RUNTIME_DIR", str(ROOT / ".cache/jupyter/runtime"))
for variable in ["MPLCONFIGDIR", "IPYTHONDIR", "JUPYTER_RUNTIME_DIR"]:
    Path(os.environ[variable]).mkdir(parents=True, exist_ok=True)
import nbformat
from nbclient import NotebookClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapters", nargs="*", type=int, choices=[1, 2, 3, 4])
    args = parser.parse_args()
    report_path = ROOT / "reports/execution.json"
    reports = json.loads(report_path.read_text()) if report_path.exists() else {}
    with tempfile.TemporaryDirectory(prefix="psds-kernel-") as directory:
        kernel = Path(directory) / "kernels/psds-test"
        kernel.mkdir(parents=True)
        (kernel / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "PSDS (.venv)", "language": "python"
        }))
        os.environ["JUPYTER_PATH"] = directory + os.pathsep + os.environ.get("JUPYTER_PATH", "")
        for chapter in args.chapters or [1, 2, 3, 4]:
            path = ROOT / f"Chapter_{chapter:02d}.ipynb"
            notebook = nbformat.read(path, as_version=4)
            # Hapus hasil lama supaya kegagalan parsial tidak menyisakan output basi.
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    cell.outputs = []
                    cell.execution_count = None
            started = time.monotonic()
            record = {"started_utc": datetime.now(timezone.utc).isoformat(),
                      "python": sys.version.split()[0], "interpreter": sys.executable}
            print(f"START {path.name}", flush=True)
            try:
                NotebookClient(notebook, timeout=600, kernel_name="psds-test",
                               resources={"metadata": {"path": str(ROOT)}},
                               allow_errors=False).execute()
                nbformat.validate(notebook)
                record["status"] = "passed"
            except Exception as error:
                record.update(status="failed", error=str(error))
                raise
            finally:
                record["seconds"] = round(time.monotonic() - started, 2)
                record["code_cells"] = sum(c.cell_type == "code" for c in notebook.cells)
                record["executed_cells"] = sum(c.cell_type == "code" and c.execution_count is not None
                                               for c in notebook.cells)
                record["figures"] = sum("image/png" in o.get("data", {})
                                        for c in notebook.cells for o in c.get("outputs", []))
                record["errors"] = sum(o.output_type == "error"
                                       for c in notebook.cells for o in c.get("outputs", []))
                nbformat.write(notebook, path)
                reports[path.name] = record
                report_path.parent.mkdir(exist_ok=True)
                report_path.write_text(json.dumps(reports, indent=2) + "\n")
            print(f"PASS {path.name}: {record['executed_cells']} cells, "
                  f"{record['figures']} figures, {record['seconds']} seconds", flush=True)


if __name__ == "__main__":
    main()
