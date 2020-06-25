import json
import os
folderPath = os.getcwd()
path = "{folderPath}/project/packages/env.json".format(folderPath=folderPath)
envFile = open(path)

env = json.loads(envFile.read())
PYTHON_CAR = os.environ['PYTHON_CAR']
currentEnv = env[PYTHON_CAR]
