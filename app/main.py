from fastapi import FastAPI, Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

#pydantic validations

class Post(BaseModel):
    name: str
    description: str
    published:bool=True
    # rating: Optional[int] = None

while True:


    try:
        conn=psycopg2.connect(host='localhost', database='fastapi_database', user='postgres',password='aSWIN@2000', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("The bluetooth device connected succesfully!")
        break
    except Exception as error:
        print("Database connection error")
        print("The error is: ", error)



@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts=cursor.fetchall()    
    print(posts)
    conn.commit()
    return{"data":posts}

# my_posts=[{"name":"name of first person", "company":"company of first person", "id":1 },{"name":"name of second person", "company": "company of second person", "id":2}]

# @app.get("/msg")
# def read_root():
#     return {"Hello"}

# @app.get("/")
# def get_elmnt():
#     return{"Welcome to the Home Page"}


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

# def find_post(id:int):
#     for i in my_posts:
#         if i['id']==id:
#             return i


# @app.post("/post")
# def create_posts(post:Post):
#     post_dict=post.dict()
#     post_dict['id']=randrange(0,100000)
#     my_posts.append(post_dict)
#     # print(my_posts)
#     return {"data": post_dict}

# @app.get("/post/{id}")
# def get_posts(id:int):
#     print(id)
#     return {f"The id is {id}"}


# @app.get("/post/{id}")
# def get_posts(id:int, response:Response):
    
#     post=find_post(int(id))
#     if not post:
#         raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=f"Not found, go away!")
        # response.status_code=status.HTTP_402_PAYMENT_REQUIRED
        # return {"message":f"The thing which you are looking is not found"}

    # print(post)
    

# @app.get("/post/latest")
# def latest_post():
#     post=my_posts[len(my_posts)-1]
#     # print(post)
#     return post

# def find_index_post(id: int):
#     for index, post in enumerate(my_posts):
#         if post["id"] == id:
#             return index
#     return None  # Return None if not found


# @app.put("/post/{id}")
# def update(id:int, post:Post):
#     index=find_index_post(id)

#     if index==None:
#         raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=f"Not found, go away!")
    
#     post_dict=post.dict()
#     post_dict['id']=id
#     my_posts[index]=post_dict
#     return {"data":post_dict}

