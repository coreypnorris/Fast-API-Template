import uvicorn
from fastapi import FastAPI, Request
from app.routers import cars, web
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from app.routers.cars import BadTripException

app = FastAPI(title="Fast API Template")
app.include_router(cars.router)
app.include_router(web.router)

@app.exception_handler(BadTripException)
async def unicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad Trip"},
    )

# This is required for VS Code IDE debugging.
# Also need to modify the launch.json for VS Code debugger to work per https://stackoverflow.com/a/63271966.
if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
