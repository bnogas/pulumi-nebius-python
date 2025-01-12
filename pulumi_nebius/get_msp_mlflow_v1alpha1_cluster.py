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
    'GetMspMlflowV1alpha1ClusterResult',
    'AwaitableGetMspMlflowV1alpha1ClusterResult',
    'get_msp_mlflow_v1alpha1_cluster',
    'get_msp_mlflow_v1alpha1_cluster_output',
]

@pulumi.output_type
class GetMspMlflowV1alpha1ClusterResult:
    """
    A collection of values returned by getMspMlflowV1alpha1Cluster.
    """
    def __init__(__self__, admin_password=None, admin_username=None, created_at=None, description=None, id=None, labels=None, metadata=None, name=None, network_id=None, parent_id=None, public_access=None, resource_version=None, service_account_id=None, status=None, storage_bucket_name=None, updated_at=None):
        if admin_password and not isinstance(admin_password, str):
            raise TypeError("Expected argument 'admin_password' to be a str")
        pulumi.set(__self__, "admin_password", admin_password)
        if admin_username and not isinstance(admin_username, str):
            raise TypeError("Expected argument 'admin_username' to be a str")
        pulumi.set(__self__, "admin_username", admin_username)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
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
        if public_access and not isinstance(public_access, bool):
            raise TypeError("Expected argument 'public_access' to be a bool")
        pulumi.set(__self__, "public_access", public_access)
        if resource_version and not isinstance(resource_version, float):
            raise TypeError("Expected argument 'resource_version' to be a float")
        pulumi.set(__self__, "resource_version", resource_version)
        if service_account_id and not isinstance(service_account_id, str):
            raise TypeError("Expected argument 'service_account_id' to be a str")
        pulumi.set(__self__, "service_account_id", service_account_id)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if storage_bucket_name and not isinstance(storage_bucket_name, str):
            raise TypeError("Expected argument 'storage_bucket_name' to be a str")
        pulumi.set(__self__, "storage_bucket_name", storage_bucket_name)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> str:
        return pulumi.get(self, "admin_password")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> str:
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metadata(self) -> 'outputs.GetMspMlflowV1alpha1ClusterMetadataResult':
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
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> bool:
        return pulumi.get(self, "public_access")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> float:
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> str:
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.GetMspMlflowV1alpha1ClusterStatusResult':
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageBucketName")
    def storage_bucket_name(self) -> str:
        return pulumi.get(self, "storage_bucket_name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")


class AwaitableGetMspMlflowV1alpha1ClusterResult(GetMspMlflowV1alpha1ClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMspMlflowV1alpha1ClusterResult(
            admin_password=self.admin_password,
            admin_username=self.admin_username,
            created_at=self.created_at,
            description=self.description,
            id=self.id,
            labels=self.labels,
            metadata=self.metadata,
            name=self.name,
            network_id=self.network_id,
            parent_id=self.parent_id,
            public_access=self.public_access,
            resource_version=self.resource_version,
            service_account_id=self.service_account_id,
            status=self.status,
            storage_bucket_name=self.storage_bucket_name,
            updated_at=self.updated_at)


def get_msp_mlflow_v1alpha1_cluster(id: Optional[str] = None,
                                    name: Optional[str] = None,
                                    parent_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMspMlflowV1alpha1ClusterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['parentId'] = parent_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('nebius:index/getMspMlflowV1alpha1Cluster:getMspMlflowV1alpha1Cluster', __args__, opts=opts, typ=GetMspMlflowV1alpha1ClusterResult, package_ref=_utilities.get_package()).value

    return AwaitableGetMspMlflowV1alpha1ClusterResult(
        admin_password=pulumi.get(__ret__, 'admin_password'),
        admin_username=pulumi.get(__ret__, 'admin_username'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        network_id=pulumi.get(__ret__, 'network_id'),
        parent_id=pulumi.get(__ret__, 'parent_id'),
        public_access=pulumi.get(__ret__, 'public_access'),
        resource_version=pulumi.get(__ret__, 'resource_version'),
        service_account_id=pulumi.get(__ret__, 'service_account_id'),
        status=pulumi.get(__ret__, 'status'),
        storage_bucket_name=pulumi.get(__ret__, 'storage_bucket_name'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_msp_mlflow_v1alpha1_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                           name: Optional[pulumi.Input[Optional[str]]] = None,
                                           parent_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetMspMlflowV1alpha1ClusterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['parentId'] = parent_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('nebius:index/getMspMlflowV1alpha1Cluster:getMspMlflowV1alpha1Cluster', __args__, opts=opts, typ=GetMspMlflowV1alpha1ClusterResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetMspMlflowV1alpha1ClusterResult(
        admin_password=pulumi.get(__response__, 'admin_password'),
        admin_username=pulumi.get(__response__, 'admin_username'),
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        labels=pulumi.get(__response__, 'labels'),
        metadata=pulumi.get(__response__, 'metadata'),
        name=pulumi.get(__response__, 'name'),
        network_id=pulumi.get(__response__, 'network_id'),
        parent_id=pulumi.get(__response__, 'parent_id'),
        public_access=pulumi.get(__response__, 'public_access'),
        resource_version=pulumi.get(__response__, 'resource_version'),
        service_account_id=pulumi.get(__response__, 'service_account_id'),
        status=pulumi.get(__response__, 'status'),
        storage_bucket_name=pulumi.get(__response__, 'storage_bucket_name'),
        updated_at=pulumi.get(__response__, 'updated_at')))
