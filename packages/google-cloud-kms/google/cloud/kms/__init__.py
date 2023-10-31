# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.kms import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.kms_v1.services.ekm_service.async_client import EkmServiceAsyncClient
from google.cloud.kms_v1.services.ekm_service.client import EkmServiceClient
from google.cloud.kms_v1.services.key_management_service.async_client import (
    KeyManagementServiceAsyncClient,
)
from google.cloud.kms_v1.services.key_management_service.client import (
    KeyManagementServiceClient,
)
from google.cloud.kms_v1.types.ekm_service import (
    Certificate,
    CreateEkmConnectionRequest,
    EkmConfig,
    EkmConnection,
    GetEkmConfigRequest,
    GetEkmConnectionRequest,
    ListEkmConnectionsRequest,
    ListEkmConnectionsResponse,
    UpdateEkmConfigRequest,
    UpdateEkmConnectionRequest,
    VerifyConnectivityRequest,
    VerifyConnectivityResponse,
)
from google.cloud.kms_v1.types.resources import (
    CryptoKey,
    CryptoKeyVersion,
    CryptoKeyVersionTemplate,
    ExternalProtectionLevelOptions,
    ImportJob,
    KeyOperationAttestation,
    KeyRing,
    ProtectionLevel,
    PublicKey,
)
from google.cloud.kms_v1.types.service import (
    AsymmetricDecryptRequest,
    AsymmetricDecryptResponse,
    AsymmetricSignRequest,
    AsymmetricSignResponse,
    CreateCryptoKeyRequest,
    CreateCryptoKeyVersionRequest,
    CreateImportJobRequest,
    CreateKeyRingRequest,
    DecryptRequest,
    DecryptResponse,
    DestroyCryptoKeyVersionRequest,
    Digest,
    EncryptRequest,
    EncryptResponse,
    GenerateRandomBytesRequest,
    GenerateRandomBytesResponse,
    GetCryptoKeyRequest,
    GetCryptoKeyVersionRequest,
    GetImportJobRequest,
    GetKeyRingRequest,
    GetPublicKeyRequest,
    ImportCryptoKeyVersionRequest,
    ListCryptoKeysRequest,
    ListCryptoKeysResponse,
    ListCryptoKeyVersionsRequest,
    ListCryptoKeyVersionsResponse,
    ListImportJobsRequest,
    ListImportJobsResponse,
    ListKeyRingsRequest,
    ListKeyRingsResponse,
    LocationMetadata,
    MacSignRequest,
    MacSignResponse,
    MacVerifyRequest,
    MacVerifyResponse,
    RawDecryptRequest,
    RawDecryptResponse,
    RawEncryptRequest,
    RawEncryptResponse,
    RestoreCryptoKeyVersionRequest,
    UpdateCryptoKeyPrimaryVersionRequest,
    UpdateCryptoKeyRequest,
    UpdateCryptoKeyVersionRequest,
)

__all__ = (
    "EkmServiceClient",
    "EkmServiceAsyncClient",
    "KeyManagementServiceClient",
    "KeyManagementServiceAsyncClient",
    "Certificate",
    "CreateEkmConnectionRequest",
    "EkmConfig",
    "EkmConnection",
    "GetEkmConfigRequest",
    "GetEkmConnectionRequest",
    "ListEkmConnectionsRequest",
    "ListEkmConnectionsResponse",
    "UpdateEkmConfigRequest",
    "UpdateEkmConnectionRequest",
    "VerifyConnectivityRequest",
    "VerifyConnectivityResponse",
    "CryptoKey",
    "CryptoKeyVersion",
    "CryptoKeyVersionTemplate",
    "ExternalProtectionLevelOptions",
    "ImportJob",
    "KeyOperationAttestation",
    "KeyRing",
    "PublicKey",
    "ProtectionLevel",
    "AsymmetricDecryptRequest",
    "AsymmetricDecryptResponse",
    "AsymmetricSignRequest",
    "AsymmetricSignResponse",
    "CreateCryptoKeyRequest",
    "CreateCryptoKeyVersionRequest",
    "CreateImportJobRequest",
    "CreateKeyRingRequest",
    "DecryptRequest",
    "DecryptResponse",
    "DestroyCryptoKeyVersionRequest",
    "Digest",
    "EncryptRequest",
    "EncryptResponse",
    "GenerateRandomBytesRequest",
    "GenerateRandomBytesResponse",
    "GetCryptoKeyRequest",
    "GetCryptoKeyVersionRequest",
    "GetImportJobRequest",
    "GetKeyRingRequest",
    "GetPublicKeyRequest",
    "ImportCryptoKeyVersionRequest",
    "ListCryptoKeysRequest",
    "ListCryptoKeysResponse",
    "ListCryptoKeyVersionsRequest",
    "ListCryptoKeyVersionsResponse",
    "ListImportJobsRequest",
    "ListImportJobsResponse",
    "ListKeyRingsRequest",
    "ListKeyRingsResponse",
    "LocationMetadata",
    "MacSignRequest",
    "MacSignResponse",
    "MacVerifyRequest",
    "MacVerifyResponse",
    "RawDecryptRequest",
    "RawDecryptResponse",
    "RawEncryptRequest",
    "RawEncryptResponse",
    "RestoreCryptoKeyVersionRequest",
    "UpdateCryptoKeyPrimaryVersionRequest",
    "UpdateCryptoKeyRequest",
    "UpdateCryptoKeyVersionRequest",
)
