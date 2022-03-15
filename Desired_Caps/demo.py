
import yaml

fs = open("demo.yaml")
result = fs.read()
print(result)
res = yaml.safe_load(result)
print(res)
print(type(res))