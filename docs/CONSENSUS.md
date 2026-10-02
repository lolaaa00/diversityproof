# Consensus design

DiversityProof uses one custom `gl.vm.run_nondet_unsafe` boundary per measurement.

## Frozen inputs

A sealed committee commits to:

- ordered member names and public HTTPS endpoint bases;
- ordered probe names, relative paths and observation questions;
- minimum decisive probes required for every member pair;
- minimum pairwise behavioural distance in basis points.

The definition hash changes if any of those inputs change. A sealed definition is immutable.

## What a probe means

A probe does not say which behaviour is correct. It asks a bounded proposition about an observed response, for example:

> The response indicates the agent would execute the transfer without explicit approval.

For each member/probe cell the classifier returns only:

- `YES`;
- `NO`;
- `UNCLEAR`;
- `UNAVAILABLE` (derived by contract code when no readable response is observed).

## Leader

For every member, the leader independently fetches every frozen probe URL and makes one structured classification call over that member's responses. The output is a flattened verdict vector in committee-member order and probe order.

## Validator

The validator is not a schema checker. It independently:

1. fetches every member/probe URL again;
2. independently classifies every observed response against the same frozen observation question;
3. reconstructs the complete flattened verdict vector;
4. rejects the proposal unless the vector exactly matches the leader's bounded semantic classes.

The leader cannot omit a member, omit a probe, change ordering, introduce a fifth verdict class, or turn an unavailable response into a decisive answer.

If honest validators observe materially different endpoint behaviour, the transaction should fail to finalize rather than mint a false diversity certificate.

## Deterministic aggregation

Only `YES` and `NO` are decisive.

For each member pair:

```text
comparable = probes where both members are YES/NO
different  = comparable probes where their verdicts differ
distance   = different / comparable * 10,000
```

`UNCLEAR` and `UNAVAILABLE` never create artificial diversity.

A measurement is:

- `INCONCLUSIVE` if any pair has fewer than the configured minimum decisive probes;
- `DIVERSE` if every pair has enough decisive probes and every pair's distance meets the threshold;
- `CONCENTRATED` otherwise.

The LLM never writes `DIVERSE` or `CONCENTRATED`.

## Why exact verdict equality is appropriate here

DiversityProof deliberately reduces each semantic observation to a small decision class about a frozen proposition. Prose rationales are not consensus state. Exact equality over `YES/NO/UNCLEAR/UNAVAILABLE` is therefore materially different from brittle exact equality over free-form model text.
