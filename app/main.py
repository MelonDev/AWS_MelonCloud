from fastapi import FastAPI
from mangum import Mangum
import uvicorn

from app.api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)


@app.get("/", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


if __name__ == '__main__':
    uvicorn.run(app)
