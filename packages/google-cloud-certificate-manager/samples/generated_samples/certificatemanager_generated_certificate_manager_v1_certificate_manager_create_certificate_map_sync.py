# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for CreateCertificateMap
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-certificate-manager


# [START certificatemanager_generated_certificate_manager_v1_CertificateManager_CreateCertificateMap_sync]
from google.cloud import certificate_manager_v1


def sample_create_certificate_map():
    # Create a client
    client = certificate_manager_v1.CertificateManagerClient()

    # Initialize request argument(s)
    request = certificate_manager_v1.CreateCertificateMapRequest(
        parent="parent_value",
        certificate_map_id="certificate_map_id_value",
    )

    # Make the request
    operation = client.create_certificate_map(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END certificatemanager_generated_certificate_manager_v1_CertificateManager_CreateCertificateMap_sync]
