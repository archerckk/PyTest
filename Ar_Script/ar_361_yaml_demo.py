import yaml

with open('resources/yaml.yml')as f:
    print(yaml.load(f, Loader=yaml.FullLoader))
