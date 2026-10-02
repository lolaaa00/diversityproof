#!/usr/bin/env python3
"""Deploy DiversityProof to GenLayer Studionet (chain 61999) with local CLI 0.39.1.

This script intentionally refuses to fall back to a global GenLayer CLI.
Install the repository-local CLI first with `npm install`, then run this script.
It never asks for or stores a private key; the CLI account must already be configured.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "diversityproof.py"
PREFLIGHT = ROOT / "scripts" / "preflight.py"
STUDIONET_RPC = "https://studio.genlayer.com/api"
REQUIRED_CLI = "0.39.1"


def run(command: list[str], *, capture: bool = False) -> str:
    print("+", " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=capture,
    )
    if capture:
        output = (completed.stdout or "") + (completed.stderr or "")
        print(output.strip())
    else:
        output = ""
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)
    return output


def main() -> int:
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if npx is None:
        print("ERROR: Node/npm/npx is required.", file=sys.stderr)
        return 2
    if not (ROOT / "node_modules").exists():
        print("ERROR: repository-local CLI is not installed. Run: npm install", file=sys.stderr)
        return 2
    if not CONTRACT.is_file():
        print(f"ERROR: contract not found: {CONTRACT}", file=sys.stderr)
        return 2

    run([sys.executable, str(PREFLIGHT)])

    version_output = run([npx, "--no-install", "genlayer", "--version"], capture=True)
    match = re.search(r"(\d+\.\d+\.\d+(?:[A-Za-z0-9.-]*)?)", version_output)
    actual = match.group(1) if match else ""
    if actual != REQUIRED_CLI:
        print(
            f"ERROR: refusing deployment with CLI {actual or 'unknown'}; required {REQUIRED_CLI} for this 61999 handoff.",
            file=sys.stderr,
        )
        return 2

    run([npx, "--no-install", "genlayer", "account", "show"])
    run(
        [
            npx,
            "--no-install",
            "genlayer",
            "deploy",
            "--contract",
            str(CONTRACT),
            "--rpc",
            STUDIONET_RPC,
        ]
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
