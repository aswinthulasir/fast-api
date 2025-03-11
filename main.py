from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

#pydantic validations

class Post(BaseModel):
    name: str
    company: str
    published:bool=True
    rating: Optional[int] = None


my_posts=[{"name":"name of first person", "company":"company of first person", "id":1 },{"name":"name of second person", "company": "company of second person", "id":2}]

@app.get("/msg")
def read_root():
    return {"Hello"}

@app.get("/")
def get_elmnt():
    return{"Welcome to the Home Page"}


# @app.post("/post")
# def create_posts(payload: dict= Body(...)):
#     print(payload)
#     return{"Details":f"name : {payload['name']} company : {payload['company']}"}




# @app.post("/post")
# def create_posts(new_post: Post):
#     print(new_post.name)
#     print(new_post.company)
#     print(new_post.published)
#     print(new_post.rating)
#     print(new_post.dict())
#     return {"data":"new post"}

def find_post(id:int):
    for i in my_posts:
        if i['id']==id:
            return i


@app.post("/post")
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    # print(my_posts)
    return {"data": post_dict}

# @app.get("/post/{id}")
# def get_posts(id:int):
#     print(id)
#     return {f"The id is {id}"}


# @app.get("/post/{id}")
# def get_posts(id):
#     post=find_post(int(id))
#     print(post)
    

@app.get("/post/latest")
def latest_post():
    post=my_posts[len(my_posts)-1]
    # print(post)
    return post