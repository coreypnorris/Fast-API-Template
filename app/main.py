from fastapi import FastAPI


app = FastAPI(title="Fast API Template")


@app.get("/")
def welcome():
    """Return a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service!"}
