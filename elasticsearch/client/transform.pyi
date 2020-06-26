# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class TransformClient(NamespacedClient):
    def delete_transform(
        self,
        transform_id: Any,
        force: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_transform(
        self,
        transform_id: Optional[Any] = None,
        allow_no_match: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_transform_stats(
        self,
        transform_id: Any,
        allow_no_match: Optional[Any] = None,
        from_: Optional[Any] = None,
        size: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def preview_transform(
        self,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_transform(
        self,
        transform_id: Any,
        body: Any,
        defer_validation: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def start_transform(
        self,
        transform_id: Any,
        timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def stop_transform(
        self,
        transform_id: Any,
        allow_no_match: Optional[Any] = None,
        force: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_checkpoint: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def update_transform(
        self,
        transform_id: Any,
        body: Any,
        defer_validation: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
