import motor.motor_asyncio 
from bson.objectid import ObjectId
from os import getenv



DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')

MONGO_DETAILS = f"mongodb+srv://{DB_USER}:{DB_PWD}@{DB_HOST}?retryWrites=true&w=majority"

print(MONGO_DETAILS)
try:
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    database = client.deviceDB
except Exception as e:
    print(f"Error : {e}")
    #exit(1)

reading_collection = database.get_collection("readings")
header_collection = database.get_collection("headers")
## readins
#helpers

def reading_helper(readings) ->dict:
    id = {"id":str(readings.pop("_id",None))}
    hid = {"header_id":str(readings.pop("header_id",None))}
    readings.update(id)
    readings.update(hid)
    return readings

#DB functions
## Retrieve all users from the database
async def retrieve_reading(q:dict):
    readings=[]
    print(f"[INFO Retrieve] q = {q}")
    try:
        async for reading in reading_collection.find(q):
            readings.append(reading_helper (reading))
            print(f"[INFO Retrieve]  reading = {reading}")
    except Exception as e:
        print("Error : ",e)
        return []

    return  readings

# Add a new reading into to the database
async def add_reading(reading_data: dict) -> dict:
    print(f"INSERTONE {type(reading_data)} : {reading_data}")
    reading = await reading_collection.insert_one(reading_data)
    new_reading = await reading_collection.find_one({"_id": reading.inserted_id})
    return reading_helper(new_reading)

async def add_many_readings(reading_array: list) -> dict:
    print(f"INSERTMANY {len(reading_array)} {type(reading_array)}")
    try:
        for reading in reading_array:
            print(f"READING: {type(reading)} {reading}")
            header_id = reading.pop("header_id")
            print(f"POPED: {header_id}")
            reading.update({"header_id":ObjectId(header_id)})
        retval = await reading_collection.insert_many(reading_array)
        print(f"ACK : {retval.acknowledged}")
        print(f"IDS : {retval.inserted_ids}")
    except Exception as e:
        print(e)
        return {"Error":e}
    ids = [str(x) for x in retval.inserted_ids]
    return {"ack":retval.acknowledged,"num_ids":len(retval.inserted_ids),"ids":ids}


""" Delete needs a diff approach
    the reading to delete needs - specific id number
    alternately - make provision to delete all packets with same header 

# Delete a student from the database
async def delete_user(username: str):
    if username:
        print(f"[DB Delete] {username}")
        await user_collection.delete_one({"username": username})
        return True

### no corrections allowed as readings once writted should not be changed.
## Repurpose for user update
# Update a student with a matching ID
async def update_user(username: str, data: dict):
    # Return false if an empty request body is sent.
    if username:
        updated_user = await user_collection.update_one(
            {"username": username}, {"$set": data}
        )
        if updated_user:
            return True
        return False
"""


def header_helper(header) ->dict:
    id = {"id":str(header.pop("_id",None))}
    header.update(id)
    return header

#DB functions
## Retrieve all users from the database
async def retrieve_header(q:dict):
    headers=[]
    print(f"[INFO Retrieve] q = {q}")
    async for header in header_collection.find(q):
        headers.append(header_helper(header))
    print(f"[INFO Retrieve]  reading = {header}")
    return  headers

# Add a new reading into to the database
async def add_header(header_data: dict) -> dict:
    header = await header_collection.insert_one(header_data)
    new_header = await header_collection.find_one({"_id": header.inserted_id})
    return header_helper(new_header)



print(40*"*")
print("DATA BASE is MONGO DB")
print(40*"*")