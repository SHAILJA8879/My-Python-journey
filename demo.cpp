#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
    pid_t pid;

    pid = fork();

    if (pid < 0)
    {
        printf("Process creation failed.\n");
        exit(1);
    }
    else if (pid == 0)
    {
        printf("Child Process\n");
        printf("Child PID = %d\n", getpid());

        execl("/bin/ls", "ls", NULL);

        printf("Exec failed\n");
        exit(1);
    }
    else
    {
        printf("Parent Process\n");
        printf("Parent PID = %d\n", getpid());
        wait(NULL);

        printf("Child process completed.\n");
    }

    return 0;
}

