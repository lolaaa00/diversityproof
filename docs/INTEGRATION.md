# Integration

DiversityProof is designed to be consumed by another Intelligent Contract.

A consumer should pin all of the following off-chain or in its own state:

1. the DiversityProof contract address;
2. `committee_id`;
3. the exact `definition_hash` it is willing to trust.

Then the decision boundary is intentionally small:

```python
ok = diversityproof.is_diverse_for(committee_id, expected_definition_hash)
```

Do not infer stronger claims from `DIVERSE` than the contract makes. In particular, do not rename it to "independent providers" unless a separate mechanism proves provider identity/provenance.

## Example use cases

- a settlement contract requires a behaviourally non-cloned agent committee before accepting a multi-agent review;
- an autonomous treasury requires minimum decision diversity before enabling an execution path;
- a benchmark system records whether several public agents remain behaviourally differentiated across a frozen suite;
- a routing system chooses a fallback committee only when its latest DiversityProof measurement is `DIVERSE`.

`examples/diversity_gate.py` shows the intended interface shape without adding a second deployable contract to the repository.
