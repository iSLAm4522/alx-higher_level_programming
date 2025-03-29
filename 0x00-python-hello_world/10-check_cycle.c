#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 * Return: 1 if a cycle is found, 0 if no cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *slow_ptr = list, *fast_ptr = list;

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        if (slow_ptr == fast_ptr)
            return (1);
    }
    return (0);
}
