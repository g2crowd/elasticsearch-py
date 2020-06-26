# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import (
    Callable,
    Optional,
    Union,
    Collection,
    Type,
    overload,
    Mapping,
    Any,
    Dict,
    List,
)
from typing_extensions import Literal

from .connection import Connection
from .connection_pool import ConnectionPool
from .serializer import JSONSerializer, Serializer, Deserializer

def get_host_info(
    node_info: Dict[str, Any], host: Optional[Dict[str, Any]]
) -> Optional[Dict[str, Any]]: ...

class Transport(object):
    DEFAULT_CONNECTION_CLASS: Type[Connection]
    connection_pool: ConnectionPool
    deserializer: Deserializer

    max_retries: int
    retry_on_timeout: bool
    retry_on_status: Collection[int]
    send_get_body_as: str
    serializer: Serializer
    connection_pool_class: Type[ConnectionPool]
    connection_class: Type[Connection]
    kwargs: Any
    hosts: Optional[List[Dict[str, Any]]]
    seed_connections: List[Connection]
    sniffer_timeout: Optional[float]
    sniff_on_start: bool
    sniff_on_connection_fail: bool
    last_sniff: float
    sniff_timeout: Optional[float]
    host_info_callback: Callable[
        [Dict[str, Any], Optional[Dict[str, Any]]], Dict[str, Any]
    ]
    def __init__(
        self,
        hosts: Union[str, Collection[str]],
        connection_class: Optional[Type[Connection]] = None,
        connection_pool_class: Type[ConnectionPool] = ConnectionPool,
        host_info_callback: Callable[
            [Dict[str, Any], Dict[str, Any]], Optional[Dict[str, Any]]
        ] = get_host_info,
        sniff_on_start: bool = False,
        sniffer_timeout: Optional[Union[float, int]] = None,
        sniff_timeout: float = 0.1,
        sniff_on_connection_fail: bool = False,
        serializer: Serializer = JSONSerializer(),
        serializers=None,
        default_mimetype: str = "application/json",
        max_retries: int = 3,
        retry_on_status: Collection[int] = (502, 503, 504),
        retry_on_timeout: bool = False,
        send_get_body_as: str = "GET",
        **kwargs
    ) -> None: ...
    def add_connection(self, host): ...
    def set_connections(self, hosts) -> None: ...
    def get_connection(self) -> Connection: ...
    def sniff_hosts(self, initial: bool = False) -> None: ...
    def mark_dead(self, connection: Connection) -> None: ...
    @overload
    def perform_request(
        self,
        method: Literal["HEAD"],
        url: str,
        headers: Optional[Mapping[str, str]] = None,
        params: Optional[Mapping[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> bool: ...
    @overload
    def perform_request(
        self,
        method: str,
        url: str,
        headers: Optional[Mapping[str, str]] = None,
        params: Optional[Mapping[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> Union[str, bool]: ...
    def close(self) -> None: ...
