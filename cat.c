#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main(){
    int p1, p2;
    p1 = fork();
    p2 = fork();
    if (p1 || p1){
        printf ("My ID: %d\n", getpid());
        printf ("My parent ID: %d\n", getppid());
        if(p1 > 0 && p2 == 0){
            fork();
            printf("My ID: %d\n", getpid());
            printf("My parent ID: %d\n", getppid());
        }
    }
}