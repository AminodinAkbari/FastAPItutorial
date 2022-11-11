from fastapi import APIRouter , FastAPI , UploadFile , File
from pydantic import BaseModel
from typing import Optional
import shutil

router = APIRouter(prefix='/test-post')

class CostumModel(BaseModel):
	model_id : int
	content : str
	like : Optional[bool]


@router.post('/First')
def test(Content:CostumModel):
	return {"Model_ID" : Content.model_id}

@router.post('/uploadfile')
def uploadfile(file:UploadFile=File(...)):
	name = file.filename
	path = f'files/{name}'
	with open(path , 'w+b') as OPEN:
		shutil.copyfileobj(file.file , OPEN)
		
	return {"name" : name}