/*Write an algorithm to find the possible next greater number from the given set of digits.
 Say for example, if a number contains 6 digits as 123456 next possible higher number will be 123465.
  consider another example 7531, in this no number is possible which is greater than this with same set of digits.
   Find the logic and write code in C++.

Example:

Input:

Get the input size of number

Any number with that size

Output:

Possible greater number within that digit, if not print " not possible".*/

#include<iostream>
#include<algorithm>         
using namespace std;

void swap(char *x,char *y) 
{
	char temp=*x;
	*x=*y;
	*y=temp;
}

void nextNum(char num[],int size)
{
	int i,j;
	for(i=size-1;i>0;i--)	
	{
		if(num[i-1]<num[i])  
		    break;
	}
	
	if(i==0)         
	{
		cout<<"Not possible";
		return;
	}
	int x=num[i-1],smaller=i;
	for(j=i+1;j<size;j++)
	{
		if(num[j]>x && num[j]<num[smaller])
		{
			smaller=j;
		}
	}
	swap(&num[smaller],&num[i-1]); 
	sort(num+i,num+size);           
    	for(int i=0;i<size;i++)
	{
		cout<<num[i];
	}
	return ;
}

int main()
{
	int n;
	cout<<"Enter the size of the number :";
	cin>>n;
	char number[n];
	cout<<"Enter the number :";
	for(int i=0;i<n;i++)
	{
		cin>>number[i];
	}
	nextNum(number,n);
	return 0;
}