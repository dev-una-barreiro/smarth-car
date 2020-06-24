import json
import os

path = f'{os.getcwd()}/project/packages/env.json'
envFile = open(path)

env = json.loads(envFile.read())
PYTHON_CAR = os.environ['PYTHON_CAR']
currentEnv = env[PYTHON_CAR]
