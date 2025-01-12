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

__all__ = ['MspMlflowV1alpha1ClusterArgs', 'MspMlflowV1alpha1Cluster']

@pulumi.input_type
class MspMlflowV1alpha1ClusterArgs:
    def __init__(__self__, *,
                 admin_password: pulumi.Input[str],
                 admin_username: pulumi.Input[str],
                 network_id: pulumi.Input[str],
                 parent_id: pulumi.Input[str],
                 service_account_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_access: Optional[pulumi.Input[bool]] = None,
                 storage_bucket_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MspMlflowV1alpha1Cluster resource.
        :param pulumi.Input[str] admin_password: MLflow admin password.
        :param pulumi.Input[str] admin_username: MLflow admin username.
        :param pulumi.Input[str] network_id: ID of the vpc network.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] service_account_id: Id of the service account that will be used to access S3 bucket (and create one if not provided).
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[bool] public_access: Either make cluster public accessible or accessible only via private VPC.
        :param pulumi.Input[str] storage_bucket_name: Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        """
        pulumi.set(__self__, "admin_password", admin_password)
        pulumi.set(__self__, "admin_username", admin_username)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "service_account_id", service_account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_access is not None:
            pulumi.set(__self__, "public_access", public_access)
        if storage_bucket_name is not None:
            pulumi.set(__self__, "storage_bucket_name", storage_bucket_name)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> pulumi.Input[str]:
        """
        MLflow admin password.
        """
        return pulumi.get(self, "admin_password")

    @admin_password.setter
    def admin_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_password", value)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Input[str]:
        """
        MLflow admin username.
        """
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "admin_username", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        ID of the vpc network.
        """
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
        Id of the service account that will be used to access S3 bucket (and create one if not provided).
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_id", value)

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
    def metadata(self) -> Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']]):
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
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Either make cluster public accessible or accessible only via private VPC.
        """
        return pulumi.get(self, "public_access")

    @public_access.setter
    def public_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_access", value)

    @property
    @pulumi.getter(name="storageBucketName")
    def storage_bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        """
        return pulumi.get(self, "storage_bucket_name")

    @storage_bucket_name.setter
    def storage_bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_bucket_name", value)


@pulumi.input_type
class _MspMlflowV1alpha1ClusterState:
    def __init__(__self__, *,
                 admin_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 public_access: Optional[pulumi.Input[bool]] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['MspMlflowV1alpha1ClusterStatusArgs']] = None,
                 storage_bucket_name: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MspMlflowV1alpha1Cluster resources.
        :param pulumi.Input[str] admin_password: MLflow admin password.
        :param pulumi.Input[str] admin_username: MLflow admin username.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] network_id: ID of the vpc network.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[bool] public_access: Either make cluster public accessible or accessible only via private VPC.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] service_account_id: Id of the service account that will be used to access S3 bucket (and create one if not provided).
        :param pulumi.Input[str] storage_bucket_name: Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if admin_password is not None:
            pulumi.set(__self__, "admin_password", admin_password)
        if admin_username is not None:
            pulumi.set(__self__, "admin_username", admin_username)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if public_access is not None:
            pulumi.set(__self__, "public_access", public_access)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if storage_bucket_name is not None:
            pulumi.set(__self__, "storage_bucket_name", storage_bucket_name)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[str]]:
        """
        MLflow admin password.
        """
        return pulumi.get(self, "admin_password")

    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_password", value)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[str]]:
        """
        MLflow admin username.
        """
        return pulumi.get(self, "admin_username")

    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_username", value)

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
    def metadata(self) -> Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MspMlflowV1alpha1ClusterMetadataArgs']]):
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
        """
        ID of the vpc network.
        """
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
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Either make cluster public accessible or accessible only via private VPC.
        """
        return pulumi.get(self, "public_access")

    @public_access.setter
    def public_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_access", value)

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
        Id of the service account that will be used to access S3 bucket (and create one if not provided).
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['MspMlflowV1alpha1ClusterStatusArgs']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['MspMlflowV1alpha1ClusterStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="storageBucketName")
    def storage_bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        """
        return pulumi.get(self, "storage_bucket_name")

    @storage_bucket_name.setter
    def storage_bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_bucket_name", value)

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


class MspMlflowV1alpha1Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['MspMlflowV1alpha1ClusterMetadataArgs', 'MspMlflowV1alpha1ClusterMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 public_access: Optional[pulumi.Input[bool]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 storage_bucket_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MspMlflowV1alpha1Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_password: MLflow admin password.
        :param pulumi.Input[str] admin_username: MLflow admin username.
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['MspMlflowV1alpha1ClusterMetadataArgs', 'MspMlflowV1alpha1ClusterMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] network_id: ID of the vpc network.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[bool] public_access: Either make cluster public accessible or accessible only via private VPC.
        :param pulumi.Input[str] service_account_id: Id of the service account that will be used to access S3 bucket (and create one if not provided).
        :param pulumi.Input[str] storage_bucket_name: Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MspMlflowV1alpha1ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MspMlflowV1alpha1Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MspMlflowV1alpha1ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MspMlflowV1alpha1ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_password: Optional[pulumi.Input[str]] = None,
                 admin_username: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['MspMlflowV1alpha1ClusterMetadataArgs', 'MspMlflowV1alpha1ClusterMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 public_access: Optional[pulumi.Input[bool]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 storage_bucket_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MspMlflowV1alpha1ClusterArgs.__new__(MspMlflowV1alpha1ClusterArgs)

            if admin_password is None and not opts.urn:
                raise TypeError("Missing required property 'admin_password'")
            __props__.__dict__["admin_password"] = None if admin_password is None else pulumi.Output.secret(admin_password)
            if admin_username is None and not opts.urn:
                raise TypeError("Missing required property 'admin_username'")
            __props__.__dict__["admin_username"] = admin_username
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["public_access"] = public_access
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["storage_bucket_name"] = storage_bucket_name
            __props__.__dict__["created_at"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["adminPassword"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MspMlflowV1alpha1Cluster, __self__).__init__(
            'nebius:index/mspMlflowV1alpha1Cluster:MspMlflowV1alpha1Cluster',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_password: Optional[pulumi.Input[str]] = None,
            admin_username: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            metadata: Optional[pulumi.Input[Union['MspMlflowV1alpha1ClusterMetadataArgs', 'MspMlflowV1alpha1ClusterMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            public_access: Optional[pulumi.Input[bool]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[Union['MspMlflowV1alpha1ClusterStatusArgs', 'MspMlflowV1alpha1ClusterStatusArgsDict']]] = None,
            storage_bucket_name: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'MspMlflowV1alpha1Cluster':
        """
        Get an existing MspMlflowV1alpha1Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_password: MLflow admin password.
        :param pulumi.Input[str] admin_username: MLflow admin username.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[str] description: Description of the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['MspMlflowV1alpha1ClusterMetadataArgs', 'MspMlflowV1alpha1ClusterMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] network_id: ID of the vpc network.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[bool] public_access: Either make cluster public accessible or accessible only via private VPC.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] service_account_id: Id of the service account that will be used to access S3 bucket (and create one if not provided).
        :param pulumi.Input[str] storage_bucket_name: Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MspMlflowV1alpha1ClusterState.__new__(_MspMlflowV1alpha1ClusterState)

        __props__.__dict__["admin_password"] = admin_password
        __props__.__dict__["admin_username"] = admin_username
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["public_access"] = public_access
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["status"] = status
        __props__.__dict__["storage_bucket_name"] = storage_bucket_name
        __props__.__dict__["updated_at"] = updated_at
        return MspMlflowV1alpha1Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> pulumi.Output[str]:
        """
        MLflow admin password.
        """
        return pulumi.get(self, "admin_password")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Output[str]:
        """
        MLflow admin username.
        """
        return pulumi.get(self, "admin_username")

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
    def metadata(self) -> pulumi.Output['outputs.MspMlflowV1alpha1ClusterMetadata']:
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
        """
        ID of the vpc network.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> pulumi.Output[Optional[bool]]:
        """
        Either make cluster public accessible or accessible only via private VPC.
        """
        return pulumi.get(self, "public_access")

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
        Id of the service account that will be used to access S3 bucket (and create one if not provided).
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.MspMlflowV1alpha1ClusterStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageBucketName")
    def storage_bucket_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Nebius S3 bucket for MLflow artifacts. If not provided, will be created under the same parent.
        """
        return pulumi.get(self, "storage_bucket_name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

