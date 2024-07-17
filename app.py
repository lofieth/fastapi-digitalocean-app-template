import asyncio

from API.hello_world import hello_world
from function.example import example
from function.body import Body
from fastapi import FastAPI


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
)


@app.post(
    path="/",
    responses=example({"example_responses": "hello world"}),
)
async def hello_world_endpoint(
    test: str = Body(),
):
    return await asyncio.to_thread(
        hello_world,
        test,
    )
