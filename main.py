
from fastapi import FastAPI

app = FastAPI()

# A path is also commonly called an endpoint or a route.

# The @app.get("/") tells FastAPI that the function right
# below is in charge of handling requests that go to 
# the path / using a get operation. 

# This is a decorator related to a path operation, 
# or a path operation decorator.

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Next: https://realpython.com/fastapi-python-web-apis/#path-parameters-get-an-item-by-id
