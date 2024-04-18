#include "lists.h"
/**
 * insert_node - Function that inserts node in an organised linked
 * list.
 * @head: Head of the list.
 * @number: Node data.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}
	ptr = *head;
	while (ptr->next != NULL)
	{
		if ((ptr->next)->n > number)
		{
			temp->next = ptr->next;
			ptr->next = temp;
			return (temp);
		}
		ptr = ptr->next;
	}
	temp->next = NULL;
	ptr->next = temp;
	return (temp);
}
