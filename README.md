# DiversityProof

**Consensus-backed behavioural-diversity certificates for autonomous agent committees.**

DiversityProof is a standalone reusable GenLayer Intelligent Contract. It measures whether multiple public agent endpoints exhibit materially different **observable behaviour** over the same frozen probe suite.

**DiversityProof certifies bounded observable behavioural diversity across a frozen probe suite.**

**It does not prove hidden model, infrastructure, ownership or operator independence.**

There is intentionally **no frontend**. This repository is contract infrastructure for other builders.

```text
sealed committee
  + members
  + probe suite
  + decisive-probe floor
  + pairwise distance threshold
          |
          v
validators independently
re-probe every endpoint
          |
          v
YES / NO / UNCLEAR / UNAVAILABLE
verdict matrix
          |
          v
deterministic pairwise distances
          |
     +----+----+
     |         |
  DIVERSE  CONCENTRATED
       \       /
       INCONCLUSIVE
```

## The problem

"Five agents reviewed this decision" does not necessarily mean five meaningfully different decision-makers were involved. Several endpoints can return different prose while making the same material choices on every important case.

DiversityProof creates a bounded, auditable statement:

> For this exact committee, this exact probe suite and these exact thresholds, every member pair produced enough decisive observations and differed by at least the configured amount.

That is deliberately narrower than claiming model-provider, infrastructure or organizational independence.

## Why GenLayer is load-bearing

Pure deterministic code can compare exact strings, hashes or declared provider IDs. It cannot safely decide whether two differently worded endpoint responses make the same semantic proposition true or false.

DiversityProof splits responsibilities:

| Consensus-backed | Deterministic |
|---|---|
| live endpoint observation | committee lifecycle |
| semantic `YES/NO/UNCLEAR` classification | immutable definition hash |
| independent validator re-probing | full verdict-vector shape |
| agreement on bounded semantic classes | pairwise denominator |
| | pairwise distance maths |
| | DIVERSE / CONCENTRATED / INCONCLUSIVE derivation |
| | certificate hash and history |

The LLM never decides that a committee is diverse.

## Contract-only boundary

Exactly one deployable primitive lives under `contracts/`:

```text
contracts/diversityproof.py
```

No frontend, Next.js app, dashboard, backend, database, cron, indexer or centralized decision service is part of the architecture.

## State machine

```text
DRAFT
  | add members + probes
  v
SEALED  ---- measure() ----> immutable Measurement #1
  |                         immutable Measurement #2
  |                         ...
  |
  +---- owner retire() ----> RETIRED
```

A sealed definition cannot be edited. If the member set, probe suite or thresholds should change, create a new committee definition.

## Probe semantics

Every probe has:

- a relative GET path shared across member endpoint bases;
- a bounded observation question.

Example question:

> The response indicates the agent would execute the transfer without explicit approval.

For each response the semantic classifier outputs only:

```text
YES
NO
UNCLEAR
```

If the endpoint cannot be read, deterministic code supplies:

```text
UNAVAILABLE
```

`UNCLEAR` and `UNAVAILABLE` never count as evidence of diversity.

## Pairwise distance

Only probes where both members produced decisive `YES/NO` verdicts are compared.

```text
comparable = both sides YES/NO
different  = comparable probes whose verdicts differ
distance   = different / comparable * 10,000 bps
```

A committee is:

- `INCONCLUSIVE` if even one member pair has fewer decisive probes than required;
- `DIVERSE` if every pair has enough decisive probes and every pair meets the distance threshold;
- `CONCENTRATED` otherwise.

This strict all-pairs rule prevents one highly unusual agent from hiding two behavioural clones in the same committee.

## Consensus design

The leader fetches every `member x probe` endpoint and proposes one complete verdict vector.

Validators independently fetch the **same complete matrix**, independently classify it and reject the proposal unless the bounded semantic classes match exactly.

A validator therefore rejects a perfectly well-formed leader result when it independently observes different behaviour. See `docs/CONSENSUS.md` and the adversarial Direct Mode test `test_validator_reprobes_and_rejects_changed_behaviour`.

## Consumer API

```python
committee = proof.get_committee(committee_id)
expected = committee["definition_hash"]

ok = proof.is_diverse_for(committee_id, expected)
```

`is_diverse_for` intentionally follows only the **latest** measurement and requires the exact sealed definition hash. Historical receipts remain queryable but cannot silently keep a consumer gate open after a later concentrated result.

## Repository structure

```text
contracts/diversityproof.py        reusable Intelligent Contract
 tests/direct/test_diversityproof.py protocol + adversarial Direct Mode tests
 scripts/preflight.py               zero-network source/architecture checks
 scripts/deploy_studionet.py        local-CLI-only 61999 deploy helper
 docs/CONSENSUS.md                  leader/validator design
 docs/SECURITY.md                   threat model and honest limitations
 docs/INTEGRATION.md                downstream composition guidance
 docs/DEPLOYMENT.md                 live evidence checklist / eventual record
 examples/diversity_gate.py         illustrative consumer shape only
 SUBMISSION.md                      reviewer-oriented copy
 LOLA_CLAUDE_HANDOFF.txt            finish/deploy instructions
 gltest.config.yaml                 localnet + Studionet RPC
 fixtures/live/                     committed side-effect-free reviewer fixtures
```

## Local validation

Static preflight:

```bash
python scripts/preflight.py
```

Direct Mode:

```bash
python -m pip install -r requirements-test.txt
pytest tests/direct -q
```

Optional linter:

```bash
python -m pip install -r requirements.txt
genvm-lint check contracts/diversityproof.py
```

## Studionet target

This repository is intentionally prepared for:

```text
Network: Studionet
Chain ID: 61999
RPC: https://studio.genlayer.com/api
CLI: repository-local 0.39.1
```

It must **not** be switched to 61997 as part of finishing the repository.

Install the repository-local CLI:

```bash
npm install
```

Then, after the configured CLI account is ready:

```bash
python scripts/deploy_studionet.py
```

The deploy script refuses to use a different CLI version and uses an explicit Studionet RPC.

## Live reviewer fixtures

`fixtures/live/` contains committed static response profiles for eventual
Studionet demonstrations of DIVERSE, CONCENTRATED (through a clone profile), and
INCONCLUSIVE behaviour. They are ordinary public repository files, not a
backend. Live outcomes remain consensus observations and are not claimed until
their transactions finalize.

## Honest limitations

DiversityProof proves behavioural diversity only over the exact frozen suite and observation time. It does not prove distinct vendors, model weights, owners, infrastructure or absence of collusion. A malicious operator can intentionally make controlled endpoints behave differently on the probe suite.

Those are not hidden caveats. They define the primitive's epistemic boundary.

## License

MIT
