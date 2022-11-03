/*
Assume that you are developing a plagiarism identifier software which identifies whether the given pattern (P) exist in the given text (T) or not. To bypass your software detection, the user will prepare a modified text (M) from the actual text (A) in the following way:

Between every character in text (A) they will insert the predecessor and successor characters of the current position unless and until the predecessor and successor characters are different and prepare the modified text (M) and that will be given to your software as text (T). If the predecessor and successor characters are the same then they will not insert any characters at that position.

successor characters are the same then they will not insert any characters at that position.

For Example:

Actual Text (A): abccd

Modified Text (M): aabbbccccdd

Now your task is to handle this modified text and identify whether there exists any given pattern (P) as per the actual text.

Prepare an efficient string-matching algorithm to identify the existence of any given pattern in the given text with the following conditions.

Your program should not extract the actual text from the modified text in any form.
You should not delete or add any character in the given text, and you should not make a duplicate copy of the given text.
Note: In test cases, 1st line is the text and 2nd line is the pattern

Test Case 1:

Input:

aabbbcccaaabbbaaabbbaa

aba

Output:

Exists

Input:

aabbbcccaaabbbaaabbbaa

abba

Output:

Not Exists
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

//function to find the number of occurences of the letters in the pattern
int findOccurences(std::string pattern){
    int occurences = 0;
    for(int i = 0; i < pattern.length(); i++){
        if(pattern[i] == 'a'){
            occurences++;
        }
    }
    return occurences;
}

int main(){
    std::string text, pattern;
    std::cin >> text >> pattern;
    std::vector<int> pattern_vec(pattern.size());
    for(int i = 0; i < pattern.size(); i++){
        pattern_vec[i] = pattern[i];
    }
    std::vector<int> text_vec(text.size());
    for(int i = 0; i < text.size(); i++){
        text_vec[i] = text[i];
    }
    std::sort(pattern_vec.begin(), pattern_vec.end());
    std::sort(text_vec.begin(), text_vec.end());
    int i = 0, j = 0;
    while(i < text_vec.size() && j < pattern_vec.size()){
        if(text_vec[i] == pattern_vec[j]){
            i++;
            j++;
        }
        else{
            i = i - j + 1;
            j = 0;
        }
    }
    if(j == pattern_vec.size()){
        std::cout << "Exists" << std::endl;
    }
    else{
        std::cout << "Not Exists" << std::endl;
    }
    return 0;
}




