# Identity Proofing and Enrollment Governance pack guide

Governance for identity proofing, enrollment, IAL selection, evidence validation, subscriber account establishment, fraud controls, privacy, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `identity-proofing-enrollment-governance-pack` is an installable SSOT governance pack for Identity Proofing and Enrollment. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for identity proofing and enrollment, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`identity-proofing-enrollment-governance-pack`](https://pypi.org/project/identity-proofing-enrollment-governance-pack/)
- GitHub package repository: [`groupsum/identity-proofing-enrollment-governance-pack`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack)
- Import package: `identity_proofing_enrollment_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 5 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:identity-proofing-enrollment`
- PyPI package: `identity-proofing-enrollment-governance-pack`
- Import package: `identity_proofing_enrollment_governance_pack`
- GitHub repository: [groupsum/identity-proofing-enrollment-governance-pack](https://github.com/groupsum/identity-proofing-enrollment-governance-pack)
- Reservation owner: `extension-pack:identity-proofing-enrollment-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Identity Proofing and Enrollment

## Authority Sources

- [NIST SP 800-63A-4: Identity Proofing and Enrollment](https://pages.nist.gov/800-63-4/sp800-63a.html)
- [NIST SP 800-63-4: Digital Identity Guidelines](https://pages.nist.gov/800-63-4/sp800-63.html)

## Included ADRs

- [`adr:identity-proofing-and-enrollment-use-nist-sp-800-63a-4`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/adr/ADR-1000-identity-proofing-and-enrollment-use-nist-sp-800-63a-4.yaml) - Identity Proofing And Enrollment Use Nist Sp 800 63a 4
- [`adr:ial-is-independent-from-aal-and-fal`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/adr/ADR-1001-ial-is-independent-from-aal-and-fal.yaml) - IAL Is Independent From AAL And FAL
- [`adr:proofing-evidence-and-fraud-controls-are-explicit`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/adr/ADR-1002-proofing-evidence-and-fraud-controls-are-explicit.yaml) - Proofing Evidence And Fraud Controls Are Explicit

## Included SPECs

- [`spc:identity-proofing-and-enrollment-contract`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/specs/SPEC-2000-identity-proofing-and-enrollment-contract.yaml) - Identity Proofing And Enrollment Contract
- [`spc:identity-assurance-level-selection-contract`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/specs/SPEC-2001-identity-assurance-level-selection-contract.yaml) - Identity Assurance Level Selection Contract
- [`spc:evidence-validation-and-identity-resolution-contract`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/specs/SPEC-2002-evidence-validation-and-identity-resolution-contract.yaml) - Evidence Validation And Identity Resolution Contract
- [`spc:subscriber-account-enrollment-contract`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/specs/SPEC-2003-subscriber-account-enrollment-contract.yaml) - Subscriber Account Enrollment Contract
- [`spc:proofing-failure-privacy-and-audit-contract`](https://github.com/groupsum/identity-proofing-enrollment-governance-pack/blob/master/src/identity_proofing_enrollment_governance_pack/templates/specs/SPEC-2004-proofing-failure-privacy-and-audit-contract.yaml) - Proofing Failure Privacy And Audit Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect identity_proofing_enrollment_governance_pack
uvx --from ssot-registry ssot pack preflight . identity_proofing_enrollment_governance_pack --all
uvx --from ssot-registry ssot pack sync . identity_proofing_enrollment_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from identity_proofing_enrollment_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-identity-proofing-and-enrollment-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/identity-proofing-enrollment-governance-pack](https://github.com/groupsum/identity-proofing-enrollment-governance-pack)
- PyPI package: [identity-proofing-enrollment-governance-pack](https://pypi.org/project/identity-proofing-enrollment-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the identity proofing and enrollment governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
