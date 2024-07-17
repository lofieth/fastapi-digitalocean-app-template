from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from database.database import database


def hello_world(text):
    try:
        hello_world = database("hello_world " + text)
        return JSONResponse({"index": hello_world})

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
