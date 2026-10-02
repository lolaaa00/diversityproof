# Studionet deployment evidence

Network target: **Studionet, chain 61999**

RPC:

```text
https://studio.genlayer.com/api
```

CLI policy for this handoff:

```text
repository-local GenLayer CLI 0.39.1 only
```

Do **not** deploy this repository to 61997 and do not fall back to a globally installed RC CLI.

## Verified preparation status (2 October 2026)

The repository-local CLI reports `0.39.1`. Network inspection reports alias
`studionet`, chain ID `61999`, and RPC `https://studio.genlayer.com/api`.
Preflight passes 21/21 and the real Direct Mode suite passes 29/29.

The active local account is named `probe` at public address
`0xaa18ecd158aec67c75a51768b747cb3247a21689`, with 8.2099 test GEN at the time
of inspection. No account named Lola is configured. Codex therefore did not
assume that this was the intended signer and did not deploy or sign a lifecycle
transaction.

No deployment transaction is currently claimed.

After Lola confirms or configures the intended signer, the finishing agent must:

1. run all static/preflight checks;
2. run Direct Mode on an environment where the GenVM test runtime works;
3. fix any genuine GenVM/linter incompatibility without weakening protocol invariants;
4. install the repository-local CLI (`npm install`) and verify exact version `0.39.1`;
5. deploy `contracts/diversityproof.py` to `https://studio.genlayer.com/api` only;
6. wait for and record FINALIZED deployment state;
7. execute at least one live diverse lifecycle and one live concentrated/inconclusive lifecycle against stable public audit fixtures;
8. verify deployed source parity against the final git commit;
9. replace this section with the contract address, deployment tx, lifecycle txs, finality states, commit SHA and source digest.

Never write `FINALIZED`, a contract address, a transaction hash or a passing live lifecycle into the documentation until it has actually been observed.
