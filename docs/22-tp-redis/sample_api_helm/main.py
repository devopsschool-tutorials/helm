#!/usr/bin/python3

import sys, time, random, pickle, os, yaml
from fastapi import FastAPI
from redis import Redis
from typing import Optional
from pydantic import BaseModel, BaseSettings
from fastapi.encoders import jsonable_encoder
import uvicorn

api_path = "/api/v1/"
yaml_settings = dict()
local_path = os.path.abspath(os.path.dirname(__file__))

if os.path.isfile(os.path.join(local_path, "config.yaml")):

  with open(os.path.join(local_path, "config.yaml"), "r") as ymlfile:
    yaml_settings = yaml.load(ymlfile, Loader=yaml.FullLoader)

  redis_password   = yaml_settings['redis_password']
  redis_host       = yaml_settings['redis_host']
  app_listen       = yaml_settings['app_listen']
  app_port         = yaml_settings['app_port']

elif os.getenv('REDIS_HOST') and os.environ.get('REDIS_PASSWORD'):

  redis_host       = os.getenv('REDIS_HOST')
  redis_password   = os.environ.get('REDIS_PASSWORD')
  app_port         = 8000
  app_listen       = "127.0.0.1"

else:
 
  print("Erreur - no config.yaml file or environement variables")
  sys.exit(1)


## Classes

class Config(BaseSettings):
    redis_password: str = redis_password
    redis_host: str     = redis_host

class Person(BaseModel):
    name: str
    city: str
    age: int

seconds = [0.5, 1, 1.5, 3 ]

app = FastAPI()
config = Config()

redis = Redis(
    host = config.redis_host, 
    password = config.redis_password,
    db = 0, 
    socket_timeout = 5, 
    charset = "utf-8"
    )

@app.get(api_path + 'health')
def health():
    return jsonable_encoder({"message": "response ok"})

@app.get(api_path +'delay')
def delay():
    delay = random.choice(seconds)
    time.sleep(delay)
    return jsonable_encoder({"delay": str(delay) + "s" })


@app.post(api_path + 'insert')
def insert(person: Person):
        
        data = { "name": person.name, "city": person.city, "age": person.age }
        p_data = pickle.dumps(data)
   
        redis.set(person.name, p_data)
        response = { "new user": person.name }
        return jsonable_encoder(response)

@app.get(api_path + 'list')
def list_all():
        response = []
        for key in redis.scan_iter():
          response.append(key.decode("utf-8"))
        return jsonable_encoder(response)

@app.get(api_path + 'get/{name}')
def person(name):
        print(name)
        p_data = redis.get(name)
        if p_data:
          data = pickle.loads(p_data)
        else:
          data = {"message":"user unknown"}
        return jsonable_encoder(data)

@app.get(api_path + 'clear')
def clean_keys():
        count = 0
        for key in redis.scan_iter():
          redis.delete(key)
          count += 1
        response = { "elements deleted": count }
        return jsonable_encoder(response)

if __name__ == "__main__":

  uvicorn.run(
     "main:app", 
     host = app_listen, 
     port = app_port, 
     log_level = "info"
     )

#Example curl --header "Content-Type: application/json" --request POST --data '{"name":"xavki", "city":"Paris", "age":"32"}' 172.22.0.2:80/insert

