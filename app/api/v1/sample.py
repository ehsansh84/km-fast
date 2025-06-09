from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder

from app.api_models.general import OutputOnlyNote, OutputCreate
from app.api_models.sample import Read, Write, Update
from app.db_models.sample import Sample as DataModel
from app.core.auth import Token, get_token

module_name = 'sample'
module_text = 'Sample'
router = APIRouter(
    prefix=f"/{module_name}",
    tags=[module_name]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutputCreate)
async def create(item: Write, token: Token = Depends(get_token)):
    obj = DataModel()
    obj.set_payload(jsonable_encoder(item))
    _id = obj.insert()

    return {
        'detail': f'{module_text} created.',
        'data': {
            'id': str(_id)
        }
    }


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=OutputOnlyNote)
async def update(id, item: Update, token: Token = Depends(get_token)):
    obj = DataModel(_id=id)
    obj.set_payload(jsonable_encoder(item))
    result = obj.update()
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{id} not updated!',
        )
    return {"detail": f"{module_text} successfully updated."}


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=OutputOnlyNote)
async def delete(id, token: Token = Depends(get_token)):
    obj = DataModel(_id=id)
    result = obj.delete()
    if result['n'] == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{module_text} with id {id} not found!',
        )
    return {
        'detail': f'{module_text} deleted.',
        'data': {
            'id': str(id)
        }
    }


@router.get("/", response_description=f"List all {module_text}s")
async def get_list(token: Token = Depends(get_token)):
    obj = DataModel()
    return obj.list_json()


@router.get("/{id}", response_description=f"Show a {module_text}", response_model=Read)
async def get_one(id, token: Token = Depends(get_token)):
    obj = DataModel(_id=id)
    obj.load()

    if obj.is_loaded():
        return obj.to_json()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{module_text} with id {id} not found!',
        )
