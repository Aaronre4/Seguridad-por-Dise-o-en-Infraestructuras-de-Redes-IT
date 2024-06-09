import networkx as nx
import matplotlib.pyplot as plt
import copy
import json

def DatosJSON(Grafo):

    with open('./assets/nodos_aristas.json', 'r') as f:
        data = json.load(f)

    # Crear un grafo
    # G = nx.Graph()

    # Añadir nodos con atributos
    for node in data['nodes']:
        Grafo.add_node(node['id'], **{k: v for k, v in node.items() if k != 'id'})

    # Añadir aristas
    for edge in data['edges']:
        Grafo.add_edge(edge['source'], edge['target'])


    print("De los siguientes nodos cuales son routers('fin' para terminar): ")

    for node in Grafo.nodes():
        if node.startswith("APLICACION"):
            print(node)

    while True:
        dato = input()

        if dato.lower() == 'fin':
            break

        if dato in Grafo.nodes():
            Grafo.nodes[dato]['ip_forward'] = True

    for node,atributos in Grafo.nodes(data=True):
        if atributos.get('ip_forward') is True:
            Grafo.nodes[node]['nivel2'] = False
            Grafo.nodes[node]['nivel3'] = True
            Grafo.nodes[node]['nivel4'] = True
        
        if node.startswith("APLICACION") and 'ip_forward' not in atributos:
            Grafo.nodes[node]['ip_forward'] = False
            Grafo.nodes[node]['nivel2'] = False
            Grafo.nodes[node]['nivel3'] = False
            Grafo.nodes[node]['nivel4'] = True

        if node.startswith("LAN"):
            Grafo.nodes[node]['nivel2'] = True
            Grafo.nodes[node]['nivel3'] = True
            Grafo.nodes[node]['nivel4'] = True

        if node.startswith("INTERFAZ_IP"):
            Grafo.nodes[node]['nivel2'] = False
            Grafo.nodes[node]['nivel3'] = True
            Grafo.nodes[node]['nivel4'] = True
            
    # Dibujar el grafo para verificar que se ha creado correctamente
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(Grafo)  # Posición de los nodos para la visualización
    nx.draw(Grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
    plt.show()