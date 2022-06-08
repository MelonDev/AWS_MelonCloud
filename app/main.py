from fastapi import FastAPI
from mangum import Mangum

from api.v1.api import router as api_router
import uvicorn

from app.environment.environment import SECRET_KEY

app = FastAPI(title='MelonCloud', openapi_prefix="/stage")

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Main"])
def main():
    return {"message": "Hello! I'm MelonCloud"}


@app.get("/env", tags=["Main"])
def env():
    return {"message": SECRET_KEY}


handler = Mangum(app=app)

if __name__ == '__main__':
    uvicorn.run(app)
