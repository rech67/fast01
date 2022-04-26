from typing import Optional
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Form

app = FastAPI()
tmp = Jinja2Templates(directory="html")

@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World"}

@app.get("/form/{item_id}")
async def read_item(request: Request, item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
