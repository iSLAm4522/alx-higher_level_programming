#include "lists.h"

/**
* is_palindrome_helper - Recursively checks if a linked list is a palindrome
* @front: Double pointer to the front of the list (updated during recursion)
* @current: Pointer to the current node being checked
*
* Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome_helper(listint_t **front, listint_t *current)
{
	int isPal;

	if (!current)
		return (1);

	isPal = is_palindrome_helper(front, current->next);

	if (!isPal || (*front)->n != current->n)
		return (0);

	*front = (*front)->next;
	return (1);
}

/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: Double pointer to the head of the list
*
* Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	return (is_palindrome_helper(head, *head));
}
