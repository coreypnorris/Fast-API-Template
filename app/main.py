import uvicorn
from fastapi import FastAPI
from app.routers import cars

app = FastAPI(title="Fast API Template")
app.include_router(cars.router)


# This is required for VS Code IDE debugging.
# Also need to modify the launch.json for VS Code debugger to work per https://stackoverflow.com/a/63271966.
if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
