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


class MountSettings(Model):
    """File Server Mount Information.

    :param mount_point: Mount Point. Path where the NFS is mounted on the File
     Server.
    :type mount_point: str
    :param file_server_public_ip: Public IP. Public IP address of the File
     Server which can be used to SSH to the node from outside of the subnet.
    :type file_server_public_ip: str
    :param file_server_internal_ip: Internal IP. Internal IP address of the
     File Server which can be used to access the File Server from within the
     subnet.
    :type file_server_internal_ip: str
    """

    _attribute_map = {
        'mount_point': {'key': 'mountPoint', 'type': 'str'},
        'file_server_public_ip': {'key': 'fileServerPublicIP', 'type': 'str'},
        'file_server_internal_ip': {'key': 'fileServerInternalIP', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MountSettings, self).__init__(**kwargs)
        self.mount_point = kwargs.get('mount_point', None)
        self.file_server_public_ip = kwargs.get('file_server_public_ip', None)
        self.file_server_internal_ip = kwargs.get('file_server_internal_ip', None)
