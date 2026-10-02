"""Illustrative consumer pattern only; not a second required deployment.

A downstream Intelligent Contract can pin the exact DiversityProof definition
hash and require a current DIVERSE measurement before enabling a privileged path.
"""

# Pseudocode intentionally kept outside contracts/ so reviewers do not confuse
# the example with the one deployable primitive in this repository.
#
# @gl.public.write
# def execute_with_diverse_committee(committee_id, expected_definition_hash):
#     proof = gl.get_contract_at(DIVERSITYPROOF_ADDRESS)
#     if not proof.view().is_diverse_for(committee_id, expected_definition_hash):
#         raise gl.vm.UserError("committee is not diversity-certified")
#     ...
