# identity-proofing-enrollment-governance-pack

Governance for identity proofing, enrollment, IAL selection, evidence validation, subscriber account establishment, fraud controls, privacy, and audit evidence.

## Package identity

- Pack ID: `pack:identity-proofing-enrollment`
- PyPI distribution: `identity-proofing-enrollment-governance-pack`
- Python import: `identity_proofing_enrollment_governance_pack`
- Reservation owner: `extension-pack:identity-proofing-enrollment-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add identity-proofing-enrollment-governance-pack
uv run ssot pack sync . identity_proofing_enrollment_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://pages.nist.gov/800-63-4/sp800-63a.html
- https://pages.nist.gov/800-63-4/sp800-63.html
