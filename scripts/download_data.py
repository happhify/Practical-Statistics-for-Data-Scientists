"""Unduh dataset edisi kedua pada commit tetap; validasi SHA-256."""
from pathlib import Path
import argparse
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validasi lokal tanpa jaringan")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "data/manifest.json").read_text())
    base = ("https://raw.githubusercontent.com/gedeck/"
            f"practical-statistics-for-data-scientists/{manifest['commit']}/data/")
    for name, info in manifest["files"].items():
        path = ROOT / "data" / name
        if path.exists():
            if hashlib.sha256(path.read_bytes()).hexdigest() != info["sha256"]:
                raise RuntimeError(f"Checksum berbeda: {path}. File lokal tidak ditimpa.")
            print(f"OK {name}")
            continue
        if args.check:
            raise FileNotFoundError(f"{path}; jalankan scripts/download_data.py")
        request = urllib.request.Request(base + name, headers={"User-Agent": "PSDS-course-reproduction"})
        with urllib.request.urlopen(request, timeout=120) as response:
            content = response.read()
        if hashlib.sha256(content).hexdigest() != info["sha256"]:
            raise RuntimeError(f"Checksum unduhan tidak sesuai: {name}")
        temporary = path.with_suffix(path.suffix + ".part")
        temporary.write_bytes(content)
        temporary.replace(path)
        print(f"DOWNLOADED {name}: {len(content):,} bytes")


if __name__ == "__main__":
    main()
