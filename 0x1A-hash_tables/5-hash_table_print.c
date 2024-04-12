#include "hash_tables.h"
/**
 * hash_table_print - Function that prints a hash table to stdout.
 * @ht: hash table address.
 */
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int x = 0, cont = 0;
	hash_node_t *cur_node;

	if (ht != NULL)
	{
		printf("{");
		for (cont = 0; cont < ht->size; cont++)
		{
			cur_node = ht->array[cont];
			for (; cur_node != NULL; cur_node = cur_node->next)
			{
				if (x != 0)
					printf(", ");
				x = 1;
				printf("'%s': '%s'", cur_node->key, cur_node->value);
			}
		}
		printf("}\n");
	}
}
