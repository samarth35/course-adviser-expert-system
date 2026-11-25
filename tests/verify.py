"""Verification test suite for Course Adviser Expert System (exp12.cpp)."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXE_NAME = "exp12.exe" if os.name == "nt" else "exp12"
BINARY = ROOT / EXE_NAME


def run_case(stdin_text: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(BINARY)],
        input=stdin_text,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    if not BINARY.exists():
        print(f"Missing binary: {BINARY}. Compile exp12.cpp first.", file=sys.stderr)
        return 1

    cases = [
        {
            "name": "All six yes -> AI and Web Mini Project",
            "input": "1 1 1 1 1 1\n",
            "code": 0,
            "stdout_contains": [
                "Samarth Mishra | EN24CS3010910",
                "Rule: C++ and DSA are complete; AI interest is present.",
                "Rule: C++ and databases are complete; web interest is present.",
                "Rule: AI foundations are ready and project time is available.",
                "Rule: Web foundations are ready and project time is available.",
                "Recommendation: AI Mini Project",
                "Recommendation: Web Mini Project",
            ],
            "stderr_contains": [],
        },
        {
            "name": "Prerequisites missing -> No project match",
            "input": "1 0 0 1 1 1\n",
            "code": 0,
            "stdout_contains": ["No project match. Review prerequisites or project time."],
            "stderr_contains": [],
        },
        {
            "name": "Time missing -> Readiness rules only, no project match",
            "input": "1 1 1 1 1 0\n",
            "code": 0,
            "stdout_contains": [
                "Rule: C++ and DSA are complete; AI interest is present.",
                "Rule: C++ and databases are complete; web interest is present.",
                "No project match. Review prerequisites or project time.",
            ],
            "stderr_contains": [],
        },
        {
            "name": "Invalid token -> Error and exit status 1",
            "input": "1 1 2 1 1 1\n",
            "code": 1,
            "stdout_contains": [],
            "stderr_contains": ["Invalid input: each answer must be 0 or 1."],
        },
        {
            "name": "AI track only -> AI Mini Project",
            "input": "1 1 0 1 0 1\n",
            "code": 0,
            "stdout_contains": [
                "Rule: C++ and DSA are complete; AI interest is present.",
                "Rule: AI foundations are ready and project time is available.",
                "Recommendation: AI Mini Project",
            ],
            "stderr_contains": [],
        },
        {
            "name": "Web track only -> Web Mini Project",
            "input": "1 0 1 0 1 1\n",
            "code": 0,
            "stdout_contains": [
                "Rule: C++ and databases are complete; web interest is present.",
                "Rule: Web foundations are ready and project time is available.",
                "Recommendation: Web Mini Project",
            ],
            "stderr_contains": [],
        },
    ]

    for case in cases:
        res = run_case(case["input"])
        assert res.returncode == case["code"], (
            f"{case['name']}: expected exit {case['code']}, got {res.returncode}\n"
            f"stdout={res.stdout}\nstderr={res.stderr}"
        )
        for expected in case["stdout_contains"]:
            assert expected in res.stdout, f"{case['name']}: missing '{expected}' in stdout:\n{res.stdout}"
        for expected in case["stderr_contains"]:
            assert expected in res.stderr, f"{case['name']}: missing '{expected}' in stderr:\n{res.stderr}"
        print(f"PASS: {case['name']}")

    print(f"\nAll {len(cases)} verification cases passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
