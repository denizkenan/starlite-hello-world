"""Minimal Starlite application."""
from typing import Any
from starlite.datastructures import ResponseHeader
from starlite import Starlite, get, Request
from starlite.datastructures import Stream
from starlite.enums import MediaType
import io
from starlette.responses import StreamingResponse

@get("/hello", response_headers = {
        "testheader": ResponseHeader(value="test value",description="test")
    })
def hello_world() -> dict[str, Any]:
    """Hi."""
    return {"hello": "world"}


@get("/sup", media_type=MediaType.TEXT)
def wassup_world() -> Stream:
    """Hi."""
    byte_stream = io.BytesIO(b"some byte string\n")

    return Stream(iterator=byte_stream)


@get("/greetings", media_type=MediaType.TEXT)
def greetings_world(request: Request) -> StreamingResponse:
    byte_stream = io.BytesIO(b"some byte string\n\n")
    """Hi."""
    return Stream(iterator=byte_stream).to_response(
        headers={f"Content-Disposition": f"attachment; filename=my-file.xlsx"},
        media_type="application/vnd.ms-excel",
        status_code=200,
        app=request.app,
    )

app = Starlite(route_handlers=[hello_world,wassup_world,greetings_world])
