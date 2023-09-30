import os

os.makedirs("project", exist_ok=True)
print(os.path.exists("project"))
print(os.path.isfile("project"))