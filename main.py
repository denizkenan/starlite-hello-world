"""Minimal Starlite application."""
from typing import Any
from starlite.datastructures import ResponseHeader
from starlite import Starlite, get


@get("/", response_headers = {
        "testheader": ResponseHeader(value="test value",description="test")
    })
def hello_world() -> dict[str, Any]:
    """Hi."""
    return {"hello": "world"}


app = Starlite(route_handlers=[hello_world])
