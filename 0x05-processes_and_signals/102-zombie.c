#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - to keep the parent process running
 *
 * Return: 0 success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombie processes and print its PID
 *
 * Return: 0 success
 */
int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}
