import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l_list = ['hello', 'World']
lib.print_python_list_info(l_list)
del l_list[1]
lib.print_python_list_info(l_list)
l_list = l_list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l_list)
l_list = []
lib.print_python_list_info(l_list)
l_list.append(0)
lib.print_python_list_info(l_list)
l_list.append(1)
l_list.append(2)
l_list.append(3)
l_list.append(4)
lib.print_python_list_info(l_list)
l_list.pop()
lib.print_python_list_info(l_list)
