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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.enterpriseknowledgegraph_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object]  # type: ignore

from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore

from google.cloud.enterpriseknowledgegraph_v1.services.enterprise_knowledge_graph_service import (
    pagers,
)
from google.cloud.enterpriseknowledgegraph_v1.types import job_state, service

from .client import EnterpriseKnowledgeGraphServiceClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    EnterpriseKnowledgeGraphServiceTransport,
)
from .transports.grpc_asyncio import EnterpriseKnowledgeGraphServiceGrpcAsyncIOTransport


class EnterpriseKnowledgeGraphServiceAsyncClient:
    """APIs for enterprise knowledge graph product."""

    _client: EnterpriseKnowledgeGraphServiceClient

    DEFAULT_ENDPOINT = EnterpriseKnowledgeGraphServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EnterpriseKnowledgeGraphServiceClient.DEFAULT_MTLS_ENDPOINT

    cloud_knowledge_graph_entity_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.cloud_knowledge_graph_entity_path
    )
    parse_cloud_knowledge_graph_entity_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_cloud_knowledge_graph_entity_path
    )
    dataset_path = staticmethod(EnterpriseKnowledgeGraphServiceClient.dataset_path)
    parse_dataset_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_dataset_path
    )
    entity_reconciliation_job_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.entity_reconciliation_job_path
    )
    parse_entity_reconciliation_job_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_entity_reconciliation_job_path
    )
    public_knowledge_graph_entity_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.public_knowledge_graph_entity_path
    )
    parse_public_knowledge_graph_entity_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_public_knowledge_graph_entity_path
    )
    table_path = staticmethod(EnterpriseKnowledgeGraphServiceClient.table_path)
    parse_table_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_table_path
    )
    common_billing_account_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        EnterpriseKnowledgeGraphServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EnterpriseKnowledgeGraphServiceAsyncClient: The constructed client.
        """
        return EnterpriseKnowledgeGraphServiceClient.from_service_account_info.__func__(EnterpriseKnowledgeGraphServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EnterpriseKnowledgeGraphServiceAsyncClient: The constructed client.
        """
        return EnterpriseKnowledgeGraphServiceClient.from_service_account_file.__func__(EnterpriseKnowledgeGraphServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return EnterpriseKnowledgeGraphServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EnterpriseKnowledgeGraphServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            EnterpriseKnowledgeGraphServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(EnterpriseKnowledgeGraphServiceClient).get_transport_class,
        type(EnterpriseKnowledgeGraphServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[
            str, EnterpriseKnowledgeGraphServiceTransport
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the enterprise knowledge graph service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.EnterpriseKnowledgeGraphServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = EnterpriseKnowledgeGraphServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_entity_reconciliation_job(
        self,
        request: Optional[
            Union[service.CreateEntityReconciliationJobRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        entity_reconciliation_job: Optional[service.EntityReconciliationJob] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.EntityReconciliationJob:
        r"""Creates a EntityReconciliationJob. A
        EntityReconciliationJob once created will right away be
        attempted to start.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_create_entity_reconciliation_job():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.CreateEntityReconciliationJobRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_entity_reconciliation_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.CreateEntityReconciliationJobRequest, dict]]):
                The request object. Request message for
                CreateEntityReconciliationJob.
            parent (:class:`str`):
                Required. The resource name of the Location to create
                the EntityReconciliationJob in. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_reconciliation_job (:class:`google.cloud.enterpriseknowledgegraph_v1.types.EntityReconciliationJob`):
                Required. The EntityReconciliationJob
                to create.

                This corresponds to the ``entity_reconciliation_job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.EntityReconciliationJob:
                Entity reconciliation job message.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entity_reconciliation_job])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateEntityReconciliationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if entity_reconciliation_job is not None:
            request.entity_reconciliation_job = entity_reconciliation_job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_entity_reconciliation_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_entity_reconciliation_job(
        self,
        request: Optional[
            Union[service.GetEntityReconciliationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.EntityReconciliationJob:
        r"""Gets a EntityReconciliationJob.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_get_entity_reconciliation_job():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.GetEntityReconciliationJobRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_entity_reconciliation_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.GetEntityReconciliationJobRequest, dict]]):
                The request object. Request message for
                GetEntityReconciliationJob.
            name (:class:`str`):
                Required. The name of the EntityReconciliationJob
                resource. Format:
                ``projects/{project}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.EntityReconciliationJob:
                Entity reconciliation job message.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetEntityReconciliationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_entity_reconciliation_job,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_entity_reconciliation_jobs(
        self,
        request: Optional[
            Union[service.ListEntityReconciliationJobsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntityReconciliationJobsAsyncPager:
        r"""Lists Entity Reconciliation Jobs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_list_entity_reconciliation_jobs():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.ListEntityReconciliationJobsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entity_reconciliation_jobs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.ListEntityReconciliationJobsRequest, dict]]):
                The request object. Request message for
                [EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs].
            parent (:class:`str`):
                Required. The name of the EntityReconciliationJob's
                parent resource. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.services.enterprise_knowledge_graph_service.pagers.ListEntityReconciliationJobsAsyncPager:
                Response message for
                   [EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListEntityReconciliationJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_entity_reconciliation_jobs,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEntityReconciliationJobsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def cancel_entity_reconciliation_job(
        self,
        request: Optional[
            Union[service.CancelEntityReconciliationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Cancels a EntityReconciliationJob. Success of
        cancellation is not guaranteed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_cancel_entity_reconciliation_job():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.CancelEntityReconciliationJobRequest(
                    name="name_value",
                )

                # Make the request
                await client.cancel_entity_reconciliation_job(request=request)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.CancelEntityReconciliationJobRequest, dict]]):
                The request object. Request message for
                CancelEntityReconciliationJob.
            name (:class:`str`):
                Required. The name of the EntityReconciliationJob
                resource. Format:
                ``projects/{project}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CancelEntityReconciliationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.cancel_entity_reconciliation_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_entity_reconciliation_job(
        self,
        request: Optional[
            Union[service.DeleteEntityReconciliationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a EntityReconciliationJob.
        It only deletes the job when the job state is in FAILED,
        SUCCEEDED, and CANCELLED.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_delete_entity_reconciliation_job():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.DeleteEntityReconciliationJobRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_entity_reconciliation_job(request=request)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.DeleteEntityReconciliationJobRequest, dict]]):
                The request object. Request message for
                DeleteEntityReconciliationJob.
            name (:class:`str`):
                Required. The name of the EntityReconciliationJob
                resource. Format:
                ``projects/{project}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DeleteEntityReconciliationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_entity_reconciliation_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def lookup(
        self,
        request: Optional[Union[service.LookupRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        ids: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.LookupResponse:
        r"""Finds the Cloud KG entities with CKG ID(s).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_lookup():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.LookupRequest(
                    parent="parent_value",
                    ids=['ids_value1', 'ids_value2'],
                )

                # Make the request
                response = await client.lookup(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.LookupRequest, dict]]):
                The request object. Request message for
                [EnterpriseKnowledgeGraphService.Lookup][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup].
            parent (:class:`str`):
                Required. The name of the Entity's parent resource.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ids (:class:`MutableSequence[str]`):
                Required. The list of entity ids to
                be used for lookup.

                This corresponds to the ``ids`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.LookupResponse:
                Response message for
                   [EnterpriseKnowledgeGraphService.Lookup][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, ids])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.LookupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if ids:
            request.ids.extend(ids)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.lookup,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search(
        self,
        request: Optional[Union[service.SearchRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        query: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.SearchResponse:
        r"""Searches the Cloud KG entities with entity name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_search():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.SearchRequest(
                    parent="parent_value",
                    query="query_value",
                )

                # Make the request
                response = await client.search(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.SearchRequest, dict]]):
                The request object. Request message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].
            parent (:class:`str`):
                Required. The name of the Entity's parent resource.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Required. The literal query string
                for search.

                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.SearchResponse:
                Response message for
                   [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, query])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.SearchRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def lookup_public_kg(
        self,
        request: Optional[Union[service.LookupPublicKgRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        ids: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.LookupPublicKgResponse:
        r"""Finds the public KG entities with public KG ID(s).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_lookup_public_kg():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.LookupPublicKgRequest(
                    parent="parent_value",
                    ids=['ids_value1', 'ids_value2'],
                )

                # Make the request
                response = await client.lookup_public_kg(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.LookupPublicKgRequest, dict]]):
                The request object. Request message for
                [EnterpriseKnowledgeGraphService.LookupPublicKg][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg].
            parent (:class:`str`):
                Required. The name of the Entity's parent resource.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ids (:class:`MutableSequence[str]`):
                Required. The list of entity ids to
                be used for lookup.

                This corresponds to the ``ids`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.LookupPublicKgResponse:
                Response message for
                   [EnterpriseKnowledgeGraphService.LookupPublicKg][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, ids])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.LookupPublicKgRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if ids:
            request.ids.extend(ids)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.lookup_public_kg,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_public_kg(
        self,
        request: Optional[Union[service.SearchPublicKgRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        query: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.SearchPublicKgResponse:
        r"""Searches the public KG entities with entity name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import enterpriseknowledgegraph_v1

            async def sample_search_public_kg():
                # Create a client
                client = enterpriseknowledgegraph_v1.EnterpriseKnowledgeGraphServiceAsyncClient()

                # Initialize request argument(s)
                request = enterpriseknowledgegraph_v1.SearchPublicKgRequest(
                    parent="parent_value",
                    query="query_value",
                )

                # Make the request
                response = await client.search_public_kg(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.enterpriseknowledgegraph_v1.types.SearchPublicKgRequest, dict]]):
                The request object. Request message for
                [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].
            parent (:class:`str`):
                Required. The name of the Entity's parent resource.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Required. The literal query string
                for search.

                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.enterpriseknowledgegraph_v1.types.SearchPublicKgResponse:
                Response message for
                   [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, query])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.SearchPublicKgRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_public_kg,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "EnterpriseKnowledgeGraphServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("EnterpriseKnowledgeGraphServiceAsyncClient",)
