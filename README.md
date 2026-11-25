# Course Adviser Expert System (C++17)

A rule-based forward-chaining expert system implemented in **C++17** that recommends an **AI Mini Project** or **Web Mini Project** based on a student's completed topics, interests, and available project time, while printing an explanation trace of every triggered rule.

---

## Aim & Objectives

- **Aim:** Design and implement a working rule-based adviser that recommends an AI or web mini project based on a student's completed topics, interests, and available project time, and explains triggered rules.
- **Objectives:**
  - Separate input facts (working memory) from recommendation rules (knowledge base).
  - Derive intermediate readiness facts (`ai_ready`, `web_ready`) via multistep forward chaining.
  - Explain each triggered rule in execution order.
  - Validate user input strictly (`0` or `1`) and test positive, partial, missing-time, and invalid cases.

---

## Architecture & Knowledge Base

1. **Command-Line Interface & Input Validation:** Reads six binary answers (`0` or `1`) in order: `cpp`, `dsa`, `db`, `ai_interest`, `web_interest`, `time`. Any missing or non-binary token exits immediately with status `1`.
2. **Working Memory (`std::set<std::string>`):** Stores initial positive facts and newly inferred intermediate/final facts per run.
3. **Knowledge Base (`std::vector<Rule>`):** Stores rules as `{needs, adds, reason}`. Recommendation rules are placed ahead of readiness rules to explicitly demonstrate multistep forward chaining:

| Rule | Premises (`needs`) | Conclusion (`adds`) | Explanation |
| --- | --- | --- | --- |
| R1 | `ai_ready`, `time` | `AI Mini Project` | AI foundations are ready and project time is available. |
| R2 | `web_ready`, `time` | `Web Mini Project` | Web foundations are ready and project time is available. |
| R3 | `cpp`, `dsa`, `ai_interest` | `ai_ready` | C++ and DSA are complete; AI interest is present. |
| R4 | `cpp`, `db`, `web_interest` | `web_ready` | C++ and databases are complete; web interest is present. |

4. **Forward-Chaining Inference Engine:** Loops over all rules until a pass adds no new facts (fixed-point closure), printing each rule's `reason` when fired.

---

## Build & Run

### Compile with GCC (`g++`)

```bash
g++ -std=c++17 -Wall -Wextra exp12.cpp -o exp12
```

### Run Interactive or Piped Input

```bash
printf '1 1 1 1 1 1\n' | ./exp12
```

Sample output:

```text
Samarth Mishra | EN24CS3010910
Course Adviser Expert System
Enter 0/1 for: C++ done, DSA done, databases done,
AI interest, web interest, project time: 
Rule: C++ and DSA are complete; AI interest is present.
Rule: C++ and databases are complete; web interest is present.
Rule: AI foundations are ready and project time is available.
Rule: Web foundations are ready and project time is available.
Recommendation: AI Mini Project
Recommendation: Web Mini Project
```

### Run Verification Suite

```bash
python tests/verify.py
```

---

## Verification Matrix

| Input Profile | Expected Outcome | Verified Result |
| --- | --- | --- |
| `1 1 1 1 1 1` | Both project options | AI and Web recommended |
| `1 0 0 1 1 1` | Prerequisites missing | No project match |
| `1 1 1 1 1 0` | Time missing | Readiness only; no match |
| `1 1 2 1 1 1` | Reject invalid input | Error; exit status `1` |

---

## Author

- **Samarth Mishra** (`EN24CS3010910`)  
  Expert Systems Lab (`CS3EA16`)
