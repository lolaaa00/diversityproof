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
GitHub Actions run `37004260271` passed against commit
`b674a91542087af2f33f4964d5c434c98ec41ea6` with 29 tests and 0 failures.
The repository contract source SHA-256 is
`706f8e69a4b66a8b4c11dbdc8b5374e2c393544ee41ccee2d3e09762aba6f6f0`.
The active local account is named `probe` at public address
`0xaa18ecd158aec67c75a51768b747cb3247a21689`, with 8.2099 test GEN at the time
of the pre-deployment inspection. The user subsequently authorized completing
the remaining deployment work with the active configured signer.

## Finalized deployment

- Contract: `0x46BFFeA797588783ae5FA850206930fB443A8Ebc`
- Deployment transaction: `0xdd97173fad3be3f649461c9d07fcf036b418ca473d2b2652fa4c955c80aef17f`
- Finality: `FINALIZED`
- Consensus result: `MAJORITY_AGREE`
- Source commit deployed: `7e4dce5d36f916da9132a0b306385aefe706ba5e`
- Local source SHA-256: `706f8e69a4b66a8b4c11dbdc8b5374e2c393544ee41ccee2d3e09762aba6f6f0`
- Retrieved source SHA-256 after normalizing the CLI's two extra trailing newlines: `706f8e69a4b66a8b4c11dbdc8b5374e2c393544ee41ccee2d3e09762aba6f6f0`
- Normalized source parity: exact match

## Finalized DIVERSE lifecycle

- Committee ID: `1`; member IDs: `1, 2, 3`; probe IDs: `1, 2, 3`; measurement ID: `1`
- Definition hash: `8d6e99ceb937a1d05f038d19b3909be85e1a816d65ae19601ad0eae5041c1dc8`
- Certificate hash: `8f25c934173a60ece0bf162176cadb1a1a957d4782ee78cb44cbd009de3ee8f3`
- Verdict vector: `NO, NO, YES / YES, YES, YES / NO, YES, NO`
- Every pair: 3 comparable, 2 different, `6666` bps
- Result: `DIVERSE`; measurement tx `0xa2f3e01ae5fd183eac8b6aa30b8613b76cffa1f6cc8cfbdd375fccfd76034b23` (`FINALIZED`)
- Exact `is_diverse_for` hash: `true`
- One-character-altered hash (`0d6e...c1dc8`): `false`
- Create tx: `0x4b96c0580ffe92f096ba326adcc8da01d9e472551970bb9255d184f75d9276a2`
- Member txs: `0x476ad2c680c2fe81e49dccc07816e8f6010226cb567c68a49123b062426f433f`, `0xf294d113e6f4bf8f92a8a849e6fd454e3a13e9bdd27061e43d97223169922794`, `0xbd95a9bbdc783aef22091ff77ee38a7e667e27d5438626c01e2b8abcfc2fb211`
- Probe txs: `0xc2f2763b34ad558a502aa3f6c7ac136433d1068cb1173b4649cdb9a0bf0c7b83`, `0x060e337bd9a772c7457862a1caa4b7c114a65ec9c59bed4e0a9dd291d70d7b61`, `0x7ffa11cabd416af896660e8a20b7b710e8231d522f18a6d1a83a8f80665574a1`
- Seal tx: `0x9ebf1a2c65b110ea74c40e69b3d8ca47a57d5fc58d9eeabf16694cb243004edd`

## Finalized CONCENTRATED lifecycle

- Committee ID: `2`; member IDs: `4, 5, 6`; probe IDs: `4, 5, 6`; measurement ID: `2`
- Definition hash: `beff3a3e2d838df42a77cb71f2344a72d26cf8338ee846dd858ca0bcdbf0c619`
- Certificate hash: `f9890579b4d6b3d47bebc62fbae291b08795bc3ac922272e58b4d44b22cc0d2c`
- Clone pair: 3 comparable, 0 different, `0` bps
- Result: `CONCENTRATED`; measurement tx `0x001b444348de94dd6e86b3126ed88de66a63b4bde4173466dcee2817171e4215` (`FINALIZED`)
- Create tx: `0xb48cb4628a0e6863be249a64eccb4a5ce510e24031e2edbe0d6b0e29a9b80230`
- Member txs: `0x82e29af50b2869f1bbcd647b21a1855110423d85006c76e31f5e5bb6775ccdfd`, `0x81edb2a8afd4c7be1d1c17756d1cc34c27c71b64799b8f23df09e55875d373af`, `0x1c36c05a053caa7f82131dd60b9748e8d14aecaf2004a962f546f2baf308f20b`
- Probe txs: `0xc317c5d7f849d80a1d8e383c06828db8b5f4daf042db33bce54e859db5f6e7eb`, `0x8f23ceeae43fbe3054c1e1159c5e55a0c566cdadaf914092b7d761afd9246417`, `0x59b0e95ac62b6038cdf05d62f0ba286d72877f32eaeb4d77a43d4ec6e3c16aee`
- Seal tx: `0x7e745057639224e9f1608a1a41810a6d34dd2ed6894fb1f288e652aa1ade9e57`

## Finalized INCONCLUSIVE lifecycle

- Committee ID: `3`; member IDs: `7, 8`; probe IDs: `7, 8, 9`; measurement ID: `3`
- Definition hash: `64b7946499f0af5fa6fc6c87c0cf00f23546585af837bd2372b2d36027b68163`
- Certificate hash: `b1890d10866ddce4905186acb1ce91c465e624dbcf81dbff4af122614a84068c`
- Pair: 0 comparable, 0 different, `0` bps; insufficient pairs: `1`
- Verdict vector: `NO, NO, YES / UNCLEAR, UNCLEAR, UNCLEAR`
- Result: `INCONCLUSIVE`; measurement tx `0x2bcf3b704b6eed7f25da58268b57168c1c312ee59bfb4273e91b59a82b46ab88` (`FINALIZED`)
- Create tx: `0x44cae15f3c4382ae3b0835931d5d77ffc09e69be3b59f20d119e1fc1b247d3b2`
- Member txs: `0xe9188ffd9395852046a5d932d74ad9916391c1b76d100b6a8a84293bb47795f6`, `0xc62fe32ebb52fbc07f3ee7770407278df6869d98c745514a0fa57d9bc294c286`
- Probe txs: `0x3e515f7c0764aa269e27642987f32d348deed411de056cb3d92f904aecf09726`, `0x0b5e4ff370f65865c65b7e619544eb3971dbb4399c7759c5d47b725e60a23b27`, `0xa4c9e35206d4a1ec953801ed5e48fbf516f74fd4bc3b3db2c6d4565e6cdb0e8c`
- Seal tx: `0x7dca1694264084c13362ebe394f714fbfe611372953c942b7605707d6e9d14b2`
