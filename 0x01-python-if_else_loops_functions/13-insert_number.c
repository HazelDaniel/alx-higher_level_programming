#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - a function that inserts a node
 * at an appropriate position in a sorted
 * linked list
 * @head: the address of the head node
 * @number: the value of the node to be inserted
 * Return: listint_t *
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev  = NULL;
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	new_node->n = number;
	new_node->next = NULL;

	if (!current)
	{
		*head = new_node;
		return (new_node);
	}

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev)
		prev->next = new_node;
	else
		*head = new_node;
	new_node->next = current;
	return (new_node);
}
