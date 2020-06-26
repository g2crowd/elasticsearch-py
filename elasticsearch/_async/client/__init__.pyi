# -*- coding: utf-8 -*-
# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from __future__ import unicode_literals
import logging
from typing import Any, Mapping, Optional, Type

from ..transport import AsyncTransport

from .async_search import AsyncSearchClient
from .autoscaling import AutoscalingClient
from .cat import CatClient
from .cluster import ClusterClient
from .dangling_indices import DanglingIndicesClient
from .indices import IndicesClient
from .ingest import IngestClient
from .nodes import NodesClient
from .remote import RemoteClient
from .snapshot import SnapshotClient
from .tasks import TasksClient

# xpack APIs
from .xpack import XPackClient
from .ccr import CcrClient
from .enrich import EnrichClient
from .eql import EqlClient
from .graph import GraphClient
from .ilm import IlmClient
from .license import LicenseClient
from .migration import MigrationClient
from .ml import MlClient
from .monitoring import MonitoringClient
from .rollup import RollupClient
from .searchable_snapshots import SearchableSnapshotsClient
from .security import SecurityClient
from .slm import SlmClient
from .sql import SqlClient
from .ssl import SslClient
from .transform import TransformClient
from .watcher import WatcherClient

logger: logging.Logger

class AsyncElasticsearch(object):
    transport: AsyncTransport

    async_search: AsyncSearchClient
    autoscaling: AutoscalingClient
    cat: CatClient
    cluster: ClusterClient
    indices: IndicesClient
    ingest: IngestClient
    nodes: NodesClient
    remote: RemoteClient
    snapshot: SnapshotClient
    tasks: TasksClient

    xpack: XPackClient
    ccr: CcrClient
    dangling_indices: DanglingIndicesClient
    enrich: EnrichClient
    eql: EqlClient
    graph: GraphClient
    ilm: IlmClient
    license: LicenseClient
    migration: MigrationClient
    ml: MlClient
    monitoring: MonitoringClient
    rollup: RollupClient
    searchable_snapshots: SearchableSnapshotsClient
    security: SecurityClient
    slm: SlmClient
    sql: SqlClient
    ssl: SslClient
    transform: TransformClient
    watcher: WatcherClient
    def __init__(
        self, hosts=None, transport_class=Type[AsyncTransport], **kwargs: Any
    ): ...
    def __repr__(self) -> str: ...
    async def __aenter__(self) -> "AsyncElasticsearch": ...
    async def __aexit__(self, *_: Any) -> None: ...
    async def close(self) -> None: ...
    # AUTO-GENERATED-API-DEFINITIONS #
    async def ping(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def info(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def create(
        self,
        index: Any,
        id: Any,
        body: Any,
        doc_type: Optional[Any] = None,
        pipeline: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def index(
        self,
        index: Any,
        body: Any,
        id: Optional[Any] = None,
        if_primary_term: Optional[Any] = None,
        if_seq_no: Optional[Any] = None,
        op_type: Optional[Any] = None,
        pipeline: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def bulk(
        self,
        body: Any,
        index: Optional[Any] = None,
        doc_type: Optional[Any] = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        pipeline: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def clear_scroll(
        self,
        body: Any = None,
        scroll_id: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def count(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        lenient: Optional[Any] = None,
        min_score: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        routing: Optional[Any] = None,
        terminate_after: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete(
        self,
        index: Any,
        id: Any,
        doc_type: Optional[Any] = None,
        if_primary_term: Optional[Any] = None,
        if_seq_no: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_by_query(
        self,
        index: Any,
        body: Any,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        conflicts: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        from_: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        lenient: Optional[Any] = None,
        max_docs: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        refresh: Optional[Any] = None,
        request_cache: Optional[Any] = None,
        requests_per_second: Optional[Any] = None,
        routing: Optional[Any] = None,
        scroll: Optional[Any] = None,
        scroll_size: Optional[Any] = None,
        search_timeout: Optional[Any] = None,
        search_type: Optional[Any] = None,
        slices: Optional[Any] = None,
        sort: Optional[Any] = None,
        stats: Optional[Any] = None,
        terminate_after: Optional[Any] = None,
        timeout: Optional[Any] = None,
        version: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_by_query_rethrottle(
        self,
        task_id: Any,
        requests_per_second: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def delete_script(
        self,
        id: Any,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def exists(
        self,
        index: Any,
        id: Any,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        stored_fields: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def exists_source(
        self,
        index: Any,
        id: Any,
        doc_type: Optional[Any] = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> bool: ...
    async def explain(
        self,
        index: Any,
        id: Any,
        body: Any = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        lenient: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        routing: Optional[Any] = None,
        stored_fields: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def field_caps(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        fields: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        include_unmapped: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get(
        self,
        index: Any,
        id: Any,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        stored_fields: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_script(
        self,
        id: Any,
        master_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_source(
        self,
        index: Any,
        id: Any,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def mget(
        self,
        body: Any,
        index: Optional[Any] = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        refresh: Optional[Any] = None,
        routing: Optional[Any] = None,
        stored_fields: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def msearch(
        self,
        body: Any,
        index: Optional[Any] = None,
        ccs_minimize_roundtrips: Optional[Any] = None,
        max_concurrent_searches: Optional[Any] = None,
        max_concurrent_shard_requests: Optional[Any] = None,
        pre_filter_shard_size: Optional[Any] = None,
        rest_total_hits_as_int: Optional[Any] = None,
        search_type: Optional[Any] = None,
        typed_keys: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def put_script(
        self,
        id: Any,
        body: Any,
        context: Optional[Any] = None,
        master_timeout: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def rank_eval(
        self,
        body: Any,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        search_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def reindex(
        self,
        body: Any,
        max_docs: Optional[Any] = None,
        refresh: Optional[Any] = None,
        requests_per_second: Optional[Any] = None,
        scroll: Optional[Any] = None,
        slices: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def reindex_rethrottle(
        self,
        task_id: Any,
        requests_per_second: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def render_search_template(
        self,
        body: Any = None,
        id: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def scripts_painless_execute(
        self,
        body: Any = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def scroll(
        self,
        body: Any = None,
        scroll_id: Optional[Any] = None,
        rest_total_hits_as_int: Optional[Any] = None,
        scroll: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def search(
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
        ccs_minimize_roundtrips: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        docvalue_fields: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        explain: Optional[Any] = None,
        from_: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        lenient: Optional[Any] = None,
        max_concurrent_shard_requests: Optional[Any] = None,
        pre_filter_shard_size: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        request_cache: Optional[Any] = None,
        rest_total_hits_as_int: Optional[Any] = None,
        routing: Optional[Any] = None,
        scroll: Optional[Any] = None,
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
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def search_shards(
        self,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        local: Optional[Any] = None,
        preference: Optional[Any] = None,
        routing: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def update(
        self,
        index: Any,
        id: Any,
        body: Any,
        doc_type: Optional[Any] = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        if_primary_term: Optional[Any] = None,
        if_seq_no: Optional[Any] = None,
        lang: Optional[Any] = None,
        refresh: Optional[Any] = None,
        retry_on_conflict: Optional[Any] = None,
        routing: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def update_by_query_rethrottle(
        self,
        task_id: Any,
        requests_per_second: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_script_context(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def get_script_languages(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def msearch_template(
        self,
        body: Any,
        index: Optional[Any] = None,
        ccs_minimize_roundtrips: Optional[Any] = None,
        max_concurrent_searches: Optional[Any] = None,
        rest_total_hits_as_int: Optional[Any] = None,
        search_type: Optional[Any] = None,
        typed_keys: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def mtermvectors(
        self,
        body: Any = None,
        index: Optional[Any] = None,
        field_statistics: Optional[Any] = None,
        fields: Optional[Any] = None,
        ids: Optional[Any] = None,
        offsets: Optional[Any] = None,
        payloads: Optional[Any] = None,
        positions: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        routing: Optional[Any] = None,
        term_statistics: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def search_template(
        self,
        body: Any,
        index: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        ccs_minimize_roundtrips: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        explain: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        preference: Optional[Any] = None,
        profile: Optional[Any] = None,
        rest_total_hits_as_int: Optional[Any] = None,
        routing: Optional[Any] = None,
        scroll: Optional[Any] = None,
        search_type: Optional[Any] = None,
        typed_keys: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def termvectors(
        self,
        index: Any,
        body: Any = None,
        id: Optional[Any] = None,
        field_statistics: Optional[Any] = None,
        fields: Optional[Any] = None,
        offsets: Optional[Any] = None,
        payloads: Optional[Any] = None,
        positions: Optional[Any] = None,
        preference: Optional[Any] = None,
        realtime: Optional[Any] = None,
        routing: Optional[Any] = None,
        term_statistics: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    async def update_by_query(
        self,
        index: Any,
        body: Any = None,
        _source: Optional[Any] = None,
        _source_excludes: Optional[Any] = None,
        _source_includes: Optional[Any] = None,
        allow_no_indices: Optional[Any] = None,
        analyze_wildcard: Optional[Any] = None,
        analyzer: Optional[Any] = None,
        conflicts: Optional[Any] = None,
        default_operator: Optional[Any] = None,
        df: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        from_: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        lenient: Optional[Any] = None,
        max_docs: Optional[Any] = None,
        pipeline: Optional[Any] = None,
        preference: Optional[Any] = None,
        q: Optional[Any] = None,
        refresh: Optional[Any] = None,
        request_cache: Optional[Any] = None,
        requests_per_second: Optional[Any] = None,
        routing: Optional[Any] = None,
        scroll: Optional[Any] = None,
        scroll_size: Optional[Any] = None,
        search_timeout: Optional[Any] = None,
        search_type: Optional[Any] = None,
        slices: Optional[Any] = None,
        sort: Optional[Any] = None,
        stats: Optional[Any] = None,
        terminate_after: Optional[Any] = None,
        timeout: Optional[Any] = None,
        version: Optional[Any] = None,
        version_type: Optional[Any] = None,
        wait_for_active_shards: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
