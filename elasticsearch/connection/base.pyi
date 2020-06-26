# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

import logging

from typing import (
    Union,
    Optional,
    Mapping,
    Tuple,
    List,
    NoReturn,
    Dict,
    Sequence,
    Any,
    AnyStr,
)

logger: logging.Logger
tracer: logging.Logger

class Connection(object):
    headers: Dict[str, str]
    use_ssl: bool
    http_compress: bool

    scheme: str
    hostname: str
    port: Optional[int]
    host: str
    url_prefix: str
    timeout: Optional[Union[float, int]]
    def __init__(
        self,
        host: str = "localhost",
        port: Optional[int] = None,
        use_ssl: bool = False,
        url_prefix: str = "",
        timeout: Optional[Union[float, int]] = 10,
        headers: Optional[Mapping[str, str]] = None,
        http_compress: Optional[bool] = None,
        cloud_id: Optional[str] = None,
        api_key: Optional[Union[Tuple[str, str], List[str], str]] = None,
        opaque_id: Optional[str] = None,
        **kwargs
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def _gzip_compress(self, body: bytes) -> bytes: ...
    def _raise_warnings(self, warning_headers: Sequence[str]) -> None: ...
    def _pretty_json(self, data: Any) -> str: ...
    def _log_trace(
        self, method: str, path: str, body: AnyStr, status_code: int, response, duration
    ) -> None: ...
    def log_request_success(
        self,
        method: str,
        full_url: str,
        path: str,
        body: AnyStr,
        status_code: int,
        response: Any,
        duration: float,
    ) -> None: ...
    def log_request_fail(
        self,
        method: str,
        full_url: str,
        path: str,
        body,
        duration: float,
        status_code: Optional[int] = None,
        response: Optional[Any] = None,
        exception: Optional[Exception] = None,
    ) -> None: ...
    def _raise_error(self, status_code: int, raw_data: str) -> NoReturn: ...
    def _get_default_user_agent(self) -> str: ...
    def _get_api_key_header_val(
        self, api_key: Optional[Union[Tuple[str, str], List[str], str]]
    ) -> str: ...
