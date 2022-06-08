from fastapi import FastAPI
from mangum import Mangum

from api.v1.api import router as api_router
import uvicorn

app = FastAPI(title='MelonCloud')

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Main"])
def main():
    return {"message": "Hello! I'm MelonCloud"}


handler = Mangum(app=app)


if __name__ == '__main__':
    uvicorn.run(app)
