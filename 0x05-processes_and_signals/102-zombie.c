#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
* infinite_while - creates an infinite loop
* Return: 1, 0 never
*/
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
/**
* main - creates zombie child process
* Return: 0
*/
int main(void)
{
	pid_t zombie_id;
	int x;

	for (x = 0; x < 5 x++)
	{
		zombie_id = fork();
		if (zombie_id > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie_id);
			sleep(1);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
