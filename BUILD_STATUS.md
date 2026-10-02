# Build status

Verified locally on 2 October 2026:

- Repository-local GenLayer CLI: **0.39.1**.
- Python syntax compilation: **PASS** for the contract, Direct Mode tests, scripts, and example.
- Static architecture/security preflight: **21/21 PASS**.
- Real Direct Mode suite: **29 passed in 30.15s** after pinning the Direct Mode SDK to available compatible release `v0.2.16`.
- Target network inspection: **Genlayer Studio Network**, chain **61999**, RPC `https://studio.genlayer.com/api`.
- Frontend/backend directories: absent by design.
- Transparent static reviewer fixtures: committed under `fixtures/live/`.

Not claimed as verified:

- GenVM SDK validation. `genvm-linter==0.11.0` could not load the contract's pinned historical runner archive from its current SDK bundle (`filename ... not found`). Its reachability warning was addressed by placing nondeterministic calls directly in the leader and validator callbacks, but the final validation attempt could not complete and was stopped after it hung while resolving that missing archive.
- Live Studionet deployment. The active local account is named `probe`; no account named Lola is configured, so Codex did not assume signing authority or deploy.
- Live DIVERSE, CONCENTRATED, or INCONCLUSIVE lifecycle results.
- GitHub Actions status until the initial commit is pushed and the workflow completes.

No deployment address, transaction hash, finality result, CI run, or live lifecycle result is fabricated here.
