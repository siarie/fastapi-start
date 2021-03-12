from fastapi import APIRouter


router = APIRouter(prefix='/users', tags=['users'])

users_dummy = [
    {
        "id": 1,
        "username": "siarie",
        "email": "sri.aspari@pm.me"
    }, {
        "id": 2,
        "username": "michael",
        "email": "michael@mail.me"
    }, {
        "id": 3,
        "username": "angel",
        "email": "angel@hotmail.com"
    }
]


@router.get('/')
def get_all_users():
    return users_dummy


@router.get('/{id}')
def get_user_id(id: int):
    for user in users_dummy:
        if user['id'] == id:
            return user

    return {"message": "not found"}
