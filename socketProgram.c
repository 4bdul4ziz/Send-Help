#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#define MAX 255
#define PORT 8080
#define SA struct sockaddr

void func(int sock)
{
        char buff[MAX];
        int n;
        for(;;)
        {
                bzero(buff,MAX);
                printf("Enter a command:");
                n=0;
                while((buff[n++]=getchar())!='\n');
                if((strncmp(buff,"exit",4))==0)
                {
                        break;
                }
                write(sock,buff,sizeof(buff));
                bzero(buff,sizeof(buff));
                read(sock,buff,sizeof(buff));
                printf("%s",buff);
        }
}

int main()
{
        int sock,sock1,len;
        struct sockaddr_in servaddr,cli;
        sock=socket(AF_INET,SOCK_STREAM,0);
        servaddr.sin_family=AF_INET;
        servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
        servaddr.sin_port=htons(PORT);
        bind(sock,(SA*)&servaddr,sizeof(servaddr));
        listen(sock,5);
        len=sizeof(cli);
        sock1=accept(sock,(SA*)&cli,&len);
        func(sock1);
        close(sock);
}
Client Code:
#include<netdb.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#define MAX 255
#define PORT 8080
#define SA struct sockaddr

void func(int sock)
{
        char buff[MAX];
        int n;
        for(;;)
        {
                bzero(buff,sizeof(buff));
                read(sock,buff,sizeof(buff));
                printf("%s",buff);
                if((strncmp(buff,"exit",4))==0)
                        break;
                write(sock,buff,sizeof(buff));
        }
}
int main()
{
        int sock,sock1;
        struct sockaddr_in servaddr,cli;
        sock=socket(AF_INET,SOCK_STREAM,0);
        bzero(&servaddr,sizeof(servaddr));
        servaddr.sin_family=AF_INET;
        servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");
        servaddr.sin_port=htons(PORT);
        connect(sock,(SA*)&servaddr,sizeof(servaddr));
        func(sock);
        close(sock);
}
 
