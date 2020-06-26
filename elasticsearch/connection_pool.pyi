# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

import logging
from typing import Sequence, Optional, Type, Any, Union, List, Tuple, Dict
from .connection import Connection

try:
    from Queue import PriorityQueue  # type: ignore
except ImportError:
    from queue import PriorityQueue

logger: logging.Logger

class ConnectionSelector(object):
    def __init__(self, opts):
        self.connection_opts = opts
    def select(self, connections: Sequence[Connection]) -> Connection: ...

class RandomSelector(ConnectionSelector): ...
class RoundRobinSelector(ConnectionSelector): ...

class ConnectionPool(object):
    connections_opts: List[Tuple[Connection, Any]]
    connections: List[Connection]
    orig_connections: Tuple[Connection, ...]
    dead: PriorityQueue
    dead_count: Dict[Connection, int]
    dead_timeout: Union[float, int]
    timeout_cutoff: Union[float, int]
    selector: ConnectionSelector
    def __init__(
        self,
        connections,
        dead_timeout: int = 60,
        timeout_cutoff: int = 5,
        selector_class: Type[ConnectionSelector] = RoundRobinSelector,
        randomize_hosts: bool = True,
        **kwargs
    ): ...
    def mark_dead(
        self, connection: Connection, now: Optional[float] = None
    ) -> None: ...
    def mark_live(self, connection: Connection) -> None: ...
    def resurrect(self, force: bool = False) -> Optional[Connection]: ...
    def get_connection(self) -> Connection: ...
    def close(self) -> None: ...
    def __repr__(self) -> str: ...

class DummyConnectionPool(ConnectionPool):
    def __init__(self, connections, **kwargs):
        self.connection_opts = connections
        self.connection = connections[0][0]
        self.connections = (self.connection,)
    def get_connection(self) -> Connection: ...
    def close(self) -> None: ...
    def _noop(self, *args: Any, **kwargs: Any) -> Any: ...
    mark_dead = mark_live = resurrect = _noop

class EmptyConnectionPool(ConnectionPool):
    def __init__(self, *_: Any, **__: Any) -> None: ...
    def get_connection(self) -> Connection: ...
    def _noop(self, *args: Any, **kwargs: Any) -> Any: ...
    close = mark_dead = mark_live = resurrect = _noop
