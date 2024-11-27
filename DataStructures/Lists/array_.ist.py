def new_list():
    """Inicializa una nueva lista.

    Returns:
        array_list: Un objeto array_list que representa la lista vacía.
    """

    return {'elements': [],
            'size': 0,
            }

def size(my_list):
    """Obtiene el tamaño de la lista.

    Args:
        my_list (array_list): La lista de la cual obtener el tamaño.

    Returns:
        int: El tamaño de la lista.
    """
    return my_list["size"]

def is_present(my_list, element, cmp_function):
    """Verifica si un elemento está presente en la lista usando una función de comparación.

    Args:
        my_list (array_list): La lista en la cual buscar.
        element (Any): El elemento a buscar.
        cmp_function (function): La función de comparación a usar.

    Returns:
        int: La posición del elemento si se encuentra, de lo contrario -1.
    """
    size = my_list['size']
    if size > 0:
        for key_pos in range(size):
            info = my_list['elements'][key_pos]
            if cmp_function(element, info) == 0:
                return key_pos
    return -1

def get_element(my_list, pos):
    """Obtiene un elemento de la lista en una posición específica.

    Args:
        my_list (array_list): La lista de la cual obtener el elemento.
        pos (int): La posición del elemento a recuperar contando desde cero.

    Returns:
        Any: El elemento en la posición especificada.

    """
    return my_list['elements'][pos]

def first_element(my_list):
    """Obtiene el primer elemento de la lista.

    Args:
        my_list (array_list): La lista de la cual obtener el primer elemento.

    Returns:
        Any: El primer elemento de la lista.

    """
    return get_element(my_list, 0)

def last_element(my_list):
    """Retorna el último elemento de una lista no vacía. Esta función NO elimina el elemento de la lista.

    Args:
        my_list (array_list): La lista a examinar.

    Returns:
        any: Último elemento de la lista.

    """
    return get_element(my_list, my_list['size'] - 1)

def insert_element(my_list, element, pos):
    """Inserta un elemento en una posición específica en la lista.

    Args:
        my_list (array_list): La lista en la cual insertar el elemento.
        element (Any): El elemento a insertar.
        pos (int): La posición en la cual insertar el elemento contando desde cero.

    Returns:
        array_list: La lista actualizada.

    """
    
    # Verificar la posición permitida para inserción utilizando check_position con pos
    if pos < 0 or pos > my_list['size']:
        return my_list
    
    # Insertar el elemento en la posición indicada
    my_list['elements'].insert(pos, element)
    
     # Incrementar el tamaño de la lista
    my_list['size'] += 1
    
    
    return my_list


def add_first(my_list, element):
    """Añade un elemento al principio de la lista.

    Args:
        my_list (array_list): La lista a la cual añadir el elemento.
        element (Any): El elemento a añadir.

    Returns:
        array_list: La lista actualizada.
    """
    return insert_element(my_list, element, 0)

def add_last(my_list, element):
    """Añade un elemento al final de la lista.

    Args:
        my_list (array_list): La lista a la cual añadir el elemento.
        element (Any): El elemento a añadir.

    Returns:
        array_list: La lista actualizada.
    """
    return insert_element(my_list, element , my_list['size'])

def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en una posición específica.

    Args:
        my_list (array_list): La lista que contiene el elemento.
        pos (int): La posición del elemento a cambiar, contando desde cero.
        new_info (Any): La nueva información a establecer.

    Returns:
        array_list: La lista actualizada.

    """
    if pos < 0 or pos >= my_list['size']:
        return my_list
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    """
    Intercambia los elementos en dos posiciones en la lista.

    Args:
        my_list (array_list): La lista que contiene los elementos.
        pos1 (int): La posición del primer elemento, contando desde cero.
        pos2 (int): La posición del segundo elemento, contando desde cero.

    Returns:
        array_list: La lista actualizada.

    """
    if pos1 < 0 or pos1 >= my_list['size'] or pos2 < 0 or pos2 >= my_list['size']:
        return my_list
    temp = my_list['elements'][pos1]
    my_list = change_info(my_list, pos1, my_list['elements'][pos2])
    my_list = change_info(my_list, pos2, temp)
    
    return my_list

def sub_list(my_list, pos, numelem):
    """Devuelve una sublista comenzando desde una posición con un número específico de elementos.

    Args:
        my_list (array_list): La lista de la cual obtener la sublista.
        pos (int): La posición inicial de la sublista, contando desde cero.
        numelem (int): El número de elementos en la sublista.

    Returns:
        array_list: La sublista creada.

    """
    if pos < 0 or pos >= my_list['size'] or numelem < 0:
        return None
    
    end_pos = min(pos + numelem, my_list['size'])
        
    # Obtener la sublista
    sub_elements = my_list['elements'][pos:end_pos]
    
    # Crear la nueva sublista
    sub_list = new_list()
    sub_list['elements'] = sub_elements
    sub_list['size'] = numelem
    
    return sub_list


def compare_elements(my_list, element, info, cmp_function=None):
    """
    Compara el elemento `element` con el elemento `info` de la lista `my_list`.
    
    Args:
        my_list (array_list): La lista que contiene los elementos.
        element (Any): El elemento que se está comparando.
        info (Any): El elemento de la lista con el que se compara.
        cmp_function (function, optional): Función de comparación personalizada.
    
    Returns:
        int: 0 si los elementos son iguales, 1 si element > info, -1 si element < info.
    """
    if cmp_function is None:
        cmp_function = default_function
    
    if my_list['size'] > 0:
        for key_pos in range(my_list['size']):
            if my_list['elements'][key_pos] == info:
                return cmp_function(element, info)
    
    # Si no se encuentra info en la lista, aún comparamos element e info
    return cmp_function(element, info)

def default_function(id1, id2):
    """
    Función de comparación por defecto.

    Args:
    id1 (any): El primer elemento a comparar
    id2 (any): El segundo elemento a comparar

    Returns:
    int: 0 si los elementos son iguales, 1 si id1 > id2, -1 si id1 < id2
    """
    if id1 == id2:
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1




def selection_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Slection Sort**

        Se recorre la lista y se selecciona el elemento más pequeño
        y se intercambia con el primer elemento de la lista.
        Se repite el proceso con el segundo elemento más pequeño y así sucesivamente.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list
    """

    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            minimum = pos1    # minimun tiene el menor elemento
            pos2 = pos1 + 1
            while (pos2 < n):
                if (sort_crit(get_element(my_list, pos2),
                (get_element(my_list, minimum)))):
                    minimum = pos2  # minimum = posición elemento más pequeño
                pos2 += 1
            if minimum != pos1:
                exchange(my_list, pos1, minimum)  # elemento más pequeño -> elem pos1
            pos1 += 1
    return my_list

def insertion_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Insertion Sort**

        Se recorre la lista y se inserta el elemento en la posición correcta
        en la lista ordenada.
        Se repite el proceso hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            pos2 = pos1
            while (pos2 > 0) and (sort_crit(
                get_element(my_list, pos2), get_element(my_list, pos2-1))):
                exchange(my_list, pos2, pos2-1)
                pos2 -= 1
            pos1 += 1
    return my_list

def shell_sort(my_list, sort_crit):

    """ Función de ordenamiento que implementa el algoritmo de **Shell Sort**
        Se recorre la lista y se ordena los elementos con un gap determinado.
        Se repite el proceso con un gap menor hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        h = 1
        while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
            h = 3*h + 1
        while (h >= 1):
            for i in range(h, n):
                j = i
                while (j >= h) and sort_crit(
                                    get_element(my_list, j),
                                    get_element(my_list, j-h)):
                    exchange(my_list, j, j-h)
                    j -= h
            h //= 3    # h se decrementa en un tercio
    return my_list

def merge_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Merge Sort**

        Se divide la lista en dos partes, se ordenan las partes y se combinan
        las partes ordenadas.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

    """
    n = size(my_list)
    if n > 1:
        mid = (n // 2)
        #se divide la lista original, en dos partes, izquierda y derecha, desde el punto mid.
        left_list = sub_list(my_list, 0, mid)
        right_list = sub_list(my_list, mid, n - mid)

        #se hace el llamado recursivo con la lista izquierda y derecha 
        merge_sort(left_list, sort_crit)
        merge_sort(right_list, sort_crit)

        #i recorre la lista izquierda, j la derecha y k la lista original
        i = j = k = 0

        left_elements = size(left_list)
        righ_telements = size(right_list)

        while (i < left_elements) and (j < righ_telements):
            elem_i = get_element(left_list, i)
            elem_j = get_element(right_list, j)
            # compara y ordena los elementos
            if sort_crit(elem_j, elem_i):   # caso estricto elem_j < elem_i
                change_info(my_list, k, elem_j)
                j += 1
            else:                            # caso elem_i <= elem_j
                change_info(my_list, k, elem_i)
                i += 1
            k += 1

        # Agrega los elementos que no se comprararon y estan ordenados
        while i < left_elements:
            change_info(my_list, k, get_element(left_list, i))
            i += 1
            k += 1

        while j < righ_telements:
            change_info(my_list, k, get_element(right_list, j))
            j += 1
            k += 1
    return my_list

def quick_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Quick Sort**

        Se selecciona un elemento como **pivot** y se ordenan los elementos

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

    """
    quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lo, hi, sort_crit):
    """ Función recursiva que implementa el algoritmo de **quick sort**, esta es llamada por la función ``quick_sort()``

        Se localiza el **pivot**, utilizando la funcion de particion.

        Luego se hace la recursión con los elementos a la izquierda del **pivot**
        y los elementos a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function
    """
    if (lo >= hi):
        return
    pivot = partition(my_list, lo, hi, sort_crit)
    quick_sort_recursive(my_list, lo, pivot-1, sort_crit)
    quick_sort_recursive(my_list, pivot+1, hi, sort_crit)

def partition(my_list, lo, hi, sort_crit):

    """ Función que implementa la partición de la lista en **quick sort**, esta es llamada por la función ``quick_sort_recursive()``

        Se selecciona un **pivot** y se ordenan los elementos menores a la izquierda del **pivot**
        y los elementos mayores a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: array_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Posición del **pivot**
        :rtype: int
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           get_element(my_list, leader), get_element(my_list, hi)):
            exchange(my_list, follower, leader)
            follower += 1
        leader += 1
    exchange(my_list, follower, hi)
    return follower

def default_sort_criteria(element1, element2):
    """ Función de comparación por defecto para ordenar de manera ascendente.

        Compara dos elementos y retorna ``True`` si el primer elemento es menor al segundo elemento.

        :param element1: Elemento 1
        :type element1: any
        :param element2: Elemento 2
        :type element2: any

        :returns: ``True`` si el primer elemento es menor al segundo elemento, ``False`` en caso contrario
        :rtype: bool
    """
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted