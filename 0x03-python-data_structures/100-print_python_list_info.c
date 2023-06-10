#include <Python.h>
#include <stdio.h>

/*
 * print_python_list_info - print and modifypy list in c
 * @p: PyObject *parameter
 * Return: NULL
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;
	PyListObject *ll;
	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d", alloc);

	for (i = 0; i <= size - 1; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		ll = (PyListObject *)obj;
		printf("%s\n", ll->ob_base.ob_base.ob_type);
	} 
}
