"""Inspect the installed pack identity."""

from identity_proofing_enrollment_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:identity-proofing-enrollment"
print(metadata["origin"]["id"])
