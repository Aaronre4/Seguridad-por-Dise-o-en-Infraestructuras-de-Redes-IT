import networkx as nx
import matplotlib.pyplot as plt
import copy
import json

def DatosCodigo(Grafo):

    #G = nx.Graph()
    #pos = nx.tree_layout(G)

    # Vamos a hacer que la aplicacion3 y la aplicacion4 si puedan hacer de gateway de nivel3 y el interfaz_ip2 no lo sea

    Grafo.add_node("APLICACION1", ip_forward=True, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("LAN1", rango="10.68.1.0", nivel2=True, nivel3=True, nivel4=True)
    Grafo.add_node("APLICACION2", ip_forward=True, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("LAN2", rango="10.68.2.0", nivel2=True, nivel3=False, nivel4=True)
    Grafo.add_node("INTERFAZ_IP1", nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("INTERFAZ_IP2", nivel2=False, nivel3=False, nivel4=True)
    Grafo.add_node("INTERFAZ_IP3", nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("INTERFAZ_IP4", nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("APLICACION3", ip_forward=False, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("APLICACION5", ip_forward=False, nivel2=False, nivel3=False, nivel4=True)
    Grafo.add_node("LAN3", rango="10.68.3.0", nivel2=True, nivel3=True, nivel4=True)
    Grafo.add_node("INTERFAZ_IP5", ip_forward=False, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("INTERFAZ_IP6", ip_forward=False, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("INTERFAZ_IP7", ip_forward=False, nivel2=False, nivel3=True, nivel4=True)
    Grafo.add_node("APLICACION4", nivel2=False, nivel3=True, nivel4=True)


    Grafo.add_edge("APLICACION1","LAN1", direccion_ip = "10.68.1.1")
    Grafo.add_edge("LAN1","APLICACION2", direccion_ip = "10.68.2.1")
    Grafo.add_edge("APLICACION2","LAN2", direccion_ip = "10.68.2.2")
    Grafo.add_edge("LAN2","INTERFAZ_IP1", direccion_ip = "10.68.2.3")
    Grafo.add_edge("LAN2","INTERFAZ_IP2", direccion_ip = "10.68.2.4")
    Grafo.add_edge("LAN2","INTERFAZ_IP3", direccion_ip = "10.68.2.5")
    Grafo.add_edge("LAN2","INTERFAZ_IP4", direccion_ip = "10.68.2.6")
    Grafo.add_edge("APLICACION3","INTERFAZ_IP1")
    Grafo.add_edge("APLICACION4","INTERFAZ_IP2")
    Grafo.add_edge("APLICACION4","INTERFAZ_IP3")
    Grafo.add_edge("APLICACION4","INTERFAZ_IP4")
    Grafo.add_edge("INTERFAZ_IP2","LAN3", direccion_ip = "10.68.3.1")
    Grafo.add_edge("INTERFAZ_IP3","LAN3", direccion_ip = "10.68.3.2")
    Grafo.add_edge("INTERFAZ_IP4","LAN3", direccion_ip = "10.68.3.3")
    Grafo.add_edge("LAN3","INTERFAZ_IP5", direccion_ip = "10.68.3.4")
    Grafo.add_edge("LAN3","INTERFAZ_IP6", direccion_ip = "10.68.3.5")
    Grafo.add_edge("LAN3","INTERFAZ_IP7", direccion_ip = "10.68.3.6")
    Grafo.add_edge("APLICACION5","INTERFAZ_IP5")
    Grafo.add_edge("APLICACION5","INTERFAZ_IP6")
    Grafo.add_edge("APLICACION5","INTERFAZ_IP7")
    
    plt.ion()
    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(Grafo, seed=0)  # Posición de los nodos para la visualización
    nx.draw(Grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
    plt.show()