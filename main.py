from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Record(BaseModel):
    id: int
    data: str

records_db = []

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"user": "test"}

@app.post("/records", response_model=Record)
def create_record(record: Record, user: dict = Depends(get_current_user)):
    records_db.append(record)
    return record

@app.get("/records/{record_id}", response_model=Record)
def get_record(record_id: int, user: dict = Depends(get_current_user)):
    for record in records_db:
        if record.id == record_id:
            return record
    raise HTTPException(status_code=404, detail="Record not found")

@app.put("/records/{record_id}", response_model=Record)
def update_record(record_id: int, updated_record: Record, user: dict = Depends(get_current_user)):
    for index, record in enumerate(records_db):
        if record.id == record_id:
            records_db[index] = updated_record
            return updated_record
    raise HTTPException(status_code=404, detail="Record not found")

@app.delete("/records/{record_id}")
def delete_record(record_id: int, user: dict = Depends(get_current_user)):
    for index, record in enumerate(records_db):
        if record.id == record_id:
            del records_db[index]
            return {"message": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Record not found")

@app.get("/records", response_model=List[Record])
def list_records(user: dict = Depends(get_current_user)):
    return records_db
