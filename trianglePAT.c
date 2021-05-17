#include <stdio.h>
#include<math.h>

struct Triangle
{
  float area;
  int a,b,c;
}S[50],temp;

float findArea(float a, float b, float c)
{
    if (a < 0 || b < 0 || c <0 || (a+b <= c) ||
        a+c <=b || b+c <=a)
    {
        printf("No");
    }
    float s = (a+b+c)/2;
    return sqrt(s*(s-a)*(s-b)*(s-c));
}
void Sort(struct Triangle *S,int n)
{
  int i,j;
  for (i = 1; i < n; i++)
    for (j = 0; j < n - i; j++) 
    {
      if (S[j].area>S[j + 1].area)
        {
           temp = S[j];
           S[j] = S[j + 1];
           S[j + 1] = temp;
        }
  }
}

void DisplaySides(struct Triangle S)
{
int x,y,z;
x=S.a;
y=S.b;
z=S.c;
  if (x <= y && y <= z)
  {
    printf("%d %d %d\n",x,y,z);
  }
  else
  {
     if (x <= z && z <= y)
     {
        printf("%d %d %d\n",x,z,y);
     }
     else
     {
        if (y <= x && x <= z)
        {
            printf("%d %d %d\n",y,x,z);
        }
         else
         {
             if (y <= z && z <= x)
             {
               printf("%d %d %d\n",y,z,x);
             }
               else
               {
                  if (z <= x && x <= y)
                  {
                      printf("%d %d %d\n",z,x,y);
                  }
                  else
                  {
                     if (x == y && y == z)
                      {
                        printf("%d %d %d\n",x,y,z);
                      }
                    else
                    {
                        printf("%d %d %d\n",z,y,x);
                    }
                }
            }
        }
    }
}
}


int main()
{
  int n;
  //printf("Number of Triangles:");
  scanf("%d",&n);
  for(int i=0;i<n;i++)
  {
    //printf("Sides of Triangle: %d",i);
    scanf("%d %d %d", &S[i].a, &S[i].b, &S[i].c);
    S[i].area=findArea(S[i].a, S[i].b, S[i].c);
  }
  Sort(S,n);
  for(int i=0;i<n;i++)
  {
    DisplaySides(S[i]);
  }
}