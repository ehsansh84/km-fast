from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder

from app.api_models.general import OutputOnlyNote, OutputCreate
from app.api_models.user import Read, Write, Update, ListRead
from app.db_models.os_user import OsUser as DataModel
from publics import exception_line
from app.core.log_tools import logger

module_name = 'user'
module_text = 'User'
router = APIRouter(
    prefix=f"/{module_name}",
    tags=[module_name]
)


@router.post("/", response_description=f"Create a {module_text}", status_code=status.HTTP_201_CREATED, response_model=OutputCreate)
async def create(item: Write):
    try:
        obj = DataModel()
        obj.set_payload(jsonable_encoder(item))
        if obj.exists('username', obj.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'{item.username} already exists!',
            )
        _id = obj.insert()
        return {
            'detail': f'{module_text} created.',
            'data': {
                'id': str(_id),
            }
        }
    except Exception as e:
        logger.log(e)


@router.put("/{_id}", response_description=f"Update a {module_text}", status_code=status.HTTP_200_OK, response_model=OutputOnlyNote)
async def update(_id, item: Update):
    obj = DataModel(_id=_id)
    obj.set_payload(jsonable_encoder(item))
    result = obj.update()
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{item.name} not found!',
        )
    return {"detail": f"{module_text} successfully updated."}


@router.delete("/{_id}", response_description=f"Delete a {module_text}", status_code=status.HTTP_200_OK, response_model=OutputOnlyNote)
async def delete(_id):
    obj = DataModel(_id=_id)
    result = obj.delete()
    if result['n'] == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{module_text} with id {_id} not found!',
        )
    return {
        'detail': f'{module_text} deleted.'
    }


@router.get("/", response_description=f"List all {module_text}s", response_model=ListRead)
async def get_list():
    obj = DataModel()
    return obj.list_json()


@router.get("/{_id}", response_description=f"Show a {module_text}", response_model=Read)
async def get_one(_id):
    obj = DataModel(_id=_id)
    obj.load()

    if obj.is_loaded():
        return obj.to_json()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{module_text} with id {_id} not found!',
        )
