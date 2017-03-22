# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserImageResults(Model):
    """UserImageResults.

    :param evaluations:
    :type evaluations: list of :class:`UserImageEvaluation
     <training.models.UserImageEvaluation>`
    :param continuation_token:
    :type continuation_token: str
    """

    _attribute_map = {
        'evaluations': {'key': 'Evaluations', 'type': '[UserImageEvaluation]'},
        'continuation_token': {'key': 'ContinuationToken', 'type': 'str'},
    }

    def __init__(self, evaluations=None, continuation_token=None):
        self.evaluations = evaluations
        self.continuation_token = continuation_token