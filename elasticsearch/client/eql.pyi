# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class EqlClient(NamespacedClient):
    def search(
        self,
        index: Any,
        body: Any,
        keep_alive: Optional[Any] = None,
        keep_on_completion: Optional[Any] = None,
        wait_for_completion_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete(
        self,
        id: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get(
        self,
        id: Any,
        keep_alive: Optional[Any] = None,
        wait_for_completion_timeout: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
