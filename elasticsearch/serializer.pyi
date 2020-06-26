# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Optional, Any, Dict

class Serializer(object):
    mimetype: str
    def loads(self, s: str) -> Any: ...
    def dumps(self, data: Any) -> str: ...

class TextSerializer(Serializer):
    mimetype: str
    def loads(self, s: str) -> Any: ...
    def dumps(self, data: Any) -> str: ...

class JSONSerializer(Serializer):
    mimetype: str
    def default(self, data: Any) -> Any: ...
    def loads(self, s: str) -> Any: ...
    def dumps(self, data: Any) -> str: ...

DEFAULT_SERIALIZERS: Dict[str, Serializer]

class Deserializer(object):
    def __init__(
        self,
        serializers: Dict[str, Serializer],
        default_mimetype: str = "application/json",
    ) -> None: ...
    def loads(self, s: str, mimetype: Optional[str] = None) -> Any: ...
