#include "lists.h"
/**
 * check_cycle - Function that checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 * Return: If there is no cycle - 0 and - 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *lagging, *speeder;

	if (list == NULL || list->next == NULL)
		return (0);

	lagging = list->next;
	speeder = list->next->next;

	while (lagging && speeder && speeder->next)
	{
		if (lagging == speeder)
			return (1);

		lagging = lagging->next;
		speeder = speeder->next->next;
	}

	return (0);
}
