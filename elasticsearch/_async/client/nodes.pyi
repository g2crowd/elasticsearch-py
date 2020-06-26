# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class NodesClient(NamespacedClient):
    async def reload_secure_settings(
        self,
        body: Any = None,
        node_id: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def info(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def hot_threads(
        self,
        node_id: Optional[Any] = None,
        doc_type: Optional[Any] = None,
        ignore_idle_threads: Optional[Any] = None,
        interval: Optional[Any] = None,
        snapshots: Optional[Any] = None,
        threads: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def usage(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def stats(
        self,
        node_id: Optional[Any] = None,
        metric: Optional[Any] = None,
        index_metric: Optional[Any] = None,
        completion_fields: Optional[Any] = None,
        fielddata_fields: Optional[Any] = None,
        fields: Optional[Any] = None,
        groups: Optional[Any] = None,
        include_segment_file_sizes: Optional[Any] = None,
        level: Optional[Any] = None,
        timeout: Optional[Any] = None,
        types: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
