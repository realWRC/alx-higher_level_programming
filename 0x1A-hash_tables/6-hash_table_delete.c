#include "hash_tables.h"
/**
 * hash_table_delete - Function that frees and deletes
 * a hash table.
 * @ht: Hash table pointer.
 */
void hash_table_delete(hash_table_t *ht)
{
	hash_node_t *cur_node, *temp;
	hash_table_t *head = ht;
	unsigned long int x;

	for (x = 0; x < ht->size; x++)
	{
		if (ht->array[x] != NULL)
		{
			cur_node = ht->array[x];
			while (cur_node != NULL)
			{
				temp = cur_node->next;
				free(cur_node->key);
				free(cur_node->value);
				free(cur_node);
				cur_node = temp;
			}
		}
	}
	free(head->array);
	free(head);
}
