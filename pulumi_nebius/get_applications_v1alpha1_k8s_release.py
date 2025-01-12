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
from ._inputs import *

__all__ = [
    'GetApplicationsV1alpha1K8sReleaseResult',
    'AwaitableGetApplicationsV1alpha1K8sReleaseResult',
    'get_applications_v1alpha1_k8s_release',
    'get_applications_v1alpha1_k8s_release_output',
]

@pulumi.output_type
class GetApplicationsV1alpha1K8sReleaseResult:
    """
    A collection of values returned by getApplicationsV1alpha1K8sRelease.
    """
    def __init__(__self__, application_name=None, cluster_id=None, created_at=None, id=None, labels=None, metadata=None, name=None, namespace=None, parent_id=None, product_slug=None, resource_version=None, set=None, status=None, updated_at=None, values=None):
        if application_name and not isinstance(application_name, str):
            raise TypeError("Expected argument 'application_name' to be a str")
        pulumi.set(__self__, "application_name", application_name)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
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
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        pulumi.set(__self__, "parent_id", parent_id)
        if product_slug and not isinstance(product_slug, str):
            raise TypeError("Expected argument 'product_slug' to be a str")
        pulumi.set(__self__, "product_slug", product_slug)
        if resource_version and not isinstance(resource_version, float):
            raise TypeError("Expected argument 'resource_version' to be a float")
        pulumi.set(__self__, "resource_version", resource_version)
        if set and not isinstance(set, dict):
            raise TypeError("Expected argument 'set' to be a dict")
        pulumi.set(__self__, "set", set)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if values and not isinstance(values, str):
            raise TypeError("Expected argument 'values' to be a str")
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> str:
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

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
    def metadata(self) -> 'outputs.GetApplicationsV1alpha1K8sReleaseMetadataResult':
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> str:
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="productSlug")
    def product_slug(self) -> str:
        return pulumi.get(self, "product_slug")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> float:
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter
    def set(self) -> Mapping[str, str]:
        return pulumi.get(self, "set")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.GetApplicationsV1alpha1K8sReleaseStatusResult':
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def values(self) -> str:
        return pulumi.get(self, "values")


class AwaitableGetApplicationsV1alpha1K8sReleaseResult(GetApplicationsV1alpha1K8sReleaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationsV1alpha1K8sReleaseResult(
            application_name=self.application_name,
            cluster_id=self.cluster_id,
            created_at=self.created_at,
            id=self.id,
            labels=self.labels,
            metadata=self.metadata,
            name=self.name,
            namespace=self.namespace,
            parent_id=self.parent_id,
            product_slug=self.product_slug,
            resource_version=self.resource_version,
            set=self.set,
            status=self.status,
            updated_at=self.updated_at,
            values=self.values)


def get_applications_v1alpha1_k8s_release(id: Optional[str] = None,
                                          metadata: Optional[Union['GetApplicationsV1alpha1K8sReleaseMetadataArgs', 'GetApplicationsV1alpha1K8sReleaseMetadataArgsDict']] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationsV1alpha1K8sReleaseResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['metadata'] = metadata
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('nebius:index/getApplicationsV1alpha1K8sRelease:getApplicationsV1alpha1K8sRelease', __args__, opts=opts, typ=GetApplicationsV1alpha1K8sReleaseResult, package_ref=_utilities.get_package()).value

    return AwaitableGetApplicationsV1alpha1K8sReleaseResult(
        application_name=pulumi.get(__ret__, 'application_name'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        namespace=pulumi.get(__ret__, 'namespace'),
        parent_id=pulumi.get(__ret__, 'parent_id'),
        product_slug=pulumi.get(__ret__, 'product_slug'),
        resource_version=pulumi.get(__ret__, 'resource_version'),
        set=pulumi.get(__ret__, 'set'),
        status=pulumi.get(__ret__, 'status'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        values=pulumi.get(__ret__, 'values'))
def get_applications_v1alpha1_k8s_release_output(id: Optional[pulumi.Input[str]] = None,
                                                 metadata: Optional[pulumi.Input[Optional[Union['GetApplicationsV1alpha1K8sReleaseMetadataArgs', 'GetApplicationsV1alpha1K8sReleaseMetadataArgsDict']]]] = None,
                                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetApplicationsV1alpha1K8sReleaseResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['metadata'] = metadata
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('nebius:index/getApplicationsV1alpha1K8sRelease:getApplicationsV1alpha1K8sRelease', __args__, opts=opts, typ=GetApplicationsV1alpha1K8sReleaseResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetApplicationsV1alpha1K8sReleaseResult(
        application_name=pulumi.get(__response__, 'application_name'),
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        created_at=pulumi.get(__response__, 'created_at'),
        id=pulumi.get(__response__, 'id'),
        labels=pulumi.get(__response__, 'labels'),
        metadata=pulumi.get(__response__, 'metadata'),
        name=pulumi.get(__response__, 'name'),
        namespace=pulumi.get(__response__, 'namespace'),
        parent_id=pulumi.get(__response__, 'parent_id'),
        product_slug=pulumi.get(__response__, 'product_slug'),
        resource_version=pulumi.get(__response__, 'resource_version'),
        set=pulumi.get(__response__, 'set'),
        status=pulumi.get(__response__, 'status'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        values=pulumi.get(__response__, 'values')))
