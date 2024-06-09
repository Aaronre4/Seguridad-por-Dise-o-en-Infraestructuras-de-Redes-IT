import networkx as nx
import matplotlib.pyplot as plt
import copy
import json
from datosJSON import DatosJSON
from datosCodigo import DatosCodigo

# Función recursiva para poder encontrar todos los caminos desde un nodo inicial a un destino con restricción sobre un atributo

def encontrar_caminos(grafo, nodo_actual, nodo_destino, nivel,camino_actual=[]):
    camino_actual = camino_actual + [nodo_actual]  # Agregar el nodo actual al camino actual
    nivel_aceptado = False
    if nodo_actual == nodo_destino:   # Si hemos alcanzado el nodo de destino, añadir el camino actual a la lista de caminos
        return [camino_actual]
    
    caminos = []  # Lista para almacenar todos los caminos encontrados
    
    for vecino in grafo.neighbors(nodo_actual):

        if nivel == 2:
            nivel_aceptado = grafo.nodes[vecino].get('nivel2', False)
        if nivel == 3:
            nivel_aceptado = grafo.nodes[vecino].get('nivel3', False)
        if nivel == 4:
            nivel_aceptado = grafo.nodes[vecino].get('nivel4', False)

        if nivel_aceptado:
            if vecino not in camino_actual:  # Evitar ciclos
                nuevos_caminos = encontrar_caminos(grafo, vecino, nodo_destino, nivel, camino_actual)
                for nuevo_camino in nuevos_caminos:
                    caminos.append(nuevo_camino)

    return caminos

def caminos(Grafo):

    print("Elige un Nodo Inicial para empezar la búsqueda")
    while True:
        nodo_inicial = input().upper()
        if nodo_inicial in Grafo.nodes():
            break
        print("No se encuentra ese nodo en el grafo, escribe uno que se encuentre en él")
    print("Elige un Nodo Destino para finalizar la búsqueda")
    while True:
        nodo_destino = input().upper()
        if nodo_destino in Grafo.nodes():
            break
        print("No se encuentra ese nodo en el grafo, escribe uno que se encuentre en él")
    print("Que nivel de caminos quieres buscar")
    nivel = int(input())
    
    #Lista de caminos encontrados
    caminos = encontrar_caminos(Grafo,nodo_inicial, nodo_destino, nivel)

    # for camino in caminos:
    #     print(camino)

    # Encontramos todos los caminos desde el nodo inicial hasta el nodo de destino

    # todos_caminos = nx.all_simple_paths(G, source=nodo_inicial, target=nodo_destino)

    # Creamos un diccionario para mapear los nodos y bordes de los caminos
    camino_nodes = set()
    camino_edges = set()
    for camino in caminos:
        for i in range(len(camino) - 1):
            camino_nodes.add(camino[i])
            camino_edges.add((camino[i], camino[i+1]))
        #print(camino)
        camino_nodes.add(camino[-1])  # Agregar el último nodo del camino


    # Colocar en el plano cada nodo para que sea un arbol Top-down
    posicion = nx.spring_layout(Grafo, seed=0)
    posicion_manual = {"APLICACION1": (0, 0), "LAN1": (0, -32), "APLICACION2": (0, -64), "LAN2": (0, -96), "INTERFAZ_IP1": (-4, -96), "APLICACION3": (-8, -96), "INTERFAZ_IP2": (-4, -128),  "INTERFAZ_IP3": (0, -128),  "INTERFAZ_IP4": (4, -128),  "APLICACION4": (12, -144),  "LAN3": (0, -160),  "INTERFAZ_IP5": (-4, -192),  "INTERFAZ_IP6": (0, -192),  "INTERFAZ_IP7": (4, -192),  "APLICACION5": (0, -224)}

    # Obtener el atributo direccion_ip de la arista
    etiquetas_aristas = nx.get_edge_attributes(Grafo, 'direccion_ip')

    fig = plt.figure(figsize=(15, 13))

    # draw graph
    nx.draw_networkx(Grafo, posicion, node_size=1200, node_color = "#0CA29B", font_size = 7)
    # draw edge attributes
    nx.draw_networkx_edge_labels(Grafo, posicion, edge_labels=etiquetas_aristas);

    nx.draw_networkx_nodes(Grafo, posicion, nodelist=camino_nodes, node_color='red', node_size=500)  # Superponemos los nodos de los caminos
    nx.draw_networkx_edges(Grafo, posicion, edgelist=camino_edges, edge_color='red', width=2)  # Superponemos los bordes de los caminos

    camino_nodes = [node for node, data in Grafo.nodes(data=True) if 'ip_forward' in data and data['ip_forward']]
    nx.draw_networkx_nodes(Grafo, posicion, nodelist=camino_nodes, node_color='pink', node_size=500)  # Superponemos los nodos de los caminos
    
    plt.show()
