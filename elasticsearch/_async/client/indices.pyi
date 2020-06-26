# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class IndicesClient(NamespacedClient):
    async def analyze(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def refresh(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def flush(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        force: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        wait_if_ongoing: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def create(
        self,
        index: Any,
        body: Any = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def clone(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        include_defaults: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def open(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def close(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def exists(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        include_defaults: Optional[Any] = None,
        local: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def exists_type(
        self,
        index: Any,
        doc_type: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        local: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def put_mapping(
        self,
        index: Any,
        body: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_mapping(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def put_alias(
        self,
        index: Any,
        name: Any,
        body: Any = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def exists_alias(
        self,
        name: Any,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        local: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def get_alias(
        self,
        index: Optional[Any] = None,
        name: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        local: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def update_aliases(
        self,
        body: Any,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_alias(
        self,
        index: Any,
        name: Any,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def put_template(
        self,
        name: Any,
        body: Any,
        create: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        order: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def exists_template(
        self,
        name: Any,
        flat_settings: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def get_template(
        self,
        name: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_template(
        self,
        name: Any,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_settings(
        self,
        index: Optional[Any] = None,
        name: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        include_defaults: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def put_settings(
        self,
        body: Any,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        preserve_existing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def stats(
        self,
        index: Optional[Any] = None,
        metric: Optional[Any] = None,
        completion_fields: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        fielddata_fields: Optional[Any] = None,
        fields: Optional[Any] = None,
        forbid_closed_indices: Optional[Any] = None,
        groups: Optional[Any] = None,
        include_segment_file_sizes: Optional[Any] = None,
        include_unloaded_segments: Optional[Any] = None,
        level: Optional[Any] = None,
        types: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def segments(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        verbose: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def clear_cache(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        fielddata: Optional[Any] = None,
        fields: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        query: Optional[Any] = None,
        request: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def recovery(
        self,
        index: Optional[Any] = None,
        active_only: Optional[Any] = None,
        detailed: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def upgrade(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        only_ancient_segments: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_upgrade(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def shard_stores(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        status: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def forcemerge(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        flush: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        max_num_segments: Optional[Any] = None,
        only_expunge_deletes: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def shrink(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def split(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def rollover(
        self,
        alias: Any,
        body: Any = None,
        new_index: Optional[Any] = None,
        dry_run: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def freeze(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def unfreeze(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def reload_search_analyzers(
        self,
        index: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_field_mapping(
        self,
        fields: Any,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        include_defaults: Optional[Any] = None,
        local: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def validate_query(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        doc_type: Optional[Any] = None,
        all_shards: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        explain: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        lenient: Optional[Any] = None,
        q: Optional[Any] = None,
        rewrite: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def create_data_stream(
        self,
        name: Any,
        body: Any = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_data_stream(
        self,
        name: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_index_template(
        self,
        name: Any,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_index_template(
        self,
        name: Optional[Any] = None,
        flat_settings: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def put_index_template(
        self,
        name: Any,
        body: Any,
        cause: Optional[Any] = None,
        create: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def exists_index_template(
        self,
        name: Any,
        flat_settings: Optional[Any] = None,
        local: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def simulate_index_template(
        self,
        name: Any,
        body: Any = None,
        cause: Optional[Any] = None,
        create: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_data_stream(
        self,
        name: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def simulate_template(
        self,
        body: Any = None,
        name: Optional[Any] = None,
        cause: Optional[Any] = None,
        create: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def resolve_index(
        self,
        name: Any,
        expand_wildcards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
