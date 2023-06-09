#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - a function that checks
 * if a singly-linked list is a palindrome
 * @head: the address of the head node
 * Return: int
 **/
int is_palindrome(listint_t **head)
{
	listint_t **check_list = NULL, *current = *head;
	int i = 0, length, j = 0;

	if (!*head)
		return (1);
	check_list = malloc(1024 * sizeof(listint_t *));
	length = 1024;
	while (current)
	{
		if (i >= length)
		{
			length += 120;
			check_list = realloc(check_list, length * sizeof(listint_t *));
		}
		check_list[i++] = current;
		current = current->next;
	}
	for (; j < (i / 2); j++)
	{
		if ((check_list[j])->n != (check_list[i - 1 - j])->n)
			break;
	}
	if (j >= (i / 2))
	{
		free(check_list);
		return (1);
	}
	return(0);
}
