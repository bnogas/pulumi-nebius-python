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

__all__ = ['MspSparkV1alpha1ClusterArgs', 'MspSparkV1alpha1Cluster']

@pulumi.input_type
class MspSparkV1alpha1ClusterArgs:
    def __init__(__self__, *,
                 limits: pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs'],
                 network_id: pulumi.Input[str],
                 parent_id: pulumi.Input[str],
                 service_account_id: pulumi.Input[str],
                 authorization: Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MspSparkV1alpha1Cluster resource.
        :param pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs'] limits: Limits for the cluster
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] service_account_id: ID of the user service account for accessing S3 buckets in the user project
        :param pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs'] authorization: Password for Spark History server and Sessions.
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        """
        pulumi.set(__self__, "limits", limits)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "service_account_id", service_account_id)
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def limits(self) -> pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs']:
        """
        Limits for the cluster
        """
        return pulumi.get(self, "limits")

    @limits.setter
    def limits(self, value: pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs']):
        pulumi.set(self, "limits", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Input[str]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[str]:
        """
        ID of the user service account for accessing S3 buckets in the user project
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']]:
        """
        Password for Spark History server and Sessions.
        """
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _MspSparkV1alpha1ClusterState:
    def __init__(__self__, *,
                 authorization: Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 limits: Optional[pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs']] = None,
                 metadata: Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['MspSparkV1alpha1ClusterStatusArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MspSparkV1alpha1Cluster resources.
        :param pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs'] authorization: Password for Spark History server and Sessions.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs'] limits: Limits for the cluster
        :param pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] service_account_id: ID of the user service account for accessing S3 buckets in the user project
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if limits is not None:
            pulumi.set(__self__, "limits", limits)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']]:
        """
        Password for Spark History server and Sessions.
        """
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterAuthorizationArgs']]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs']]:
        """
        Limits for the cluster
        """
        return pulumi.get(self, "limits")

    @limits.setter
    def limits(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterLimitsArgs']]):
        pulumi.set(self, "limits", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterMetadataArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[pulumi.Input[float]]:
        """
        Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
        each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
        or current.
        """
        return pulumi.get(self, "resource_version")

    @resource_version.setter
    def resource_version(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "resource_version", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the user service account for accessing S3 buckets in the user project
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['MspSparkV1alpha1ClusterStatusArgs']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['MspSparkV1alpha1ClusterStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class MspSparkV1alpha1Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterAuthorizationArgs', 'MspSparkV1alpha1ClusterAuthorizationArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 limits: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterLimitsArgs', 'MspSparkV1alpha1ClusterLimitsArgsDict']]] = None,
                 metadata: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterMetadataArgs', 'MspSparkV1alpha1ClusterMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MspSparkV1alpha1Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterAuthorizationArgs', 'MspSparkV1alpha1ClusterAuthorizationArgsDict']] authorization: Password for Spark History server and Sessions.
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterLimitsArgs', 'MspSparkV1alpha1ClusterLimitsArgsDict']] limits: Limits for the cluster
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterMetadataArgs', 'MspSparkV1alpha1ClusterMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] service_account_id: ID of the user service account for accessing S3 buckets in the user project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MspSparkV1alpha1ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MspSparkV1alpha1Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MspSparkV1alpha1ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MspSparkV1alpha1ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterAuthorizationArgs', 'MspSparkV1alpha1ClusterAuthorizationArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 limits: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterLimitsArgs', 'MspSparkV1alpha1ClusterLimitsArgsDict']]] = None,
                 metadata: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterMetadataArgs', 'MspSparkV1alpha1ClusterMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MspSparkV1alpha1ClusterArgs.__new__(MspSparkV1alpha1ClusterArgs)

            __props__.__dict__["authorization"] = authorization
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            if limits is None and not opts.urn:
                raise TypeError("Missing required property 'limits'")
            __props__.__dict__["limits"] = limits
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        super(MspSparkV1alpha1Cluster, __self__).__init__(
            'nebius:index/mspSparkV1alpha1Cluster:MspSparkV1alpha1Cluster',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorization: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterAuthorizationArgs', 'MspSparkV1alpha1ClusterAuthorizationArgsDict']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            limits: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterLimitsArgs', 'MspSparkV1alpha1ClusterLimitsArgsDict']]] = None,
            metadata: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterMetadataArgs', 'MspSparkV1alpha1ClusterMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[Union['MspSparkV1alpha1ClusterStatusArgs', 'MspSparkV1alpha1ClusterStatusArgsDict']]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'MspSparkV1alpha1Cluster':
        """
        Get an existing MspSparkV1alpha1Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterAuthorizationArgs', 'MspSparkV1alpha1ClusterAuthorizationArgsDict']] authorization: Password for Spark History server and Sessions.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterLimitsArgs', 'MspSparkV1alpha1ClusterLimitsArgsDict']] limits: Limits for the cluster
        :param pulumi.Input[Union['MspSparkV1alpha1ClusterMetadataArgs', 'MspSparkV1alpha1ClusterMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] service_account_id: ID of the user service account for accessing S3 buckets in the user project
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MspSparkV1alpha1ClusterState.__new__(_MspSparkV1alpha1ClusterState)

        __props__.__dict__["authorization"] = authorization
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["limits"] = limits
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["status"] = status
        __props__.__dict__["updated_at"] = updated_at
        return MspSparkV1alpha1Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Optional['outputs.MspSparkV1alpha1ClusterAuthorization']]:
        """
        Password for Spark History server and Sessions.
        """
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def limits(self) -> pulumi.Output['outputs.MspSparkV1alpha1ClusterLimits']:
        """
        Limits for the cluster
        """
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.MspSparkV1alpha1ClusterMetadata']:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human readable name for the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> pulumi.Output[float]:
        """
        Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
        each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
        or current.
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[str]:
        """
        ID of the user service account for accessing S3 buckets in the user project
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.MspSparkV1alpha1ClusterStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

