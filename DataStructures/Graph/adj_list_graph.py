from DataStructures.Lists import array_list as lt 
from DataStructures.Map import map_linear_probing as mp
from . import edge as e

def new_graph(size=15, directed=False):
    """
    Crea un grafo vacío.
    
    El grafo tiene los siguientes atributos:
    - vertices: Mapa que almacena los vértices y sus listas de adyacencia (usando map_linear_probing)
    - information: Mapa que almacena la información de los vértices (usando map_linear_probing)
    - edges: Número de aristas en el grafo (inicializado en 0)
    - directed: Indica si el grafo es dirigido
    - type: Tipo de implementación (inicializado en 'ADJ_LIST')
    - in_degree: Mapa que almacena los grados de entrada de los vértices (solo para grafos dirigidos)
    
    Args:
        size (int): Capacidad inicial de los mapas (por defecto=15)
        directed (bool): Indica si el grafo es dirigido (por defecto=False)
    
    Returns:
        dict: El grafo vacío recién creado
    """
    graph = {
        'vertices': mp.new_map(size, 0.5),      # Mapa para almacenar vértices y listas de adyacencia
        'information': mp.new_map(size, 0.5),   # Mapa para almacenar información de los vértices  
        'edges': 0,                              # Contador de aristas
        'directed': directed,                    # Indica si el grafo es dirigido
        'type': 'ADJ_LIST',                      # Tipo de implementación
        'in_degree': None if not directed else mp.new_map(size, 0.5)  # Grados de entrada para grafos dirigidos
    }
    return graph

def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo.
    Para grafos no dirigidos, cada arco aparece una sola vez.
    
    Args:
        graph (adj_list_graph): El grafo sobre el que se ejecuta la operacion
        
    Returns:
        array_list: La lista con los arcos del grafo
    """
    # Crear una nueva lista para almacenar los arcos
    edges_list = lt.new_list()
    
    # Obtener la lista de vértices
    vertex_list = vertices(graph)
    
    # Para cada vértice
    for i in range(lt.size(vertex_list)):
        vertex = lt.get_element(vertex_list, i)
        
        # Obtener su lista de adyacencia
        adj_list = mp.get(graph['vertices'], vertex)
        
        # Para cada arco en la lista de adyacencia
        for j in range(lt.size(adj_list)):
            edge = lt.get_element(adj_list, j)
            
            # Si el grafo no es dirigido, solo agregar el arco si vertex_a <= vertex_b
            # para evitar duplicados
            if not graph['directed']:
                if e.either(edge) <= e.other(edge, e.either(edge)):
                    lt.add_last(edges_list, edge)
            else:
                lt.add_last(edges_list, edge)
                    
    return edges_list

def add_edge(graph, vertex_a, vertex_b, weight=0):
    """
    Agrega un arco al grafo entre los vértices vertex_a y vertex_b con peso weight.
    
    Args:
        graph (dict): El grafo al cual agregar el arco
        vertex_a (any): Vértice de inicio
        vertex_b (any): Vértice destino
        weight (float): Peso del arco (default=0)
    
    Returns:
        dict: El grafo actualizado
    """
    # Verificar si ambos vértices existen
    if not (mp.contains(graph['vertices'], vertex_a) and 
            mp.contains(graph['vertices'], vertex_b)):
        return graph

    # Crear el nuevo arco
    new_edge = e.new_edge(vertex_a, vertex_b, weight)
    
    # Obtener la lista de adyacencia del vértice a
    adj_list_a = mp.get(graph['vertices'], vertex_a)
    
    # Verificar si el arco ya existe
    edge_found = False
    for i in range(lt.size(adj_list_a)):
        edge = lt.get_element(adj_list_a, i)
        if (e.either(edge) == vertex_a and e.other(edge, vertex_a) == vertex_b):
            lt.change_info(adj_list_a, i, new_edge)
            edge_found = True
            break
    
    # Si el arco no existe, agregarlo
    if not edge_found:
        lt.add_last(adj_list_a, new_edge)
        graph['edges'] += 1
        
        # Si el grafo es no dirigido, agregar el arco en la otra dirección
        if not graph['directed']:
            adj_list_b = mp.get(graph['vertices'], vertex_b)
            reverse_edge = e.new_edge(vertex_b, vertex_a, weight)
            lt.add_last(adj_list_b, reverse_edge)
    return graph

def num_edges(graph):
    """
    Retorna el numero de arcos en el grafo.
    
    Args:
        graph (adj_list_graph): El grafo sobre el que se ejecuta la operacion.
    
    Returns:
        int: El numero de arcos del grafo.
    """
    return graph['edges']

def insert_vertex(graph, key_vertex, info_vertex):
    """
    Inserta un nuevo vértice en el grafo si no existe ya.
    
    Crea una lista de adyacencia vacía para el nuevo vértice y almacena su información.
    Para grafos dirigidos, inicializa el contador de grados de entrada en 0.
    
    Args:
        graph (dict): El grafo en el que se insertará el vértice
        key_vertex (any): Clave del vértice a insertar
        info_vertex (any): Información a asociar con el vértice
    
    Returns:
        dict: El grafo actualizado
    """
    # Verifica si el vértice ya existe
    if not mp.contains(graph['vertices'], key_vertex):
        # Crea una lista de adyacencia vacía para el nuevo vértice
        adj_list = lt.new_list()
        
        # Agrega el vértice y su lista de adyacencia al mapa de vértices
        mp.put(graph['vertices'], key_vertex, adj_list)
        
        # Agrega la información del vértice
        mp.put(graph['information'], key_vertex, info_vertex)
        
        # Inicializa el grado de entrada para grafos dirigidos
        if graph['directed'] and graph['in_degree'] is not None:
            mp.put(graph['in_degree'], key_vertex, 0)
    
    return

def vertices(graph):
    """
    Retorna una lista con todos los vertices del grafo
    
    Args:
        graph (adj_list_graph): El grafo sobre el que se ejecuta la operacion
        
    Returns:
        array_list: La lista con los vertices del grafo
    """
    # Obtener el conjunto de llaves (vértices) del mapa de vértices
    vertex_keys = mp.key_set(graph['vertices'])
    
    return vertex_keys

def num_vertices(graph):
    """
    Retorna el numero de vertices en el grafo.
    
    Args:
        graph (adj_list_graph): El grafo sobre el que se ejecuta la operacion.
    
    Returns:
        array_list: La lista con los vertices del grafo
    """
        
    return lt.size(vertices(graph))

def degree(graph, key_vertex):
    """
    Retorna el número de arcos asociados al vértice "key_vertex".

    Parámetros:
    graph (dict): La representación del grafo en forma de lista de adyacencia.
    key_vertex (any): El vértice del que se desea conocer el grado.

    Retorna:
    int: Grado del vértice.
    """
    #Verifica si -> vértice existe en mapa de vértices
    if mp.contains(graph['vertices'], key_vertex):
        #Obtiene -> lista  adyacencia del vértice key_vertex
        adj_list = mp.get(graph['vertices'], key_vertex)
        #Retorna -> tamaño lista de adyacencia como el grado del vértice
        return lt.size(adj_list)
    # Retorna None si -> vértice no está en el grafo
    return None

def in_degree(graph, key_vertex):
    """
    Retorna el número de arcos que llegan al vértice 'key_vertex'.
    
    Args:
        graph (adj_list_graph): El grafo sobre el que se ejecuta la operación.
        key_vertex (any): El vértice del que se desea conocer el grado de entrada.
    
    Returns:
        int: El grado de entrada del vértice.
    """
    #Verificar si -> vértice existe
    if not mp.contains(graph['vertices'], key_vertex):
        return None
    
    #Contador -> grado entrada
    contador_grado = 0

    #Recorrer -> vértices grafo
    vertex_list = vertices(graph)
    for i in range(lt.size(vertex_list)):
        vertex = lt.get_element(vertex_list, i)
        
        #Obtener -> lista adyacencia de cada vértice
        adj_list = mp.get(graph['vertices'], vertex)
        
        #Contar -> aristas que apuntan a key_vertex
        for j in range(lt.size(adj_list)):
            edge = lt.get_element(adj_list, j)
            if e.other(edge, vertex) == key_vertex: 
                contador_grado += 1
                
    return contador_grado