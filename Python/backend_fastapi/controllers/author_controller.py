from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from shared.modules.author_module import author_module
from shared.dto.schemas.author_dto import AuthorDTO

router = APIRouter()

author_service = author_module["service"]
author_mapper = author_module["dto_mapper"]

@router.get("/authors", status_code=status.HTTP_200_OK)
async def list_authors():
    authors = author_service.list_all_authors()
    return author_mapper.to_external_list(authors)

@router.get("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def get_author(author_id: int):
    author = author_service.get_author_by_id(author_id)
    if author:
        return author_mapper.to_external(author)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

@router.post("/authors", status_code=status.HTTP_201_CREATED)
async def create_author(dto: AuthorDTO):
    author = author_mapper.to_domain(dto.dict())
    created_author = author_service.create_author(author)
    return author_mapper.to_external(created_author)

@router.put("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def update_author(author_id: int, dto: AuthorDTO):
    updated_author = author_mapper.to_domain(dto.dict(), author_id)
    result = author_service.update_author(author_id, updated_author)
    if result:
        return author_mapper.to_external(result)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")

@router.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: int):
    author_service.delete_author(author_id)
    return {}