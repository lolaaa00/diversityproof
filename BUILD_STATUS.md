# Build status

Verified locally on 2 October 2026:

- Repository-local GenLayer CLI: **0.39.1**.
- Python syntax compilation: **PASS** for the contract, Direct Mode tests, scripts, and example.
- Static architecture/security preflight: **21/21 PASS**.
- Real Direct Mode suite: **29 passed in 30.15s** after pinning the Direct Mode SDK to available compatible release `v0.2.16`.
- Target network inspection: **Genlayer Studio Network**, chain **61999**, RPC `https://studio.genlayer.com/api`.
- Frontend/backend directories: absent by design.
- Transparent static reviewer fixtures: committed under `fixtures/live/`.
- GitHub Actions: **PASS**, run `37004260271`, testing commit `b674a91542087af2f33f4964d5c434c98ec41ea6` with 29 passed and 0 failures.
- Contract source SHA-256: `706f8e69a4b66a8b4c11dbdc8b5374e2c393544ee41ccee2d3e09762aba6f6f0`.
- Studionet deployment: **FINALIZED / MAJORITY_AGREE** at `0x46BFFeA797588783ae5FA850206930fB443A8Ebc`.
- Live reviewer lifecycle: **DIVERSE, CONCENTRATED, and INCONCLUSIVE verified and finalized**.

Not claimed as verified:

- GenVM SDK validation. `genvm-linter==0.11.0` could not load the contract's pinned historical runner archive from its current SDK bundle (`filename ... not found`). Its reachability warning was addressed by placing nondeterministic calls directly in the leader and validator callbacks, but the final validation attempt could not complete and was stopped after it hung while resolving that missing archive.
All deployment and lifecycle claims are backed by finalized Studionet receipts and contract views recorded in `docs/DEPLOYMENT.md`.
