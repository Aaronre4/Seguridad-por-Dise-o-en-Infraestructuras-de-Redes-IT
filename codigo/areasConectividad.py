import networkx as nx
import matplotlib.pyplot as plt
import copy
import json

def areas(Grafo):

    G2 = Grafo.copy()
    posicion = nx.spring_layout(Grafo, seed=0)

    print("Que nivel de áreas quieres buscar")
    nivel = int(input())

    Conectados_router = [] # Lista de nodos vecinos a los routers

    for node, data in Grafo.nodes(data=True): # data=True: Este argumento opcional indica que quieres incluir los datos de los nodos en la vista devuelta.Al establecerlo en True, la vista contendrá tuplas (nodo, datos_del_nodo).
        #if 'ip_forward' in data and data['ip_forward']:
        if nivel == 2 and not data['nivel2']:
            vecinos = list(G2.neighbors(node))
            vecinos.insert(0,node) # Añadimos el nodo que vamos a quitar el inicio
            Conectados_router.append(vecinos) # Añado a la lista los nodos conectados al nodo que vamos a quitar
            #G2.remove_node(node)
        elif nivel == 3 and not data['nivel3']:
            vecinos = list(G2.neighbors(node))
            vecinos.insert(0,node) # Añadimos el nodo que vamos a quitar el inicio
            Conectados_router.append(vecinos) # Añado a la lista los nodos conectados al nodo que vamos a quitar
            #G2.remove_node(node)
        elif nivel == 4 and not data['nivel4']:
            vecinos = list(G2.neighbors(node))
            vecinos.insert(0,node) # Añadimos el nodo que vamos a quitar el inicio
            Conectados_router.append(vecinos) # Añado a la lista los nodos conectados al nodo que vamos a quitar
            #G2.remove_node(node)


    # Imprimir el nodo quitado y sus vecinos
    for lista in Conectados_router:  
        G2.remove_node(lista[0])
        print(f"Vecinos: {lista}")
    #           Resultado
    # Vecinos: ['APLICACION1', 'LAN1']
    # Vecinos: ['APLICACION2', 'LAN1', 'LAN2']

    # Encuentra los componentes conectados después de eliminar los nodos
    componentes_conectados = list(nx.connected_components(G2))

    # Crea subgrafos para cada componente conectado
    subgrafos = [G2.subgraph(componente) for componente in componentes_conectados]

    # draw graph
    # nx.draw_networkx(G2, posicion_manual, node_size=1200, node_color = "#0CA29B", font_size = 7)

    # Dibuja los subgrafos obtenidos
    plt.figure(figsize=(10, 5))
    for i, subgrafo in enumerate(subgrafos): # enumerate devuelve tanto el índice como el elemento correspondiente en cada iteración.
        subgrafo_editable = nx.Graph(subgrafo) # Crear un nuevo grafo editable
        for lista in Conectados_router:
            for elemento_lista in lista:
                for node in subgrafo.nodes:
                    #print(f"Subgrafo: {node}")
                    if node == elemento_lista:
                        subgrafo_editable.add_node(lista[0])
                        subgrafo_editable.add_edge(lista[0],node)
        plt.subplot(1, len(subgrafos), i+1)
        # if i == 1:
        #     G3 = subgrafo_editable
        # if i == 2:
        #     G4 = subgrafo_editable
        etiquetas_aristas_subgrafo = nx.get_edge_attributes(subgrafo_editable, 'direccion_ip')
        nx.draw_networkx(subgrafo_editable, posicion, node_size=900, node_color="#0CA29B", font_size=6, with_labels=True)
        plt.title(f"Subgrafo {i+1}")
    plt.ioff()
    plt.tight_layout()
    plt.show()