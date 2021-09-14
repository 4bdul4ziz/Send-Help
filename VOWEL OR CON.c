/* AUTHOR :- RITUL SINGH
   DATE :- 02/09/2019
   TIME :- 00:48
   END TIME:- 01:12 */
#include<stdio.h>
int main()
{
	char c;
	int isLowercaseVowel,isUppercaseVowel;
	printf("Enter Your Alphabet\n");
	scanf("%c",&c);
	isLowercaseVowel = (c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
	isUppercaseVowel = (c=='A'||c=='E'||c == 'I'||c =='O'||c =='U');
	if (isLowercaseVowel || isUppercaseVowel)
	printf("Your Alphabet is VOWEL",c);
	else
	printf("Your Alphabet is CONSONANT",c);
	return 0;
	
}
