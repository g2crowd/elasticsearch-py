# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class TasksClient(NamespacedClient):
    def list(
        self,
        actions: Optional[Any] = None,
        detailed: Optional[Any] = None,
        group_by: Optional[Any] = None,
        nodes: Optional[Any] = None,
        parent_task_id: Optional[Any] = None,
        timeout: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def cancel(
        self,
        task_id: Optional[Any] = None,
        actions: Optional[Any] = None,
        nodes: Optional[Any] = None,
        parent_task_id: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get(
        self,
        task_id: Any,
        timeout: Optional[Any] = None,
        wait_for_completion: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
