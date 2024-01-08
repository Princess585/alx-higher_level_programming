#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * struct listint_s - Function of a singly list linked
 * @n: The integer of a function
 * @next: points to next node
 *
 * Description: singly list limked to a node struct for projects
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
void reverse_listint(listint_t **head);

#endif /* LISTS_H */
