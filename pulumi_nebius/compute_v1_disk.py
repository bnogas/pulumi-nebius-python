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

__all__ = ['ComputeV1DiskArgs', 'ComputeV1Disk']

@pulumi.input_type
class ComputeV1DiskArgs:
    def __init__(__self__, *,
                 parent_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 block_size_bytes: Optional[pulumi.Input[float]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['ComputeV1DiskMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 placement_policy: Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']] = None,
                 size_bytes: Optional[pulumi.Input[float]] = None,
                 size_gibibytes: Optional[pulumi.Input[float]] = None,
                 size_kibibytes: Optional[pulumi.Input[float]] = None,
                 size_mebibytes: Optional[pulumi.Input[float]] = None,
                 source_image_family: Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComputeV1Disk resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] type: ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
               `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['ComputeV1DiskMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[float] size_bytes: *Cannot be set alongside size_kibibytes or size_gibibytes.*
        :param pulumi.Input[float] size_gibibytes: *Cannot be set alongside size_bytes or size_mebibytes.*
        :param pulumi.Input[float] size_kibibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[float] size_mebibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input['ComputeV1DiskSourceImageFamilyArgs'] source_image_family: *Cannot be set alongside source_image_id.*
        :param pulumi.Input[str] source_image_id: *Cannot be set alongside source_image_family.*
        """
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "type", type)
        if block_size_bytes is not None:
            pulumi.set(__self__, "block_size_bytes", block_size_bytes)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if placement_policy is not None:
            pulumi.set(__self__, "placement_policy", placement_policy)
        if size_bytes is not None:
            pulumi.set(__self__, "size_bytes", size_bytes)
        if size_gibibytes is not None:
            pulumi.set(__self__, "size_gibibytes", size_gibibytes)
        if size_kibibytes is not None:
            pulumi.set(__self__, "size_kibibytes", size_kibibytes)
        if size_mebibytes is not None:
            pulumi.set(__self__, "size_mebibytes", size_mebibytes)
        if source_image_family is not None:
            pulumi.set(__self__, "source_image_family", source_image_family)
        if source_image_id is not None:
            pulumi.set(__self__, "source_image_id", source_image_id)

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
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
        `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "block_size_bytes")

    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "block_size_bytes", value)

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
    def metadata(self) -> Optional[pulumi.Input['ComputeV1DiskMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['ComputeV1DiskMetadataArgs']]):
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
    @pulumi.getter(name="placementPolicy")
    def placement_policy(self) -> Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']]:
        return pulumi.get(self, "placement_policy")

    @placement_policy.setter
    def placement_policy(self, value: Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']]):
        pulumi.set(self, "placement_policy", value)

    @property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_kibibytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_bytes")

    @size_bytes.setter
    def size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_bytes", value)

    @property
    @pulumi.getter(name="sizeGibibytes")
    def size_gibibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_mebibytes.*
        """
        return pulumi.get(self, "size_gibibytes")

    @size_gibibytes.setter
    def size_gibibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_gibibytes", value)

    @property
    @pulumi.getter(name="sizeKibibytes")
    def size_kibibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_kibibytes")

    @size_kibibytes.setter
    def size_kibibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_kibibytes", value)

    @property
    @pulumi.getter(name="sizeMebibytes")
    def size_mebibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_mebibytes")

    @size_mebibytes.setter
    def size_mebibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_mebibytes", value)

    @property
    @pulumi.getter(name="sourceImageFamily")
    def source_image_family(self) -> Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']]:
        """
        *Cannot be set alongside source_image_id.*
        """
        return pulumi.get(self, "source_image_family")

    @source_image_family.setter
    def source_image_family(self, value: Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']]):
        pulumi.set(self, "source_image_family", value)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> Optional[pulumi.Input[str]]:
        """
        *Cannot be set alongside source_image_family.*
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image_id", value)


@pulumi.input_type
class _ComputeV1DiskState:
    def __init__(__self__, *,
                 block_size_bytes: Optional[pulumi.Input[float]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['ComputeV1DiskMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 placement_policy: Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 size_bytes: Optional[pulumi.Input[float]] = None,
                 size_gibibytes: Optional[pulumi.Input[float]] = None,
                 size_kibibytes: Optional[pulumi.Input[float]] = None,
                 size_mebibytes: Optional[pulumi.Input[float]] = None,
                 source_image_family: Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['ComputeV1DiskStatusArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComputeV1Disk resources.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['ComputeV1DiskMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[float] size_bytes: *Cannot be set alongside size_kibibytes or size_gibibytes.*
        :param pulumi.Input[float] size_gibibytes: *Cannot be set alongside size_bytes or size_mebibytes.*
        :param pulumi.Input[float] size_kibibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[float] size_mebibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input['ComputeV1DiskSourceImageFamilyArgs'] source_image_family: *Cannot be set alongside source_image_id.*
        :param pulumi.Input[str] source_image_id: *Cannot be set alongside source_image_family.*
        :param pulumi.Input[str] type: ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
               `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if block_size_bytes is not None:
            pulumi.set(__self__, "block_size_bytes", block_size_bytes)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if placement_policy is not None:
            pulumi.set(__self__, "placement_policy", placement_policy)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if size_bytes is not None:
            pulumi.set(__self__, "size_bytes", size_bytes)
        if size_gibibytes is not None:
            pulumi.set(__self__, "size_gibibytes", size_gibibytes)
        if size_kibibytes is not None:
            pulumi.set(__self__, "size_kibibytes", size_kibibytes)
        if size_mebibytes is not None:
            pulumi.set(__self__, "size_mebibytes", size_mebibytes)
        if source_image_family is not None:
            pulumi.set(__self__, "source_image_family", source_image_family)
        if source_image_id is not None:
            pulumi.set(__self__, "source_image_id", source_image_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "block_size_bytes")

    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "block_size_bytes", value)

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
    def metadata(self) -> Optional[pulumi.Input['ComputeV1DiskMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['ComputeV1DiskMetadataArgs']]):
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
    @pulumi.getter(name="placementPolicy")
    def placement_policy(self) -> Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']]:
        return pulumi.get(self, "placement_policy")

    @placement_policy.setter
    def placement_policy(self, value: Optional[pulumi.Input['ComputeV1DiskPlacementPolicyArgs']]):
        pulumi.set(self, "placement_policy", value)

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
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_kibibytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_bytes")

    @size_bytes.setter
    def size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_bytes", value)

    @property
    @pulumi.getter(name="sizeGibibytes")
    def size_gibibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_mebibytes.*
        """
        return pulumi.get(self, "size_gibibytes")

    @size_gibibytes.setter
    def size_gibibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_gibibytes", value)

    @property
    @pulumi.getter(name="sizeKibibytes")
    def size_kibibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_kibibytes")

    @size_kibibytes.setter
    def size_kibibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_kibibytes", value)

    @property
    @pulumi.getter(name="sizeMebibytes")
    def size_mebibytes(self) -> Optional[pulumi.Input[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_mebibytes")

    @size_mebibytes.setter
    def size_mebibytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size_mebibytes", value)

    @property
    @pulumi.getter(name="sourceImageFamily")
    def source_image_family(self) -> Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']]:
        """
        *Cannot be set alongside source_image_id.*
        """
        return pulumi.get(self, "source_image_family")

    @source_image_family.setter
    def source_image_family(self, value: Optional[pulumi.Input['ComputeV1DiskSourceImageFamilyArgs']]):
        pulumi.set(self, "source_image_family", value)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> Optional[pulumi.Input[str]]:
        """
        *Cannot be set alongside source_image_family.*
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['ComputeV1DiskStatusArgs']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['ComputeV1DiskStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
        `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

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


class ComputeV1Disk(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size_bytes: Optional[pulumi.Input[float]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['ComputeV1DiskMetadataArgs', 'ComputeV1DiskMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 placement_policy: Optional[pulumi.Input[Union['ComputeV1DiskPlacementPolicyArgs', 'ComputeV1DiskPlacementPolicyArgsDict']]] = None,
                 size_bytes: Optional[pulumi.Input[float]] = None,
                 size_gibibytes: Optional[pulumi.Input[float]] = None,
                 size_kibibytes: Optional[pulumi.Input[float]] = None,
                 size_mebibytes: Optional[pulumi.Input[float]] = None,
                 source_image_family: Optional[pulumi.Input[Union['ComputeV1DiskSourceImageFamilyArgs', 'ComputeV1DiskSourceImageFamilyArgsDict']]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ComputeV1Disk resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['ComputeV1DiskMetadataArgs', 'ComputeV1DiskMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] size_bytes: *Cannot be set alongside size_kibibytes or size_gibibytes.*
        :param pulumi.Input[float] size_gibibytes: *Cannot be set alongside size_bytes or size_mebibytes.*
        :param pulumi.Input[float] size_kibibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[float] size_mebibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[Union['ComputeV1DiskSourceImageFamilyArgs', 'ComputeV1DiskSourceImageFamilyArgsDict']] source_image_family: *Cannot be set alongside source_image_id.*
        :param pulumi.Input[str] source_image_id: *Cannot be set alongside source_image_family.*
        :param pulumi.Input[str] type: ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
               `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputeV1DiskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ComputeV1Disk resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComputeV1DiskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputeV1DiskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size_bytes: Optional[pulumi.Input[float]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['ComputeV1DiskMetadataArgs', 'ComputeV1DiskMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 placement_policy: Optional[pulumi.Input[Union['ComputeV1DiskPlacementPolicyArgs', 'ComputeV1DiskPlacementPolicyArgsDict']]] = None,
                 size_bytes: Optional[pulumi.Input[float]] = None,
                 size_gibibytes: Optional[pulumi.Input[float]] = None,
                 size_kibibytes: Optional[pulumi.Input[float]] = None,
                 size_mebibytes: Optional[pulumi.Input[float]] = None,
                 source_image_family: Optional[pulumi.Input[Union['ComputeV1DiskSourceImageFamilyArgs', 'ComputeV1DiskSourceImageFamilyArgsDict']]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComputeV1DiskArgs.__new__(ComputeV1DiskArgs)

            __props__.__dict__["block_size_bytes"] = block_size_bytes
            __props__.__dict__["labels"] = labels
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["placement_policy"] = placement_policy
            __props__.__dict__["size_bytes"] = size_bytes
            __props__.__dict__["size_gibibytes"] = size_gibibytes
            __props__.__dict__["size_kibibytes"] = size_kibibytes
            __props__.__dict__["size_mebibytes"] = size_mebibytes
            __props__.__dict__["source_image_family"] = source_image_family
            __props__.__dict__["source_image_id"] = source_image_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["created_at"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        super(ComputeV1Disk, __self__).__init__(
            'nebius:index/computeV1Disk:ComputeV1Disk',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            block_size_bytes: Optional[pulumi.Input[float]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            metadata: Optional[pulumi.Input[Union['ComputeV1DiskMetadataArgs', 'ComputeV1DiskMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            placement_policy: Optional[pulumi.Input[Union['ComputeV1DiskPlacementPolicyArgs', 'ComputeV1DiskPlacementPolicyArgsDict']]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            size_bytes: Optional[pulumi.Input[float]] = None,
            size_gibibytes: Optional[pulumi.Input[float]] = None,
            size_kibibytes: Optional[pulumi.Input[float]] = None,
            size_mebibytes: Optional[pulumi.Input[float]] = None,
            source_image_family: Optional[pulumi.Input[Union['ComputeV1DiskSourceImageFamilyArgs', 'ComputeV1DiskSourceImageFamilyArgsDict']]] = None,
            source_image_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[Union['ComputeV1DiskStatusArgs', 'ComputeV1DiskStatusArgsDict']]] = None,
            type: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'ComputeV1Disk':
        """
        Get an existing ComputeV1Disk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['ComputeV1DiskMetadataArgs', 'ComputeV1DiskMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[float] size_bytes: *Cannot be set alongside size_kibibytes or size_gibibytes.*
        :param pulumi.Input[float] size_gibibytes: *Cannot be set alongside size_bytes or size_mebibytes.*
        :param pulumi.Input[float] size_kibibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[float] size_mebibytes: *Cannot be set alongside size_bytes or size_gibibytes.*
        :param pulumi.Input[Union['ComputeV1DiskSourceImageFamilyArgs', 'ComputeV1DiskSourceImageFamilyArgsDict']] source_image_family: *Cannot be set alongside source_image_id.*
        :param pulumi.Input[str] source_image_id: *Cannot be set alongside source_image_family.*
        :param pulumi.Input[str] type: ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
               `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComputeV1DiskState.__new__(_ComputeV1DiskState)

        __props__.__dict__["block_size_bytes"] = block_size_bytes
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["labels"] = labels
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["placement_policy"] = placement_policy
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["size_bytes"] = size_bytes
        __props__.__dict__["size_gibibytes"] = size_gibibytes
        __props__.__dict__["size_kibibytes"] = size_kibibytes
        __props__.__dict__["size_mebibytes"] = size_mebibytes
        __props__.__dict__["source_image_family"] = source_image_family
        __props__.__dict__["source_image_id"] = source_image_id
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        __props__.__dict__["updated_at"] = updated_at
        return ComputeV1Disk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "block_size_bytes")

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
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.ComputeV1DiskMetadata']:
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
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(self) -> pulumi.Output[Optional['outputs.ComputeV1DiskPlacementPolicy']]:
        return pulumi.get(self, "placement_policy")

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
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> pulumi.Output[Optional[float]]:
        """
        *Cannot be set alongside size_kibibytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_bytes")

    @property
    @pulumi.getter(name="sizeGibibytes")
    def size_gibibytes(self) -> pulumi.Output[Optional[float]]:
        """
        *Cannot be set alongside size_bytes or size_mebibytes.*
        """
        return pulumi.get(self, "size_gibibytes")

    @property
    @pulumi.getter(name="sizeKibibytes")
    def size_kibibytes(self) -> pulumi.Output[Optional[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_kibibytes")

    @property
    @pulumi.getter(name="sizeMebibytes")
    def size_mebibytes(self) -> pulumi.Output[Optional[float]]:
        """
        *Cannot be set alongside size_bytes or size_gibibytes.*
        """
        return pulumi.get(self, "size_mebibytes")

    @property
    @pulumi.getter(name="sourceImageFamily")
    def source_image_family(self) -> pulumi.Output[Optional['outputs.ComputeV1DiskSourceImageFamily']]:
        """
        *Cannot be set alongside source_image_id.*
        """
        return pulumi.get(self, "source_image_family")

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> pulumi.Output[Optional[str]]:
        """
        *Cannot be set alongside source_image_family.*
        """
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.ComputeV1DiskStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        ### Supported values the list of available types will be clarified later, it is not final version Possible values: -
        `UNSPECIFIED` - `NETWORK_SSD` - `NETWORK_HDD` - `NETWORK_SSD_NON_REPLICATED` - `NETWORK_SSD_IO_M3`
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

