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

__all__ = ['RegistryV1RegistryArgs', 'RegistryV1Registry']

@pulumi.input_type
class RegistryV1RegistryArgs:
    def __init__(__self__, *,
                 parent_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegistryV1Registry resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['RegistryV1RegistryMetadataArgs'] metadata: This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
               the end user and the system. ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        """
        pulumi.set(__self__, "parent_id", parent_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)

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
    def description(self) -> Optional[pulumi.Input[str]]:
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
    def metadata(self) -> Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']]:
        """
        This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
        the end user and the system. ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']]):
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
class _RegistryV1RegistryState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 images_count: Optional[pulumi.Input[float]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 status: Optional[pulumi.Input['RegistryV1RegistryStatusArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RegistryV1Registry resources.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[float] images_count: Registry.Type type = 2;
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['RegistryV1RegistryMetadataArgs'] metadata: This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
               the end user and the system. ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input['RegistryV1RegistryStatusArgs'] status: This is filled in by the server and reports the current state of the system.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if images_count is not None:
            pulumi.set(__self__, "images_count", images_count)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

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
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="imagesCount")
    def images_count(self) -> Optional[pulumi.Input[float]]:
        """
        Registry.Type type = 2;
        """
        return pulumi.get(self, "images_count")

    @images_count.setter
    def images_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "images_count", value)

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
    def metadata(self) -> Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']]:
        """
        This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
        the end user and the system. ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['RegistryV1RegistryMetadataArgs']]):
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
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['RegistryV1RegistryStatusArgs']]:
        """
        This is filled in by the server and reports the current state of the system.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['RegistryV1RegistryStatusArgs']]):
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


class RegistryV1Registry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['RegistryV1RegistryMetadataArgs', 'RegistryV1RegistryMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a RegistryV1Registry resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['RegistryV1RegistryMetadataArgs', 'RegistryV1RegistryMetadataArgsDict']] metadata: This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
               the end user and the system. ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistryV1RegistryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a RegistryV1Registry resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param RegistryV1RegistryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistryV1RegistryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['RegistryV1RegistryMetadataArgs', 'RegistryV1RegistryMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistryV1RegistryArgs.__new__(RegistryV1RegistryArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["images_count"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        super(RegistryV1Registry, __self__).__init__(
            'nebius:index/registryV1Registry:RegistryV1Registry',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            images_count: Optional[pulumi.Input[float]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            metadata: Optional[pulumi.Input[Union['RegistryV1RegistryMetadataArgs', 'RegistryV1RegistryMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            status: Optional[pulumi.Input[Union['RegistryV1RegistryStatusArgs', 'RegistryV1RegistryStatusArgsDict']]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'RegistryV1Registry':
        """
        Get an existing RegistryV1Registry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[float] images_count: Registry.Type type = 2;
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['RegistryV1RegistryMetadataArgs', 'RegistryV1RegistryMetadataArgsDict']] metadata: This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
               the end user and the system. ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[Union['RegistryV1RegistryStatusArgs', 'RegistryV1RegistryStatusArgsDict']] status: This is filled in by the server and reports the current state of the system.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegistryV1RegistryState.__new__(_RegistryV1RegistryState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["images_count"] = images_count
        __props__.__dict__["labels"] = labels
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["status"] = status
        __props__.__dict__["updated_at"] = updated_at
        return RegistryV1Registry(resource_name, opts=opts, __props__=__props__)

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
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="imagesCount")
    def images_count(self) -> pulumi.Output[float]:
        """
        Registry.Type type = 2;
        """
        return pulumi.get(self, "images_count")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.RegistryV1RegistryMetadata']:
        """
        This is metadata about the resource, such as its id, name, labels, etc. This contains fields that may be updated both by
        the end user and the system. ### Inner value description Common resource metadata.
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
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> pulumi.Output[float]:
        """
        Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
        each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
        or current.
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.RegistryV1RegistryStatus']:
        """
        This is filled in by the server and reports the current state of the system.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

