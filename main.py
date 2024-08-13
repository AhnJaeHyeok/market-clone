from fastapi import FastAPI,UploadFile,Form,Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import sqlite3

con = sqlite3.connect('db.db',check_same_thread=False)
cur = con.cursor()

app = FastAPI()

@app.post('/items') #post를 통해서 items 라는 api 를 받는다
async def create_item(image:UploadFile,
                title:Annotated[str,Form()],
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()],
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]#폼데이터로 해서 넘어오겠다.
                ):
    
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO
                items(title,image,price,description,place,insertAt)
                VALUES('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
                """)#SQL. image_bytes.hex() 16진법으로 바꿈
    con.commit()
    return '200'

@app.get('/items')
async def get_items():
    #컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * From items;               
                       """).fetchall()
    
    return JSONResponse(jsonable_encoder(dict(row) for row in rows))

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor() #특정 id에 맞는 이미지 컬럼만 가져올라면 SELECT
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]
    
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')

@app.post('/signup')
def signup(id:Annotated[str, Form()], password:Annotated[str, Form()]):
    print(id, password)
    return '200'


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
