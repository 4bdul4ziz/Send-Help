/*
Goal
Develop and implement a word ladder finder.
Details
A word ladder (aka doublet) is a type of puzzle created by Charles Dodgson (aka Lewis Carroll) in the 1800s. The premise of the puzzle is to “convert” one word into the other by a sequence of single-letter changes, with each change generating a valid English word. For example, you can change beer into wine via the sequence beer – beet – bent – lent – lint – line – wine. There may be other ladders for these words as well.
Your program should begin by reading words from the file sgb-words.txt; the file consists of 5 757 words used to test the Stanford GraphBase. Note that all words have exactly five letters.
Each word should have two values connected to it: • A pointer to a word (and its connected data)
Pro tip: You can use an integer index instead of a pointer. Use −1 for NULL or nullptr. • A linear list of pointers to other words
Initialize the pointer for each word to NULL. Then, examine each pair of words — there are 16 568 646 such pairs. If the pair has a Hamming distance of 1, then add each word — a pointer to the word, actually — to the other word’s list.
Read two five-letter words from the keyboard. Find both words in the word list. If either word is not in the list, stop and output that no word ladder exists. Otherwise, do the following algorithm.

*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>

using namespace std;
struct word {...};

string wordList[];

//split the word into a list of characters
string splitter(string word, &wordList){
    for (int i = 0; i < word.length(); i++){
        wordList[i] = word[i];
    }
    return wordList;
}

//compare the two words to see if they are one letter apart
bool compare(string word1, string word2){
    int count = 0;
    for (int i = 0; i < word1.length(); i++){
        if (word1[i] != word2[i]){
            count++;
        }
    }
    if (count == 1){
        return true;
    }
    else{
        return false;
    }
}

//find the word in the list
int findWord(string word, string wordList[]){
    for (int i = 0; i < wordList.length(); i++){
        if (word == wordList[i]){
            return i;
        }
    }
    return -1;
}

//function to make a list of the words read from the file
string wordList[];
void makeList(string wordList[]){
    ifstream infile;
    infile.open("sgb-words.txt");
    string word;
    int i = 0;
    while (infile >> word){
        wordList[i] = word;
        i++;
    }
    infile.close();
}
