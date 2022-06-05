from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def testing_child_resource():
    return {"message": "Hi There! This is my route endpoint."}


@router.get("/hello/{x}")
async def hello(x: int):
    return {"message": f"Hello! :{x * 543}"}
