import subprocess

packages = [
    "pydot",
    "graphviz",
    "networkx",
    "matplotlib"
]

for package in packages:
    subprocess.check_call(["pip", "install", package])