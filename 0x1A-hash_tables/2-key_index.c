#include "hash_tables.h"
/**
 * key_index - function that gives the index of a key.
 * @key: the key to identify the index.
 * @size: array size of hash table.
 * Return: the index for storing the key/value pair
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int index;

	if (size == 0)
		return (0);
	index = hash_djb2(key);
	return (index % size);
}
