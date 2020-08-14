import os

print(os.listdir("."))
path = os.path.join(".","testPath.py")
print(os.path.isfile(path))