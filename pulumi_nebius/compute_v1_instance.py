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

__all__ = ['ComputeV1InstanceArgs', 'ComputeV1Instance']

@pulumi.input_type
class ComputeV1InstanceArgs:
    def __init__(__self__, *,
                 network_interfaces: pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]],
                 parent_id: pulumi.Input[str],
                 resources: pulumi.Input['ComputeV1InstanceResourcesArgs'],
                 boot_disk: Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']] = None,
                 cloud_init_user_data: Optional[pulumi.Input[str]] = None,
                 filesystems: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]] = None,
                 gpu_cluster: Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recovery_policy: Optional[pulumi.Input[str]] = None,
                 secondary_disks: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 stopped: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ComputeV1Instance resource.
        :param pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]] network_interfaces: ### Inner value description Describes the specification of a network interface.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['ComputeV1InstanceMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[str] recovery_policy: ### Supported values Possible values: - `RECOVER` - `FAIL`
        """
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "resources", resources)
        if boot_disk is not None:
            pulumi.set(__self__, "boot_disk", boot_disk)
        if cloud_init_user_data is not None:
            pulumi.set(__self__, "cloud_init_user_data", cloud_init_user_data)
        if filesystems is not None:
            pulumi.set(__self__, "filesystems", filesystems)
        if gpu_cluster is not None:
            pulumi.set(__self__, "gpu_cluster", gpu_cluster)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if recovery_policy is not None:
            pulumi.set(__self__, "recovery_policy", recovery_policy)
        if secondary_disks is not None:
            pulumi.set(__self__, "secondary_disks", secondary_disks)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if stopped is not None:
            pulumi.set(__self__, "stopped", stopped)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]]:
        """
        ### Inner value description Describes the specification of a network interface.
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]]):
        pulumi.set(self, "network_interfaces", value)

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
    def resources(self) -> pulumi.Input['ComputeV1InstanceResourcesArgs']:
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: pulumi.Input['ComputeV1InstanceResourcesArgs']):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']]:
        return pulumi.get(self, "boot_disk")

    @boot_disk.setter
    def boot_disk(self, value: Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']]):
        pulumi.set(self, "boot_disk", value)

    @property
    @pulumi.getter(name="cloudInitUserData")
    def cloud_init_user_data(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cloud_init_user_data")

    @cloud_init_user_data.setter
    def cloud_init_user_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_init_user_data", value)

    @property
    @pulumi.getter
    def filesystems(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]]:
        return pulumi.get(self, "filesystems")

    @filesystems.setter
    def filesystems(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]]):
        pulumi.set(self, "filesystems", value)

    @property
    @pulumi.getter(name="gpuCluster")
    def gpu_cluster(self) -> Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']]:
        return pulumi.get(self, "gpu_cluster")

    @gpu_cluster.setter
    def gpu_cluster(self, value: Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']]):
        pulumi.set(self, "gpu_cluster", value)

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
    def metadata(self) -> Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']]):
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
    @pulumi.getter(name="recoveryPolicy")
    def recovery_policy(self) -> Optional[pulumi.Input[str]]:
        """
        ### Supported values Possible values: - `RECOVER` - `FAIL`
        """
        return pulumi.get(self, "recovery_policy")

    @recovery_policy.setter
    def recovery_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_policy", value)

    @property
    @pulumi.getter(name="secondaryDisks")
    def secondary_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]]:
        return pulumi.get(self, "secondary_disks")

    @secondary_disks.setter
    def secondary_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]]):
        pulumi.set(self, "secondary_disks", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def stopped(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "stopped")

    @stopped.setter
    def stopped(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "stopped", value)


@pulumi.input_type
class _ComputeV1InstanceState:
    def __init__(__self__, *,
                 boot_disk: Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']] = None,
                 cloud_init_user_data: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 filesystems: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]] = None,
                 gpu_cluster: Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 recovery_policy: Optional[pulumi.Input[str]] = None,
                 resource_version: Optional[pulumi.Input[float]] = None,
                 resources: Optional[pulumi.Input['ComputeV1InstanceResourcesArgs']] = None,
                 secondary_disks: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['ComputeV1InstanceStatusArgs']] = None,
                 stopped: Optional[pulumi.Input[bool]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComputeV1Instance resources.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input['ComputeV1InstanceMetadataArgs'] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]] network_interfaces: ### Inner value description Describes the specification of a network interface.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] recovery_policy: ### Supported values Possible values: - `RECOVER` - `FAIL`
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        if boot_disk is not None:
            pulumi.set(__self__, "boot_disk", boot_disk)
        if cloud_init_user_data is not None:
            pulumi.set(__self__, "cloud_init_user_data", cloud_init_user_data)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if filesystems is not None:
            pulumi.set(__self__, "filesystems", filesystems)
        if gpu_cluster is not None:
            pulumi.set(__self__, "gpu_cluster", gpu_cluster)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if recovery_policy is not None:
            pulumi.set(__self__, "recovery_policy", recovery_policy)
        if resource_version is not None:
            pulumi.set(__self__, "resource_version", resource_version)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if secondary_disks is not None:
            pulumi.set(__self__, "secondary_disks", secondary_disks)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if stopped is not None:
            pulumi.set(__self__, "stopped", stopped)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']]:
        return pulumi.get(self, "boot_disk")

    @boot_disk.setter
    def boot_disk(self, value: Optional[pulumi.Input['ComputeV1InstanceBootDiskArgs']]):
        pulumi.set(self, "boot_disk", value)

    @property
    @pulumi.getter(name="cloudInitUserData")
    def cloud_init_user_data(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cloud_init_user_data")

    @cloud_init_user_data.setter
    def cloud_init_user_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_init_user_data", value)

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
    def filesystems(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]]:
        return pulumi.get(self, "filesystems")

    @filesystems.setter
    def filesystems(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceFilesystemArgs']]]]):
        pulumi.set(self, "filesystems", value)

    @property
    @pulumi.getter(name="gpuCluster")
    def gpu_cluster(self) -> Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']]:
        return pulumi.get(self, "gpu_cluster")

    @gpu_cluster.setter
    def gpu_cluster(self, value: Optional[pulumi.Input['ComputeV1InstanceGpuClusterArgs']]):
        pulumi.set(self, "gpu_cluster", value)

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
    def metadata(self) -> Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']]:
        """
        ### Inner value description Common resource metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['ComputeV1InstanceMetadataArgs']]):
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]]]:
        """
        ### Inner value description Describes the specification of a network interface.
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

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
    @pulumi.getter(name="recoveryPolicy")
    def recovery_policy(self) -> Optional[pulumi.Input[str]]:
        """
        ### Supported values Possible values: - `RECOVER` - `FAIL`
        """
        return pulumi.get(self, "recovery_policy")

    @recovery_policy.setter
    def recovery_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_policy", value)

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
    def resources(self) -> Optional[pulumi.Input['ComputeV1InstanceResourcesArgs']]:
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input['ComputeV1InstanceResourcesArgs']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="secondaryDisks")
    def secondary_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]]:
        return pulumi.get(self, "secondary_disks")

    @secondary_disks.setter
    def secondary_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComputeV1InstanceSecondaryDiskArgs']]]]):
        pulumi.set(self, "secondary_disks", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['ComputeV1InstanceStatusArgs']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['ComputeV1InstanceStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def stopped(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "stopped")

    @stopped.setter
    def stopped(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "stopped", value)

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


class ComputeV1Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_disk: Optional[pulumi.Input[Union['ComputeV1InstanceBootDiskArgs', 'ComputeV1InstanceBootDiskArgsDict']]] = None,
                 cloud_init_user_data: Optional[pulumi.Input[str]] = None,
                 filesystems: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceFilesystemArgs', 'ComputeV1InstanceFilesystemArgsDict']]]]] = None,
                 gpu_cluster: Optional[pulumi.Input[Union['ComputeV1InstanceGpuClusterArgs', 'ComputeV1InstanceGpuClusterArgsDict']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['ComputeV1InstanceMetadataArgs', 'ComputeV1InstanceMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceNetworkInterfaceArgs', 'ComputeV1InstanceNetworkInterfaceArgsDict']]]]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 recovery_policy: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Union['ComputeV1InstanceResourcesArgs', 'ComputeV1InstanceResourcesArgsDict']]] = None,
                 secondary_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceSecondaryDiskArgs', 'ComputeV1InstanceSecondaryDiskArgsDict']]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 stopped: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a ComputeV1Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['ComputeV1InstanceMetadataArgs', 'ComputeV1InstanceMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceNetworkInterfaceArgs', 'ComputeV1InstanceNetworkInterfaceArgsDict']]]] network_interfaces: ### Inner value description Describes the specification of a network interface.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] recovery_policy: ### Supported values Possible values: - `RECOVER` - `FAIL`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputeV1InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ComputeV1Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComputeV1InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputeV1InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_disk: Optional[pulumi.Input[Union['ComputeV1InstanceBootDiskArgs', 'ComputeV1InstanceBootDiskArgsDict']]] = None,
                 cloud_init_user_data: Optional[pulumi.Input[str]] = None,
                 filesystems: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceFilesystemArgs', 'ComputeV1InstanceFilesystemArgsDict']]]]] = None,
                 gpu_cluster: Optional[pulumi.Input[Union['ComputeV1InstanceGpuClusterArgs', 'ComputeV1InstanceGpuClusterArgsDict']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metadata: Optional[pulumi.Input[Union['ComputeV1InstanceMetadataArgs', 'ComputeV1InstanceMetadataArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceNetworkInterfaceArgs', 'ComputeV1InstanceNetworkInterfaceArgsDict']]]]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 recovery_policy: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Union['ComputeV1InstanceResourcesArgs', 'ComputeV1InstanceResourcesArgsDict']]] = None,
                 secondary_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceSecondaryDiskArgs', 'ComputeV1InstanceSecondaryDiskArgsDict']]]]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 stopped: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComputeV1InstanceArgs.__new__(ComputeV1InstanceArgs)

            __props__.__dict__["boot_disk"] = boot_disk
            __props__.__dict__["cloud_init_user_data"] = None if cloud_init_user_data is None else pulumi.Output.secret(cloud_init_user_data)
            __props__.__dict__["filesystems"] = filesystems
            __props__.__dict__["gpu_cluster"] = gpu_cluster
            __props__.__dict__["labels"] = labels
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if network_interfaces is None and not opts.urn:
                raise TypeError("Missing required property 'network_interfaces'")
            __props__.__dict__["network_interfaces"] = network_interfaces
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["recovery_policy"] = recovery_policy
            if resources is None and not opts.urn:
                raise TypeError("Missing required property 'resources'")
            __props__.__dict__["resources"] = resources
            __props__.__dict__["secondary_disks"] = secondary_disks
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["stopped"] = stopped
            __props__.__dict__["created_at"] = None
            __props__.__dict__["resource_version"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_at"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["cloudInitUserData"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ComputeV1Instance, __self__).__init__(
            'nebius:index/computeV1Instance:ComputeV1Instance',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            boot_disk: Optional[pulumi.Input[Union['ComputeV1InstanceBootDiskArgs', 'ComputeV1InstanceBootDiskArgsDict']]] = None,
            cloud_init_user_data: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            filesystems: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceFilesystemArgs', 'ComputeV1InstanceFilesystemArgsDict']]]]] = None,
            gpu_cluster: Optional[pulumi.Input[Union['ComputeV1InstanceGpuClusterArgs', 'ComputeV1InstanceGpuClusterArgsDict']]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            metadata: Optional[pulumi.Input[Union['ComputeV1InstanceMetadataArgs', 'ComputeV1InstanceMetadataArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceNetworkInterfaceArgs', 'ComputeV1InstanceNetworkInterfaceArgsDict']]]]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            recovery_policy: Optional[pulumi.Input[str]] = None,
            resource_version: Optional[pulumi.Input[float]] = None,
            resources: Optional[pulumi.Input[Union['ComputeV1InstanceResourcesArgs', 'ComputeV1InstanceResourcesArgsDict']]] = None,
            secondary_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceSecondaryDiskArgs', 'ComputeV1InstanceSecondaryDiskArgsDict']]]]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[Union['ComputeV1InstanceStatusArgs', 'ComputeV1InstanceStatusArgsDict']]] = None,
            stopped: Optional[pulumi.Input[bool]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'ComputeV1Instance':
        """
        Get an existing ComputeV1Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Timestamp indicating when the resource was created. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels associated with the resource.
        :param pulumi.Input[Union['ComputeV1InstanceMetadataArgs', 'ComputeV1InstanceMetadataArgsDict']] metadata: ### Inner value description Common resource metadata.
        :param pulumi.Input[str] name: Human readable name for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ComputeV1InstanceNetworkInterfaceArgs', 'ComputeV1InstanceNetworkInterfaceArgsDict']]]] network_interfaces: ### Inner value description Describes the specification of a network interface.
        :param pulumi.Input[str] parent_id: Identifier of the parent resource to which the resource belongs.
        :param pulumi.Input[str] recovery_policy: ### Supported values Possible values: - `RECOVER` - `FAIL`
        :param pulumi.Input[float] resource_version: Version of the resource for safe concurrent modifications and consistent reads. Positive and monotonically increases on
               each resource spec change (but *not* on each change of the resource's container(s) or status). Service allows zero value
               or current.
        :param pulumi.Input[str] updated_at: Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
               8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComputeV1InstanceState.__new__(_ComputeV1InstanceState)

        __props__.__dict__["boot_disk"] = boot_disk
        __props__.__dict__["cloud_init_user_data"] = cloud_init_user_data
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["filesystems"] = filesystems
        __props__.__dict__["gpu_cluster"] = gpu_cluster
        __props__.__dict__["labels"] = labels
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["network_interfaces"] = network_interfaces
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["recovery_policy"] = recovery_policy
        __props__.__dict__["resource_version"] = resource_version
        __props__.__dict__["resources"] = resources
        __props__.__dict__["secondary_disks"] = secondary_disks
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["status"] = status
        __props__.__dict__["stopped"] = stopped
        __props__.__dict__["updated_at"] = updated_at
        return ComputeV1Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> pulumi.Output[Optional['outputs.ComputeV1InstanceBootDisk']]:
        return pulumi.get(self, "boot_disk")

    @property
    @pulumi.getter(name="cloudInitUserData")
    def cloud_init_user_data(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cloud_init_user_data")

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
    def filesystems(self) -> pulumi.Output[Optional[Sequence['outputs.ComputeV1InstanceFilesystem']]]:
        return pulumi.get(self, "filesystems")

    @property
    @pulumi.getter(name="gpuCluster")
    def gpu_cluster(self) -> pulumi.Output[Optional['outputs.ComputeV1InstanceGpuCluster']]:
        return pulumi.get(self, "gpu_cluster")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels associated with the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.ComputeV1InstanceMetadata']:
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence['outputs.ComputeV1InstanceNetworkInterface']]:
        """
        ### Inner value description Describes the specification of a network interface.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Identifier of the parent resource to which the resource belongs.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="recoveryPolicy")
    def recovery_policy(self) -> pulumi.Output[Optional[str]]:
        """
        ### Supported values Possible values: - `RECOVER` - `FAIL`
        """
        return pulumi.get(self, "recovery_policy")

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
    def resources(self) -> pulumi.Output['outputs.ComputeV1InstanceResources']:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="secondaryDisks")
    def secondary_disks(self) -> pulumi.Output[Optional[Sequence['outputs.ComputeV1InstanceSecondaryDisk']]]:
        return pulumi.get(self, "secondary_disks")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.ComputeV1InstanceStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def stopped(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "stopped")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp indicating when the resource was last updated. A string representing a timestamp in [ISO
        8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS.SSS±HH:MM`
        """
        return pulumi.get(self, "updated_at")

