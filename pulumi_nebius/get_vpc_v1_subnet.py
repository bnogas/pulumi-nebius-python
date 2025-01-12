# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'GetVpcV1SubnetResult',
    'AwaitableGetVpcV1SubnetResult',
    'get_vpc_v1_subnet',
    'get_vpc_v1_subnet_output',
]

@pulumi.output_type
class GetVpcV1SubnetResult:
    """
    A collection of values returned by getVpcV1Subnet.
    """
    def __init__(__self__, created_at=None, id=None, ipv4_private_pools=None, ipv4_public_pools=None, labels=None, metadata=None, name=None, network_id=None, parent_id=None, resource_version=None, status=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4_private_pools and not isinstance(ipv4_private_pools, dict):
            raise TypeError("Expected argument 'ipv4_private_pools' to be a dict")
        pulumi.set(__self__, "ipv4_private_pools", ipv4_private_pools)
        if ipv4_public_pools and not isinstance(ipv4_public_pools, dict):
            raise TypeError("Expected argument 'ipv4_public_pools' to be a dict")
        pulumi.set(__self__, "ipv4_public_pools", ipv4_public_pools)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        pulumi.set(__self__, "parent_id", parent_id)
        if resource_version and not isinstance(resource_version, float):
            raise TypeError("Expected argument 'resource_version' to be a float")
        pulumi.set(__self__, "resource_version", resource_version)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv4PrivatePools")
    def ipv4_private_pools(self) -> 'outputs.GetVpcV1SubnetIpv4PrivatePoolsResult':
        return pulumi.get(self, "ipv4_private_pools")

    @property
    @pulumi.getter(name="ipv4PublicPools")
    def ipv4_public_pools(self) -> 'outputs.GetVpcV1SubnetIpv4PublicPoolsResult':
        return pulumi.get(self, "ipv4_public_pools")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metadata(self) -> 'outputs.GetVpcV1SubnetMetadataResult':
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> str:
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> float:
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.GetVpcV1SubnetStatusResult':
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")


class AwaitableGetVpcV1SubnetResult(GetVpcV1SubnetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcV1SubnetResult(
            created_at=self.created_at,
            id=self.id,
            ipv4_private_pools=self.ipv4_private_pools,
            ipv4_public_pools=self.ipv4_public_pools,
            labels=self.labels,
            metadata=self.metadata,
            name=self.name,
            network_id=self.network_id,
            parent_id=self.parent_id,
            resource_version=self.resource_version,
            status=self.status,
            updated_at=self.updated_at)


def get_vpc_v1_subnet(id: Optional[str] = None,
                      name: Optional[str] = None,
                      parent_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcV1SubnetResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['parentId'] = parent_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('nebius:index/getVpcV1Subnet:getVpcV1Subnet', __args__, opts=opts, typ=GetVpcV1SubnetResult, package_ref=_utilities.get_package()).value

    return AwaitableGetVpcV1SubnetResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        id=pulumi.get(__ret__, 'id'),
        ipv4_private_pools=pulumi.get(__ret__, 'ipv4_private_pools'),
        ipv4_public_pools=pulumi.get(__ret__, 'ipv4_public_pools'),
        labels=pulumi.get(__ret__, 'labels'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        network_id=pulumi.get(__ret__, 'network_id'),
        parent_id=pulumi.get(__ret__, 'parent_id'),
        resource_version=pulumi.get(__ret__, 'resource_version'),
        status=pulumi.get(__ret__, 'status'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_vpc_v1_subnet_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             parent_id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetVpcV1SubnetResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['parentId'] = parent_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('nebius:index/getVpcV1Subnet:getVpcV1Subnet', __args__, opts=opts, typ=GetVpcV1SubnetResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetVpcV1SubnetResult(
        created_at=pulumi.get(__response__, 'created_at'),
        id=pulumi.get(__response__, 'id'),
        ipv4_private_pools=pulumi.get(__response__, 'ipv4_private_pools'),
        ipv4_public_pools=pulumi.get(__response__, 'ipv4_public_pools'),
        labels=pulumi.get(__response__, 'labels'),
        metadata=pulumi.get(__response__, 'metadata'),
        name=pulumi.get(__response__, 'name'),
        network_id=pulumi.get(__response__, 'network_id'),
        parent_id=pulumi.get(__response__, 'parent_id'),
        resource_version=pulumi.get(__response__, 'resource_version'),
        status=pulumi.get(__response__, 'status'),
        updated_at=pulumi.get(__response__, 'updated_at')))
