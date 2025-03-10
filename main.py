from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#pydantic validations

class Post(BaseModel):
    name: str
    company: str


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

@app.post("/post")
def create_posts(new_post: Post):
    print(new_post.name)
    print(new_post.company)
    return {"data":"new post"}