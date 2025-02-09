# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .applications_v1alpha1_k8s_release import *
from .compute_v1_disk import *
from .compute_v1_filesystem import *
from .compute_v1_gpu_cluster import *
from .compute_v1_instance import *
from .compute_v1alpha1_disk import *
from .compute_v1alpha1_filesystem import *
from .compute_v1alpha1_gpu_cluster import *
from .compute_v1alpha1_instance import *
from .get_applications_v1alpha1_k8s_release import *
from .get_compute_v1_disk import *
from .get_compute_v1_filesystem import *
from .get_compute_v1_gpu_cluster import *
from .get_compute_v1_image import *
from .get_compute_v1_instance import *
from .get_compute_v1alpha1_disk import *
from .get_compute_v1alpha1_filesystem import *
from .get_compute_v1alpha1_gpu_cluster import *
from .get_compute_v1alpha1_image import *
from .get_compute_v1alpha1_instance import *
from .get_iam_v1_auth_public_key import *
from .get_iam_v1_federation import *
from .get_iam_v1_federation_certificate import *
from .get_iam_v1_group import *
from .get_iam_v1_group_membership import *
from .get_iam_v1_invitation import *
from .get_iam_v1_project import *
from .get_iam_v1_service_account import *
from .get_iam_v1_tenant import *
from .get_iam_v1_tenant_user_account import *
from .get_mk8s_v1_cluster import *
from .get_mk8s_v1_node_group import *
from .get_mk8s_v1alpha1_cluster import *
from .get_mk8s_v1alpha1_node_group import *
from .get_msp_mlflow_v1alpha1_cluster import *
from .get_msp_postgresql_v1alpha1_cluster import *
from .get_msp_spark_v1alpha1_cluster import *
from .get_msp_spark_v1alpha1_session import *
from .get_registry_v1_registry import *
from .get_storage_v1_bucket import *
from .get_vpc_v1_allocation import *
from .get_vpc_v1_network import *
from .get_vpc_v1_pool import *
from .get_vpc_v1_subnet import *
from .get_vpc_v1alpha1_allocation import *
from .get_vpc_v1alpha1_network import *
from .get_vpc_v1alpha1_pool import *
from .get_vpc_v1alpha1_scope import *
from .get_vpc_v1alpha1_subnet import *
from .iam_v1_auth_public_key import *
from .iam_v1_federation import *
from .iam_v1_federation_certificate import *
from .iam_v1_group_membership import *
from .iam_v1_invitation import *
from .iam_v1_service_account import *
from .mk8s_v1_cluster import *
from .mk8s_v1_node_group import *
from .mk8s_v1alpha1_cluster import *
from .mk8s_v1alpha1_node_group import *
from .msp_mlflow_v1alpha1_cluster import *
from .msp_postgresql_v1alpha1_cluster import *
from .msp_spark_v1alpha1_cluster import *
from .msp_spark_v1alpha1_session import *
from .provider import *
from .registry_v1_registry import *
from .storage_v1_bucket import *
from .vpc_v1_allocation import *
from .vpc_v1alpha1_allocation import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_nebius.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_nebius.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "nebius",
  "mod": "index/applicationsV1alpha1K8sRelease",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/applicationsV1alpha1K8sRelease:ApplicationsV1alpha1K8sRelease": "ApplicationsV1alpha1K8sRelease"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1Disk",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1Disk:ComputeV1Disk": "ComputeV1Disk"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1Filesystem",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1Filesystem:ComputeV1Filesystem": "ComputeV1Filesystem"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1GpuCluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1GpuCluster:ComputeV1GpuCluster": "ComputeV1GpuCluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1Instance",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1Instance:ComputeV1Instance": "ComputeV1Instance"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1alpha1Disk",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1alpha1Disk:ComputeV1alpha1Disk": "ComputeV1alpha1Disk"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1alpha1Filesystem",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1alpha1Filesystem:ComputeV1alpha1Filesystem": "ComputeV1alpha1Filesystem"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1alpha1GpuCluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1alpha1GpuCluster:ComputeV1alpha1GpuCluster": "ComputeV1alpha1GpuCluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/computeV1alpha1Instance",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/computeV1alpha1Instance:ComputeV1alpha1Instance": "ComputeV1alpha1Instance"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1AuthPublicKey",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1AuthPublicKey:IamV1AuthPublicKey": "IamV1AuthPublicKey"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1Federation",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1Federation:IamV1Federation": "IamV1Federation"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1FederationCertificate",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1FederationCertificate:IamV1FederationCertificate": "IamV1FederationCertificate"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1GroupMembership",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1GroupMembership:IamV1GroupMembership": "IamV1GroupMembership"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1Invitation",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1Invitation:IamV1Invitation": "IamV1Invitation"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/iamV1ServiceAccount",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/iamV1ServiceAccount:IamV1ServiceAccount": "IamV1ServiceAccount"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mk8sV1Cluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mk8sV1Cluster:Mk8sV1Cluster": "Mk8sV1Cluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mk8sV1NodeGroup",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mk8sV1NodeGroup:Mk8sV1NodeGroup": "Mk8sV1NodeGroup"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mk8sV1alpha1Cluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mk8sV1alpha1Cluster:Mk8sV1alpha1Cluster": "Mk8sV1alpha1Cluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mk8sV1alpha1NodeGroup",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mk8sV1alpha1NodeGroup:Mk8sV1alpha1NodeGroup": "Mk8sV1alpha1NodeGroup"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mspMlflowV1alpha1Cluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mspMlflowV1alpha1Cluster:MspMlflowV1alpha1Cluster": "MspMlflowV1alpha1Cluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mspPostgresqlV1alpha1Cluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mspPostgresqlV1alpha1Cluster:MspPostgresqlV1alpha1Cluster": "MspPostgresqlV1alpha1Cluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mspSparkV1alpha1Cluster",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mspSparkV1alpha1Cluster:MspSparkV1alpha1Cluster": "MspSparkV1alpha1Cluster"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/mspSparkV1alpha1Session",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/mspSparkV1alpha1Session:MspSparkV1alpha1Session": "MspSparkV1alpha1Session"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/registryV1Registry",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/registryV1Registry:RegistryV1Registry": "RegistryV1Registry"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/storageV1Bucket",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/storageV1Bucket:StorageV1Bucket": "StorageV1Bucket"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/vpcV1Allocation",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/vpcV1Allocation:VpcV1Allocation": "VpcV1Allocation"
  }
 },
 {
  "pkg": "nebius",
  "mod": "index/vpcV1alpha1Allocation",
  "fqn": "pulumi_nebius",
  "classes": {
   "nebius:index/vpcV1alpha1Allocation:VpcV1alpha1Allocation": "VpcV1alpha1Allocation"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "nebius",
  "token": "pulumi:providers:nebius",
  "fqn": "pulumi_nebius",
  "class": "Provider"
 }
]
"""
)
