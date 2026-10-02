# DiversityProof submission notes

## One-line description

DiversityProof certifies that an agent committee is observably behaviourally diverse over a frozen probe suite, using independent GenLayer re-probing plus deterministic all-pairs distance rules.

## Why it is a standalone Intelligent Contract

DiversityProof is deliberately contract-only. It has no frontend or product flow. Other contracts can pin a committee definition hash and consume `is_diverse_for(...)` as a reusable precondition.

## The primitive

A multi-agent committee can look independent while its members make materially identical decisions. String comparison cannot detect semantic equivalence, and trusting one off-chain classifier recreates a centralized oracle.

DiversityProof freezes:

- member endpoint bases;
- a shared probe suite;
- one observation proposition per probe;
- a minimum decisive-probe floor;
- a minimum pairwise behavioural distance.

GenLayer validators independently re-fetch every endpoint and classify every observed response into the same four bounded states: `YES`, `NO`, `UNCLEAR`, `UNAVAILABLE`.

Deterministic contract code then computes all pairwise distances. `UNCLEAR` and `UNAVAILABLE` never create fake diversity. A single under-observed pair makes the certificate `INCONCLUSIVE`; a single pair below threshold makes it `CONCENTRATED`.

## Delete GenLayer: what breaks?

- Exact string comparison mistakes paraphrases for diversity.
- Caller-declared model/provider IDs are assertions, not observed behaviour.
- One centralized LLM classifier can forge the behavioural matrix.
- Deterministic code cannot decide whether two differently worded responses make the same natural-language proposition true or false.

GenLayer is load-bearing because independent validators re-observe the same public behaviour and agree on bounded semantic classes before any diversity state can be recorded.

## What the model does not decide

The model never decides:

- committee status;
- pairwise distance;
- minimum evidence sufficiency;
- thresholds;
- certificate hashes;
- whether another contract may consume a different definition.

All of those are deterministic.

## Adversarial property reviewers should inspect

`test_validator_reprobes_and_rejects_changed_behaviour` proves the validator is substantive rather than format-only: the leader first proposes a well-formed diverse vector; the validator independently re-probes and observes clone behaviour, then rejects the leader result.

## Honest claim boundary

`DIVERSE` means bounded **observable behavioural diversity over the sealed probe suite**. It does not prove distinct model vendors, different weights, separate ownership or absence of collusion.

## Network target

This handoff is for **Studionet 61999 only** using the repository-local GenLayer CLI `0.39.1`. It must not be silently migrated to 61997.

## Verified live deployment

DiversityProof is finalized on Studionet at
`0x46BFFeA797588783ae5FA850206930fB443A8Ebc`. Finalized reviewer lifecycles prove
DIVERSE, clone-pair CONCENTRATED, and insufficient-evidence INCONCLUSIVE results.
The exact transactions, definition hashes, certificate hashes, pairwise data,
source-parity proof, and consumer hash-gate results are in `docs/DEPLOYMENT.md`.
