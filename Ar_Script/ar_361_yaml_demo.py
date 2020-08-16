import yaml

with open('resources/yaml.yml')as f:
    print(yaml.load(f, Loader=yaml.FullLoader))


with open('tag.yml')as f:
    data=yaml.safe_load(f)


for i in data:
    print(i)