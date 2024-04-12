#include "hash_tables.h"
/**
 * hash_table_get - Function that retrieves a value of 
 * associted key.
 * @ht: hash table to be searched.
 * @key: the key to be found.
 * Return: the value for associated key on success or
 * NULL on failure.
 */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	hash_node_t *t_node;
	unsigned long int index;

	if (key == NULL || ht == NULL)
		return (NULL);
	index = key_index((const unsigned char *)key, ht->size);
	t_node = ht->array[index];
	while (t_node != NULL)
	{
		if (strcmp(t_node->key, key) == 0)
			return (t_node->value);
		t_node = t_node->next;
	}
	return (NULL);
}
