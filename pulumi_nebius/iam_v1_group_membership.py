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

__all__ = ['IamV1GroupMembershipArgs', 'IamV1GroupMembership']

@pulumi.input_type
class IamV1GroupMembershipArgs:
    def __init__(__self__, *,
                 parent_id: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IamV1GroupMembership resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[str] member_id: Member of the group. Can be tenant user account id or service account id.
        :param pulumi.Input['IamV1GroupMembershipMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        """
        pulumi.set(__self__, "parent_id", parent_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if member_id is not None:
            pulumi.set(__self__, "member_id", member_id)
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[str]]:
        """
        Member of the group. Can be tenant user account id or service account id.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_id", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']]):
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
class _IamV1GroupMembershipState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 status: Optional[pulumi.Input['IamV1GroupMembershipStatusArgs']] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IamV1GroupMembership resources.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[str] member_id: Member of the group. Can be tenant user account id or service account id.
        :param pulumi.Input['IamV1GroupMembershipMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if member_id is not None:
            pulumi.set(__self__, "member_id", member_id)
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[str]]:
        """
        Member of the group. Can be tenant user account id or service account id.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_id", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['IamV1GroupMembershipMetadataArgs']]):
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
    def status(self) -> Optional[pulumi.Input['IamV1GroupMembershipStatusArgs']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['IamV1GroupMembershipStatusArgs']]):
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


class IamV1GroupMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['IamV1GroupMembershipMetadataArgs', 'IamV1GroupMembershipMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a IamV1GroupMembership resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[str] member_id: Member of the group. Can be tenant user account id or service account id.
        :param pulumi.Input[Union['IamV1GroupMembershipMetadataArgs', 'IamV1GroupMembershipMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IamV1GroupMembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a IamV1GroupMembership resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IamV1GroupMembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamV1GroupMembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['IamV1GroupMembershipMetadataArgs', 'IamV1GroupMembershipMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IamV1GroupMembershipArgs.__new__(IamV1GroupMembershipArgs)

            __props__.__dict__["labels"] = labels
            __props__.__dict__["member_id"] = member_id
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        super(IamV1GroupMembership, __self__).__init__(
            'nebius:index/iamV1GroupMembership:IamV1GroupMembership',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            member_id: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Union['IamV1GroupMembershipMetadataArgs', 'IamV1GroupMembershipMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            status: Optional[pulumi.Input[Union['IamV1GroupMembershipStatusArgs', 'IamV1GroupMembershipStatusArgsDict']]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'IamV1GroupMembership':
        """
        Get an existing IamV1GroupMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[str] member_id: Member of the group. Can be tenant user account id or service account id.
        :param pulumi.Input[Union['IamV1GroupMembershipMetadataArgs', 'IamV1GroupMembershipMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IamV1GroupMembershipState.__new__(_IamV1GroupMembershipState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["labels"] = labels
        __props__.__dict__["member_id"] = member_id
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["status"] = status
        __props__.__dict__["updated_at"] = updated_at
        return IamV1GroupMembership(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[Optional[str]]:
        """
        Member of the group. Can be tenant user account id or service account id.
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.IamV1GroupMembershipMetadata']:
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
    def status(self) -> pulumi.Output['outputs.IamV1GroupMembershipStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

