#include<stdio.h>
#include<string.h>

int main()
{
    int c=0;
    char sen[100];
    int a=0,e=0,i=0,o=0,u=0;
    scanf("%[^\s]",sen);
    
    if(strlen(sen)>0 && strlen(sen)<100)
    {
        while(sen[c]!='\0')
        {
            if(sen[c]=='a' || sen[c]=='A')
                a++;
            else if(sen[c]=='e' || sen[c]=='E')
                e++;
            else if(sen[c]=='i' || sen[c]=='I')
                i++;
            else if(sen[c]=='o' || sen[c]=='O')
                o++;
            else if(sen[c]=='u' || sen[c]=='U')
                u++;
            c++;    
        }
    }
    printf("a\n");
    printf("%d\n",a);
    printf("e\n");
    printf("%d\n",e);
    printf("i\n");
    printf("%d\n",i);
    printf("o\n");
    printf("%d\n",o);
    printf("u\n");
    printf("%d\n",u);
}
