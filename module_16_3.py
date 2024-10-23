from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_user() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def userName(username: str = Path(min_length=5, max_length=20, description='Enter username',
                                        example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='33')) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def updateUser(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='7'),
                     username: str = Path(min_length=5, max_length=20, description='Enter username',
                                        example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='33')) -> str:
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def deleteUser(user_id: int) -> str:
    users.pop(user_id)
    return f'User with {user_id} was deleted.'


