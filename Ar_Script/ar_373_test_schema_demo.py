import json

from jsonschema import validate


dict2 = {"id": "503", "name": "班级优化2", "info": {"uid":2017,"stuName":["张三","赵五"]}}

schema=json.load(open('schema_demo.json'))

validate(dict2,schema=schema)