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


class AzureBlobFileSystemReference(Model):
    """Azure Blob Storage Container mounting configuration.

    All required parameters must be populated in order to send to Azure.

    :param account_name: Required. Account name. Name of the Azure storage
     account.
    :type account_name: str
    :param container_name: Required. Container name. Name of the Azure Blob
     Storage container to mount on the cluster.
    :type container_name: str
    :param credentials: Required. Credentials. Information about the Azure
     storage credentials.
    :type credentials: ~azure.mgmt.batchai.models.AzureStorageCredentialsInfo
    :param relative_mount_path: Required. Relative mount path. The relative
     path on the compute node where the Azure File container will be mounted.
     Note that all cluster level containers will be mounted under
     $AZ_BATCHAI_MOUNT_ROOT location and all job level containers will be
     mounted under $AZ_BATCHAI_JOB_MOUNT_ROOT.
    :type relative_mount_path: str
    :param mount_options: Mount options. Mount options for mounting blobfuse
     file system.
    :type mount_options: str
    """

    _validation = {
        'account_name': {'required': True},
        'container_name': {'required': True},
        'credentials': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'account_name': {'key': 'accountName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'AzureStorageCredentialsInfo'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
        'mount_options': {'key': 'mountOptions', 'type': 'str'},
    }

    def __init__(self, *, account_name: str, container_name: str, credentials, relative_mount_path: str, mount_options: str=None, **kwargs) -> None:
        super(AzureBlobFileSystemReference, self).__init__(**kwargs)
        self.account_name = account_name
        self.container_name = container_name
        self.credentials = credentials
        self.relative_mount_path = relative_mount_path
        self.mount_options = mount_options
