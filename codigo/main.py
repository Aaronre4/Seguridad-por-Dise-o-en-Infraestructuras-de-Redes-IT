import networkx as nx
import matplotlib.pyplot as plt
import copy
import json

from datosJSON import DatosJSON
from datosCodigo import DatosCodigo
from encontrarCaminos import caminos
from areasConectividad import areas

G = nx.Graph()

print("Eliga como se añadirán los datos:(número de elección)")
print("[1] -> Mediante un archivo JSON")
print("[2] -> Mediante un archivo de código Python")

while True:
    eleccion = int(input())
    if eleccion < 1 or eleccion > 2:
        print("Dicho número no es correcto")
    else:
        break
if eleccion == 1:
    DatosJSON(G)
elif eleccion == 2:
    DatosCodigo(G)
caminos(G)
areas(G)