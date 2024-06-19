from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Wisdom(BaseModel):
    id: Optional[UUID] = None
    wisdom: Optional[str] = None

wisdoms = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/wisdomDZ/", response_model=Wisdom)
def create_tasks(wisdom: Wisdom):
    wisdom.id = uuid4()
    wisdoms.append(wisdom)
    return wisdom

@app.get("/wisdomDZ/", response_model=List[Wisdom])
def read_tasks():
    return wisdoms

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
