import os

with open(os.path.dirname(__file__)+ "../../sequence/a.txt", "a") as f:
    f.write("hello")
