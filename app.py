import asyncio

from fastapi import FastAPI
from function.body import Body
from function.example import example
from API.hello_world import hello_world


app = FastAPI(docs_url="/docs", redoc_url="/redocs")


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
