import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cars, web
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR
from app.routers.cars import BadTripException


# Routers
app = FastAPI(title="Fast API Template")
app.include_router(cars.router)
app.include_router(web.router)


# Middleware
origins = [
    "http://localhost:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def global_exception_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as ex:
        # Add custom logging here in future. For now, just print to console.
        print(str(ex))
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error."},
        )


# Custom exception handlers
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
