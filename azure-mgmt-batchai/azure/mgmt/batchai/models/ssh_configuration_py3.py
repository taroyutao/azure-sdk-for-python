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


class SshConfiguration(Model):
    """SSH configuration.

    All required parameters must be populated in order to send to Azure.

    :param public_ips_to_allow: Allowed public IPs. List of source IP ranges
     to allow SSH connection from. The default value is '*' (all source IPs are
     allowed). Maximum number of IP ranges that can be specified is 400.
    :type public_ips_to_allow: list[str]
    :param user_account_settings: Required. User account settings. Settings
     for administrator user account to be created on a node. The account can be
     used to establish SSH connection to the node.
    :type user_account_settings:
     ~azure.mgmt.batchai.models.UserAccountSettings
    """

    _validation = {
        'user_account_settings': {'required': True},
    }

    _attribute_map = {
        'public_ips_to_allow': {'key': 'publicIPsToAllow', 'type': '[str]'},
        'user_account_settings': {'key': 'userAccountSettings', 'type': 'UserAccountSettings'},
    }

    def __init__(self, *, user_account_settings, public_ips_to_allow=None, **kwargs) -> None:
        super(SshConfiguration, self).__init__(**kwargs)
        self.public_ips_to_allow = public_ips_to_allow
        self.user_account_settings = user_account_settings
