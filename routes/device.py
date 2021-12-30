from fastapi import Depends, APIRouter, HTTPException, status, Form


#from jose import jwt, JWTError

from typing import Optional, List
from datetime import datetime, timedelta

from models.device import Reading, Header 
import json

#USER_DB = 'detaBase'
USER_DB = 'mongodb'
if USER_DB == 'mongodb':
    ## MONGO DB
    from database import (
        retrieve_reading,
        add_reading,
        add_many_readings,
        retrieve_header,
        add_header,
    )
else:
    print("Invalid Database value")
    exit(1)
    
router = APIRouter()

@router.post("/reading")
async def post_readings(reading_data: Reading):
    print(f"POST: {reading_data}")
    new_reading=await add_reading(reading_data.dict())
    return new_reading

@router.post("/many")
async def post_many(header_id:str,reading_array:List[Reading]):
    print(F"POST Many {len(reading_array)}")
    print(f"HEADID : {header_id}")

    tmp_array = []
    retvals={}
    header_dict = {"header_id":header_id}
    for i in reading_array:
        i_dict = i.dict()
        i_dict.update(header_dict)
        print("I_DICT ",i_dict)
        tmp_array.append(i_dict)
    try:
        retvals = await add_many_readings(tmp_array)
        print("RETVALS :", retvals)
    except Exception as e:
        print("Error",e)
    return retvals



@router.get("/reading/{q}")
async def get_readings(q:Optional[str]=None):
    if q == None:
        q={}
    else:
        try:
            q = json.loads(q)
        except Exception:
            q = {}
            print("Ignoring parameter q")
    try:
        readings = await retrieve_reading(q)
    except Exception as e:
        print("Error : ",e)
        return {"Error":"Failed to read"}
    return readings


### on inserting the header - returns headers ID 
### - client to ensure it store this id for future use
@router.post("/header")
async def post_header(header_data:Header)->dict:
    print(f"POST : {type(header_data)} {header_data}")
    new_header = await add_header(header_data.dict())
    return {"id":new_header.pop("id",None)}

@router.get("/header/{q}")
async def get_header(q:Optional[str]=None):
    if q == None:
        q={}
    else:
        try:
            q = json.loads(q)
        except Exception:
            q = {}
            print("Ignoring parameter q")
    header = await retrieve_header(q)
    return header
