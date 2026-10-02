#!/usr/bin/env python3
"""Zero-network structural preflight for DiversityProof."""
from __future__ import annotations

import ast
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "diversityproof.py"
README = ROOT / "README.md"

checks: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    checks.append((name, bool(condition)))


def main() -> int:
    source = CONTRACT.read_text(encoding="utf-8")
    tree = ast.parse(source)

    check("contract exists", CONTRACT.is_file())
    check("README exists", README.is_file())
    check("GenLayer dependency header", '"Depends": "py-genlayer:' in source)
    check("contract class", "class DiversityProof(gl.Contract):" in source)
    check("custom nondeterministic consensus", "gl.vm.run_nondet_unsafe" in source)
    check(
        "validators re-observe",
        source.count("gl.nondet.web.render") >= 2
        and source.count("gl.nondet.exec_prompt") >= 2
        and "own == proposed" in source,
    )
    check("live web observation", "gl.nondet.web.render" in source)
    check("LLM semantic classification", "gl.nondet.exec_prompt" in source)
    check("definition hash", "definition_hash" in source and "Keccak256" in source)
    check("certificate hash", "certificate_hash" in source)
    check("bounded members", "MAX_MEMBERS = 5" in source)
    check("bounded probes", "MAX_PROBES = 8" in source)
    check("no transfer logic", "gl.message.value" not in source and "transfer(" not in source.lower())
    check("no HTTP endpoints", "http://" not in source)
    check("Studionet RPC documented", "https://studio.genlayer.com/api" in (ROOT / "gltest.config.yaml").read_text(encoding="utf-8"))
    check("no frontend directory", not (ROOT / "frontend").exists())
    check("no Next.js", not (ROOT / "next.config.js").exists() and not (ROOT / "app").exists())
    check("no backend directory", not (ROOT / "backend").exists())
    check("AST has public writes", source.count("@gl.public.write") >= 6)
    check("AST has public views", source.count("@gl.public.view") >= 6)

    banned_imports = {"requests", "httpx", "openai", "anthropic", "web3", "flask", "fastapi", "django"}
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    check("no centralized/network client imports", imported.isdisjoint(banned_imports))

    failures = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + " - " + name)
    print(f"\n{len(checks) - len(failures)}/{len(checks)} preflight checks passed")
    if failures:
        print("Failures:", ", ".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
