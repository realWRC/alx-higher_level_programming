#include "hash_tables.h"
/**
 * hash_table_create - creates a hash table.
 * @size: Array size.
 * Return: Pointer to the new hash table on success
 * or NULL on failure.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int index;
	hash_table_t *table;

	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
		return (NULL);
	table->size = size;
	table->array = malloc(sizeof(hash_node_t *) * size);
	if (table->array == NULL)
		return (NULL);
	for (index = 0; index < size; index++)
		table->array[index] = NULL;
	return (table);
}
