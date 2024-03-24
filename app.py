import asyncio

from fastapi import FastAPI, Response, Request, Header
from function.body import Body
from function.example import example
from API.hello_world import hello_world


app = FastAPI(docs_url="/docs", redoc_url="/redocs")


@app.post(
    "/",
    tags=["example_tag"],
    responses=example({"example_responses": "hello world"}),
)
async def hello_world_endpoint(
    request: Request,
    response: Response,
    test: str = Body(),
):
    result = await asyncio.to_thread(
        hello_world,
        test,
    )
    return result
