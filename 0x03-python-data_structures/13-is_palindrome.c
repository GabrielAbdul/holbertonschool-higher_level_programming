#include "lists.h"

/**
 * is_palindrome - function that returns 1 if n is a palindrome
 * otherwise return 0
 *
 * @head: head node
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	int list_len = rint_listint(*head);
	listint_t *node;
	int *result = malloc(sizeof(int) * list_len), i = 0;
	int start = 0, end = 0;

	node = *head;
	while (node)
	{
		result[i] = node->n;
		node = node->next;
		i++;
	}

	for (start = 0, end = list_len - 1; start < list_len / 2; start++, end--)
	{
		if (result[start] != result[end])
			return (0);
	}
	free(result);
	return (1);
}

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int rint_listint(listint_t *h)
{
	const listint_t *current;
	int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

