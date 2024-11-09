from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from shared.modules.user_module import user_module
from shared.dto.schemas.user_dto import UserDTO

router = APIRouter()

user_service = user_module["service"]
user_dto_mapper = user_module["dto_mapper"]

@router.get("/users", status_code=status.HTTP_200_OK)
async def list_users():
    users = user_service.list_all_users()
    return user_dto_mapper.to_external_list(users)

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user:
        return user_dto_mapper.to_dto(user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, dto: UserDTO):
    updated_user = user_dto_mapper.to_domain(dto.dict(), user_id)
    result = user_service.update_user(user_id, updated_user)
    if result:
        return user_dto_mapper.to_dto(result)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    user_service.delete_user(user_id)
    return {}
