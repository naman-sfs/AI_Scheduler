from fastapi import APIRouter, Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from .scheduler import SCHEDULER
from ..models import Input

schedule_router = APIRouter(prefix='/api/schedule')

@schedule_router.get('/')
def get_api():
    return "schedule apis"

@schedule_router.post('/plan')
def set_plan(input:Input, res:Response):
    try:
        date = datetime.today().strftime('%m/%d/%Y')
        scheduler = SCHEDULER()
        
        answer = scheduler.create_events(date,input.text)

        data = {
            "date":date,
            "content":convert_to_dict(answer),
        }
        print(data)
        res.status_code = status.HTTP_200_OK
        return {"data":data,"message":"Response Generated","statusCode":status.HTTP_200_OK}
    
    except ValueError as ve:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"data":{},"message":str(ve),"statusCode":status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        print(str(e))
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"data":{},"message":"An error occurred: " + str(e),"statusCode":status.HTTP_500_INTERNAL_SERVER_ERROR}


@schedule_router.post('/goal')
def set_goral(input:Input, res:Response):
    try:
        date = datetime.today().strftime('%m/%d/%Y')
        scheduler = SCHEDULER()
        
        answer = scheduler.create_goals(date,input.text)
        print(answer)
        data = {
            "date":date,
            "content":convert_to_dict(answer),
        }
        
        res.status_code = status.HTTP_200_OK
        return {"data":data,"message":"Response Generated","statusCode":status.HTTP_200_OK}
    
    except ValueError as ve:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"data":{},"message":str(ve),"statusCode":status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"data":{},"message":"An error occurred: " + str(e),"statusCode":status.HTTP_500_INTERNAL_SERVER_ERROR}


def convert_to_dict(input_string):
    # Remove single quotes from the string
    input_string = input_string.replace("'", "")
    
    items = input_string.split(",")
    output_dict = {}
    for item in items:
        key, value = item.split(":")
        output_dict[key.strip()] = value.strip()
    return output_dict