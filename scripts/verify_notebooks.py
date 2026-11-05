"""Execute each notebook in an isolated Python process and verify its assertions.

Usage: python scripts/verify_notebooks.py [--write] [notebook ...]
No Jupyter server or local kernelspec installation is required.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def execute(path, write):
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager

    # Use this interpreter, even when a different system python3 kernelspec exists.
    class CurrentPythonKernel(KernelManager):
        def format_kernel_cmd(self, extra_arguments=None):
            return [sys.executable, "-m", "ipykernel_launcher", "-f", self.connection_file]

    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    with tempfile.TemporaryDirectory(prefix="scientific-computing-") as tmp:
        os.environ["MPLCONFIGDIR"] = str(Path(tmp) / "matplotlib")
        os.environ["IPYTHONDIR"] = str(Path(tmp) / "ipython")
        os.environ["JUPYTER_RUNTIME_DIR"] = str(Path(tmp) / "jupyter")
        os.environ["MPLBACKEND"] = "module://matplotlib_inline.backend_inline"
        client = NotebookClient(
            nb, timeout=180, kernel_manager_class=CurrentPythonKernel,
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.execute()
    if write:
        nbformat.write(nb, path)
    streams = [o.get("text", "") for c in nb.cells if c.cell_type == "code"
               for o in c.get("outputs", []) if o.output_type == "stream"]
    print(json.dumps({"notebook": str(path.relative_to(ROOT)), "status": "PASS",
                      "code_cells": sum(c.cell_type == "code" for c in nb.cells),
                      "results": streams}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Save fresh notebook outputs")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("notebooks", nargs="*")
    args = parser.parse_args()
    if args.worker:
        execute(Path(args.notebooks[0]).resolve(), args.write)
        return
    paths = [Path(p).resolve() for p in args.notebooks] if args.notebooks else sorted(ROOT.glob("[0-9]*_*/*.ipynb"))
    if not paths:
        parser.error("No notebooks found")
    failures = []
    for path in paths:
        command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
        if args.write:
            command.append("--write")
        result = subprocess.run(command + [str(path)], cwd=ROOT, check=False)
        if result.returncode:
            failures.append(str(path))
    if failures:
        print("FAILED: " + ", ".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print(f"All {len(paths)} notebooks passed.")


if __name__ == "__main__":
    main()
