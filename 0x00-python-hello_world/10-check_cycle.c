#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - a function that checks
 * for cycles in a linked list using floyd's
 * cycle detection algorithm
 * @list: the head of the linked list
 * Return: int
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast;

	if (list)
		fast = slow->next;

	while (slow && fast->next)
	{
		if (fast == slow)
			return (1);

		if (fast->next)
			fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
