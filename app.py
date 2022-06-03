from datetime import datetime
import typing
from uuid import uuid1
import strawberry
import requests
import json

# FETCH THE DATA TO USE IT
response_API = requests.get('http://localhost:5000/api/users').json()
users = response_API

@strawberry.type
class User:
    userId: int
    userName: str
    userPwd: str
    userCreation: datetime

@strawberry.input
class UserInputType:
    userName: str
    userPwd: str

# users = [
#     User(userId=1, userName='Luis', userPwd='123', userCreation='123'),
#     User(userId=2, userName='Felipe', userPwd='123', userCreation='123'),
#     User(userId=3, userName='LuF', userPwd='123', userCreation='123'),
# ]

def get_Users():
    print(users)
    return users

@strawberry.type
class Query:
    get_users: typing.List[User] = strawberry.field(resolver=get_Users)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, info, user: UserInputType) -> User:
        user = User(
            userName = user.userName,
            userPwd = user.userPwd,
        )
        users.append(user)
        return user

    @strawberry.mutation
    def update_user(self, info, id: int, user: UserInputType) -> User:
        old_user = users[id]
        old_user.name = user.name
        old_user.pwd = user.pwd
        return old_user
    
    @strawberry.mutation
    def delete_user(self, info, id: int) -> User:
        old_user = users[id]
        del users[id]
        return old_user

schema = strawberry.Schema(query = Query, mutation = Mutation)