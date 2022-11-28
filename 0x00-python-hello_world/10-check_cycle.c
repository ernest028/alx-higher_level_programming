#include "lists.h"

/**
 *  * check_cycle - checks if list is a loop, ie, if it has a tail node
 *
 * 		that points to the head node
 *
 *    * @list: list to be analyzed
 *
 *     * Return: 1 if loop, 0 if not loop
 */

int check_cycle(listint_t *list)
{

	listint_t *slow, *fast;
	slow = fast = list;

	while(slow && fast && fast->next)
	{
		/* Slow pointer will move one node per iteration whereas
		 *
		 * 	fast node will move two nodes per iteration */

		slow = slow->next;
		fast  = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
