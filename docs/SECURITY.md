# Security and limitations

## What DiversityProof proves

A `DIVERSE` measurement means that, for the exact sealed committee and exact sealed probe suite, every member pair had enough independently re-observed decisive probes and met the configured behavioural-distance threshold.

It does **not** prove:

- different model vendors;
- different weights, prompts or infrastructure;
- organizational independence;
- correctness, safety, intelligence or quality;
- future behaviour after the measurement;
- absence of collusion.

The primitive proves bounded observable behavioural diversity, nothing more.

## Threats addressed

### Leader forgery

Validators re-fetch and re-classify every member/probe response. A leader cannot obtain a certificate by supplying a well-formed but false verdict vector.

### Selective omission

The verdict vector length is fixed by `member_count * probe_count`; validators reconstruct the entire vector.

### Prompt injection in endpoint responses

Endpoint text is JSON-framed as untrusted data. The classifier prompt explicitly forbids following instructions contained in responses. Probe questions are also bounded and screened against obvious control-language markers.

### Fake diversity through uncertainty

`UNCLEAR` and `UNAVAILABLE` are excluded from the distance denominator and cannot count as differences. Too few decisive probes produces `INCONCLUSIVE`.

### Definition substitution

Consumers pin the sealed `definition_hash`. A measurement from a different committee/probe definition cannot satisfy `is_diverse_for`.

### Stale historical success

The contract exposes full immutable measurement history and only uses `latest_measurement_id` for `is_diverse_for`. A later concentrated result supersedes an earlier diverse result for the consumer gate without rewriting history.

## Known limitations

- Public endpoints can change between validator observations; in that case consensus may fail, which is safer than certifying unstable behaviour.
- The probe suite determines what dimensions are measured. A weak or redundant suite produces a weak certificate.
- An operator controlling several endpoints can intentionally program different behaviours on the probe suite. DiversityProof certifies observable diversity, not hidden ownership independence.
- GET audit endpoints must be side-effect-free by design. The contract intentionally does not issue arbitrary POST requests.
- URL-shape checks are defence in depth; validator-network egress policy remains a protocol/runtime responsibility.
