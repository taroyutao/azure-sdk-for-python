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


class ImageReference(Model):
    """The OS image reference.

    All required parameters must be populated in order to send to Azure.

    :param publisher: Required. Publisher. Publisher of the image.
    :type publisher: str
    :param offer: Required. Offer. Offer of the image.
    :type offer: str
    :param sku: Required. SKU. SKU of the image.
    :type sku: str
    :param version: Version. Version of the image.
    :type version: str
    :param virtual_machine_image_id: Custom VM image resource ID. The ARM
     resource identifier of the virtual machine image for the compute nodes.
     This is of the form
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/images/{imageName}.
     The virtual machine image must be in the same region and subscription as
     the cluster. For information about the firewall settings for the Batch
     node agent to communicate with the Batch service see
     https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration.
     Note, you need to provide publisher, offer and sku of the base OS image of
     which the custom image has been derived from.
    :type virtual_machine_image_id: str
    """

    _validation = {
        'publisher': {'required': True},
        'offer': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'virtual_machine_image_id': {'key': 'virtualMachineImageId', 'type': 'str'},
    }

    def __init__(self, *, publisher: str, offer: str, sku: str, version: str=None, virtual_machine_image_id: str=None, **kwargs) -> None:
        super(ImageReference, self).__init__(**kwargs)
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
        self.virtual_machine_image_id = virtual_machine_image_id
