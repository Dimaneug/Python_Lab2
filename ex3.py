import os

for root, dirs, files in os.walk("."):
    for name in files:
        if name.endswith(".py"):
            print(os.path.abspath(os.path.join(root, name)))
