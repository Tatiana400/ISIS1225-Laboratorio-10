from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Lists import array_list as lt

def new_map(num_elements, load_factor, prime=109345121): 
    """
    Crea una tabla de símbolos (map) sin elementos.

    Parameters:
    num_elements (int): Número de parejas <key,value> que inicialmente puede almacenar la tabla
    load_factor (float): Factor de carga máximo de la tabla
    prime (int): Número primo utilizado en la función hash. Se utiliza 109345121 por defecto

    Returns:
    map_linear_probing: Un nuevo map
    """
    # Calcular la capacidad (siguiente número primo mayor a num_elements/load_factor)
    capacity = mf.next_prime(int(num_elements / load_factor))

    # Crear una lista vacía de tamaño capacity
    table = lt.new_list()
    for _ in range(capacity):
        lt.add_last(table, None)

    # Generar números aleatorios para scale y shift
    import random
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)

    # Crear el mapa
    map_struct = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0,
        'type': 'PROBING'
    }

    return map_struct

EMPTY_ENTRY = me.new_map_entry('__EMPTY__', '__EMPTY__')

def contains(my_map, key, return_position=False):
    """
    Verifica si una llave está en el map. Si se solicita, retorna la posición de la llave en la tabla.

    Args:
        my_map (map_linear_probing): map a examinar
        key (any): La llave asociada a la pareja
        return_position (bool, optional): Indica si se debe retornar la posición de la llave en la tabla
    Returns:
        (bool): True si la llave está en el map
    """
    capacity = my_map['capacity']
    posicion_i = mf.hash_value(my_map, key)
    entry = lt.get_element(my_map['table'], posicion_i)
    
    # Mientras la casilla no esté vacía
    while (entry is not None):
        llave = me.get_key(entry)
        if llave == key:
            if return_position:
                return True, posicion_i  # Retorna True y la posición si se solicita
            return True
        
        # Avanza al siguiente índice en la tabla de manera circular
        posicion_i = (posicion_i + 1) % capacity
        entry = lt.get_element(my_map["table"], posicion_i)
    
    if return_position:
        return False, -1  # Si no se encuentra la llave, retorna False y -1 como posición
    return False


def get(my_map, key): 
    """
    Retorna el valor asociado a la llave en el map. Si la llave no existe, retorna None.

    Args:
        my_map (map_linear_probing): map a examinar
        key (any): La llave asociada a la pareja

    Returns:
        Valor asociado a la llave o None si la llave no existe
    """
    posicion_i = mf.hash_value(my_map, key)
    capacity = my_map['capacity']
    start_pos = posicion_i  # Guardar la posición inicial para detectar ciclos

    while True:
        entry = lt.get_element(my_map['table'], posicion_i)
        
        # Si encontramos un EMPTY_ENTRY, la llave no existe
        if entry == EMPTY_ENTRY:
            return None
            
        # Si la entrada tiene un valor, comparamos la llave
        if entry is not None:
            llave = me.get_key(entry)
            if llave == key:
                return me.get_value(entry)
        
        # Avanza al siguiente índice en la tabla de manera circular
        posicion_i = (posicion_i + 1) % capacity
        if posicion_i == start_pos:  # Si volvemos a la posición inicial, terminamos la búsqueda
            return None
    

def size(my_map): 
    """Retorna el número de parejas llave-valor en el map

    Args:
        my_map (map_linear_probing): Map a examinar
    
    Returns:
        int: Número de parejas llave-valor en el map
    """
    return my_map["size"]    
    
 
def is_empty(my_map): 
    """Indica si el map se encuentra vacío

    Args:
        my_map (map_linear_probing): Map a examinar
    
    Returns:
        bool: True si el map está vacío
              False si el map no está vacío
    """
    if my_map["size"] == 0:
        return True  
    
    return False
    
def key_set(my_map):
    """Retorna una lista con todas las llaves de la tabla de hash

    Args:
        my_map (map_linear_probing): Map a examinar
    
    Returns:
        array_list: Lista de llaves
    """
    llaves = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"], i)
        
        if entry is not None and entry != EMPTY_ENTRY:  # Asegurarse de que no es una posición vacía o eliminada
            llave = me.get_key(entry)
            lt.add_last(llaves, llave)
            
    return llaves

def value_set(my_map):
    """Retorna una lista con todos los valores de la tabla hash

    Args:
        my_map (map_linear_probing): Map a examinar
        
    Returns:
        array_list: Lista de valores
    """
    valores = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"], i)
        
        if entry is not None and entry !=EMPTY_ENTRY:  # Asegurarse de que no es una posición vacía o eliminada
            valor = me.get_value(entry)
            lt.add_last(valores, valor)
            
    return valores
 
def find_slot(my_map, key, hash_value):
    table = my_map['table']
    capacity = my_map['capacity']

    while True:
        if is_available(table, hash_value):
            return False, hash_value
        entry = lt.get_element(table, hash_value)
        if me.get_key(entry) == key:
            return True, hash_value
        hash_value = (hash_value + 1) % capacity  # Asegurar que el índice esté dentro del rango
        
def is_available(table, pos):
    """Informa si la posición pos está disponible en la tabla de hash
    Se entiende que una posición está disponible si su contenido es igual a None (no se ha
    usado esa posición) o a _EMPTY_ (la posición fue liberada)
    """
    if pos >= lt.size(table):  # Asegurar que el índice esté dentro del rango
        return False
    entry = lt.get_element(table, pos)
    return entry is None or entry == EMPTY_ENTRY
   
def rehash(my_map):
    """Hace rehash de todos los elementos de la tabla de hash.
    Incrementa la capacidad de la tabla y rehash todos los elementos.
    
    Args:
        my_map (map_linear_probing): Map a hacer rehash
    
    Returns:
        map_linear_probing: Map con la nueva capacidad
    """
    # Calculamos el nuevo tamaño considerando el factor de carga
    new_size = my_map['size'] * 2  # Duplicamos el número de elementos actual
    
    # Crear un nuevo mapa con la capacidad correcta basada en el factor de carga
    rehashed_map = new_map(new_size, my_map['limit_factor'], my_map['prime'])
    
    # Reinsertar los elementos en la nueva tabla
    for i in range(lt.size(my_map['table'])):
        entry = lt.get_element(my_map['table'], i)
        if entry not in (None, EMPTY_ENTRY):
            key = me.get_key(entry)
            value = me.get_value(entry)

            hash_value = mf.hash_value(rehashed_map, key)
            finded, pos = find_slot(rehashed_map, key, hash_value)
            new_entry = me.new_map_entry(key, value)
            lt.change_info(rehashed_map['table'], pos, new_entry)
            rehashed_map['size'] += 1
    
    # Actualizar el mapa original con las propiedades del rehashed_map
    my_map.update(rehashed_map)
    
    return my_map

def put(my_map, key, value):
    """Ingresa una pareja llave-valor a la tabla de hash. Si la
    llave ya existe, se reemplaza el valor.
    Args:
        my_map (map_linear_probing): El mapa donde se guarda la pareja llave-valor
        key (any): La llave asociada a la pareja
        value (any): El valor asociado a la pareja
    
    Returns:
        map_linear_probing: El mapa modificado
    """
    hash_value = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_value)
    
    if found:
        # Si la llave existe, solo actualizamos el valor
        entry = lt.get_element(my_map['table'], pos)
        me.set_value(entry, value)
    else:
        # Verificar si necesitamos hacer rehash antes de insertar el nuevo elemento
        current_load = my_map['size'] / my_map['capacity']
        needs_rehash = (current_load + (1/my_map['capacity'])) > my_map['limit_factor']
        
        if needs_rehash:
            my_map = rehash(my_map)
            # Recalcular la posición después del rehash
            hash_value = mf.hash_value(my_map, key)
            found, pos = find_slot(my_map, key, hash_value)
        
        # Insertar el nuevo elemento
        new_entry = me.new_map_entry(key, value)
        lt.change_info(my_map['table'], pos, new_entry)
        my_map['size'] += 1
        
    return my_map

def remove(my_map, key):
    """Elimina la pareja llave-valor del mapa, si existe.

    Args:
        my_map (map_linear_probing): Mapa donde se va a eliminar la pareja.
        key (any): Llave a eliminar.

    Returns:
        map_linear_probing: Mapa con la pareja eliminada o sin cambios si no se encuentra la llave.
    """
    # Manejar el caso de un mapa vacío
    if my_map['size'] == 0:
        return my_map  # No hacer nada si el mapa está vacío
    
    found, pos = contains(my_map, key, return_position=True)  # Verifica si la llave está en el mapa y obtiene la posición
    
    if found:
        # Marcar la posición como vacía
        lt.change_info(my_map['table'], pos, EMPTY_ENTRY)
        my_map['size'] -= 1  # Reducir el tamaño del mapa
    # Si no se encuentra la llave, no se hace nada, el tamaño permanece igual

    return my_map

def default_compare(key, element):
    """Función de comparación por defecto. Compara una llave con la llave de un
    elemento llave-valor

    Args:
        key (any): Llave a comparar
        element (map_entry): entry a comparar
    
    Returns:
        int: 0 si son iguales, 1 si key > la llave del elemento,
            -1 si key < que la llave del elemento
    """
    element_key = me.get_key(element)

    # Comparación entre llave (key) y llave del elemento
    if key == element_key:
        return 0  # Si las llaves son iguales
    elif key > element_key:
        return 1  # Si la llave (key) es mayor que la llave del elemento
    else:
        return -1  # Si la llave (key) es menor que la llave del elemento   