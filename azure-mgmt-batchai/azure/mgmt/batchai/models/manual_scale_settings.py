# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManualScaleSettings(Model):
    """Manual scale settings for the cluster.

    All required parameters must be populated in order to send to Azure.

    :param target_node_count: Required. Target node count. The desired number
     of compute nodes in the Cluster. Default is 0. Default value: 0 .
    :type target_node_count: int
    :param node_deallocation_option: Node deallocation options. An action to
     be performed when the cluster size is decreasing. The default value is
     requeue. Possible values include: 'requeue', 'terminate',
     'waitforjobcompletion'. Default value: "requeue" .
    :type node_deallocation_option: str or
     ~azure.mgmt.batchai.models.DeallocationOption
    """

    _validation = {
        'target_node_count': {'required': True},
    }

    _attribute_map = {
        'target_node_count': {'key': 'targetNodeCount', 'type': 'int'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManualScaleSettings, self).__init__(**kwargs)
        self.target_node_count = kwargs.get('target_node_count', 0)
        self.node_deallocation_option = kwargs.get('node_deallocation_option', "requeue")
