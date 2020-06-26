# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class MlClient(NamespacedClient):
    def close_job(
        self,
        job_id: Any,
        body: Any = None,
        allow_no_jobs: Optional[Any] = None,
        force: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_calendar(
        self,
        calendar_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_calendar_event(
        self,
        calendar_id: Any,
        event_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_calendar_job(
        self,
        calendar_id: Any,
        job_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_datafeed(
        self,
        datafeed_id: Any,
        force: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_expired_data(
        self,
        body: Any = None,
        job_id: Optional[Any] = None,
        requests_per_second: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_filter(
        self,
        filter_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_forecast(
        self,
        job_id: Any,
        forecast_id: Optional[Any] = None,
        allow_no_forecasts: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_job(
        self,
        job_id: Any,
        force: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_model_snapshot(
        self,
        job_id: Any,
        snapshot_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def find_file_structure(
        self,
        body: Any,
        charset: Optional[Any] = None,
        column_names: Optional[Any] = None,
        delimiter: Optional[Any] = None,
        explain: Optional[Any] = None,
        format: Optional[Any] = None,
        grok_pattern: Optional[Any] = None,
        has_header_row: Optional[Any] = None,
        line_merge_size_limit: Optional[Any] = None,
        lines_to_sample: Optional[Any] = None,
        quote: Optional[Any] = None,
        should_trim_fields: Optional[Any] = None,
        timeout: Optional[Any] = None,
        timestamp_field: Optional[Any] = None,
        timestamp_format: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def flush_job(
        self,
        job_id: Any,
        body: Any = None,
        advance_time: Optional[Any] = None,
        calc_interim: Optional[Any] = None,
        end: Optional[Any] = None,
        skip_time: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def forecast(
        self,
        job_id: Any,
        duration: Optional[Any] = None,
        expires_in: Optional[Any] = None,
        max_model_memory: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_buckets(
        self,
        job_id: Any,
        body: Any = None,
        timestamp: Optional[Any] = None,
        anomaly_score: Optional[Any] = None,
        desc: Optional[Any] = None,
        end: Optional[Any] = None,
        exclude_interim: Optional[Any] = None,
        expand: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        sort: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_calendar_events(
        self,
        calendar_id: Any,
        end: Optional[Any] = None,
        from_: Optional[Any] = None,
        job_id: Optional[Any] = None,
        size: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_calendars(
        self,
        body: Any = None,
        calendar_id: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_datafeed_stats(
        self,
        datafeed_id: Optional[Any] = None,
        allow_no_datafeeds: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_datafeeds(
        self,
        datafeed_id: Optional[Any] = None,
        allow_no_datafeeds: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_filters(
        self,
        filter_id: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_influencers(
        self,
        job_id: Any,
        body: Any = None,
        desc: Optional[Any] = None,
        end: Optional[Any] = None,
        exclude_interim: Optional[Any] = None,
        from_: Optional[Any] = None,
        influencer_score: Optional[Any] = None,
        size: Optional[Any] = None,
        sort: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_job_stats(
        self,
        job_id: Optional[Any] = None,
        allow_no_jobs: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_jobs(
        self,
        job_id: Optional[Any] = None,
        allow_no_jobs: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_overall_buckets(
        self,
        job_id: Any,
        body: Any = None,
        allow_no_jobs: Optional[Any] = None,
        bucket_span: Optional[Any] = None,
        end: Optional[Any] = None,
        exclude_interim: Optional[Any] = None,
        overall_score: Optional[Any] = None,
        start: Optional[Any] = None,
        top_n: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_records(
        self,
        job_id: Any,
        body: Any = None,
        desc: Optional[Any] = None,
        end: Optional[Any] = None,
        exclude_interim: Optional[Any] = None,
        from_: Optional[Any] = None,
        record_score: Optional[Any] = None,
        size: Optional[Any] = None,
        sort: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def info(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def open_job(
        self,
        job_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def post_calendar_events(
        self,
        calendar_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def post_data(
        self,
        job_id: Any,
        body: Any,
        reset_end: Optional[Any] = None,
        reset_start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def preview_datafeed(
        self,
        datafeed_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_calendar(
        self,
        calendar_id: Any,
        body: Any = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_calendar_job(
        self,
        calendar_id: Any,
        job_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_datafeed(
        self,
        datafeed_id: Any,
        body: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_filter(
        self,
        filter_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_job(
        self,
        job_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def set_upgrade_mode(
        self,
        enabled: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def start_datafeed(
        self,
        datafeed_id: Any,
        body: Any = None,
        end: Optional[Any] = None,
        start: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def stop_datafeed(
        self,
        datafeed_id: Any,
        allow_no_datafeeds: Optional[Any] = None,
        force: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def update_datafeed(
        self,
        datafeed_id: Any,
        body: Any,
        allow_no_indices: Optional[Any] = None,
        expand_wildcards: Optional[Any] = None,
        ignore_throttled: Optional[Any] = None,
        ignore_unavailable: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def update_filter(
        self,
        filter_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def update_job(
        self,
        job_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def validate(
        self,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def validate_detector(
        self,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_data_frame_analytics(
        self,
        id: Any,
        force: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def evaluate_data_frame(
        self,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_data_frame_analytics(
        self,
        id: Optional[Any] = None,
        allow_no_match: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_data_frame_analytics_stats(
        self,
        id: Optional[Any] = None,
        allow_no_match: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_data_frame_analytics(
        self,
        id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def start_data_frame_analytics(
        self,
        id: Any,
        body: Any = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def stop_data_frame_analytics(
        self,
        id: Any,
        body: Any = None,
        allow_no_match: Optional[Any] = None,
        force: Optional[Any] = None,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_trained_model(
        self,
        model_id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_trained_models(
        self,
        model_id: Optional[Any] = None,
        allow_no_match: Optional[Any] = None,
        decompress_definition: Optional[Any] = None,
        for_export: Optional[Any] = None,
        from_: Optional[Any] = None,
        include_model_definition: Optional[Any] = None,
        size: Optional[Any] = None,
        tags: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_trained_models_stats(
        self,
        model_id: Optional[Any] = None,
        allow_no_match: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_trained_model(
        self,
        model_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def estimate_model_memory(
        self,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def explain_data_frame_analytics(
        self,
        body: Any = None,
        id: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_categories(
        self,
        job_id: Any,
        body: Any = None,
        category_id: Optional[Any] = None,
        from_: Optional[Any] = None,
        partition_field_value: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_model_snapshots(
        self,
        job_id: Any,
        body: Any = None,
        snapshot_id: Optional[Any] = None,
        desc: Optional[Any] = None,
        end: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        sort: Optional[Any] = None,
        start: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def revert_model_snapshot(
        self,
        job_id: Any,
        snapshot_id: Any,
        body: Any = None,
        delete_intervening_results: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def update_model_snapshot(
        self,
        job_id: Any,
        snapshot_id: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
