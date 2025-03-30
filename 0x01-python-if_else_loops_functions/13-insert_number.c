#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly linked list
* @head: Double pointer to the head of the list
* @number: The number to insert
* Return: Address of the new node, or NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = NULL;
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	prev->next = newNode;
	newNode->next = current;

	return (newNode);
}
