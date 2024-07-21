from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from database.database import database


def hello_world(text):
    try:
        # Concatenate "hello_world " with the provided text and store it in the database
        hello_world = database("hello_world " + text)

        # Return a JSON response with the result
        return JSONResponse({"index": hello_world})

    except Exception as e:
        # Handle any exceptions that occur during execution
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
