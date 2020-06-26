# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class AsyncSearchClient(NamespacedClient):
    async def delete(
        self,
        id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get(
        self,
        id: Any,
        keep_alive: Optional[Any] = None,
        typed_keys: Optional[Any] = None,
        wait_for_completion_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def submit(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        allow_partial_search_results: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        batched_reduce_size: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        docvalue_fields: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        explain: Optional[Any] = None,
        from_: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        keep_alive: Optional[Any] = None,
        keep_on_completion: Optional[Any] = None,
        lenient: Optional[Any] = None,
        max_concurrent_shard_requests: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        request_cache: Optional[Any] = None,
        routing: Optional[Any] = None,
        search_type: Optional[Any] = None,
        seq_no_primary_term: Optional[Any] = None,
        size: Optional[Any] = None,
        sort: Optional[Any] = None,
        stats: Optional[Any] = None,
        stored_fields: Optional[Any] = None,
        suggest_field: Optional[Any] = None,
        suggest_mode: Optional[Any] = None,
        suggest_size: Optional[Any] = None,
        suggest_text: Optional[Any] = None,
        terminate_after: Optional[Any] = None,
        timeout: Optional[Any] = None,
        track_scores: Optional[Any] = None,
        track_total_hits: Optional[Any] = None,
        typed_keys: Optional[Any] = None,
        version: Optional[Any] = None,
        wait_for_completion_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
