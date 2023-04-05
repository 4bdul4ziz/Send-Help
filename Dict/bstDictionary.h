#ifndef _BST_DICTIONARY_H
#define _BST_DICTIONARY_H
#include <cstdint>
#include <stdexcept>
#include <algorithm>

static const int NULL_INDEX = 0xffffffff, DEFAULT_INITIAL_CAPACITY = 16;

template <typename KeyType, typename ValueType>

class BSTDictionary{
public:
    explicit BSTDictionary(int _cap = DEFAULT_INITIAL_CAPACITY){
        if(nTrees == 0){

            capacity = _cap;

            left = new int[capacity];
            right = new int[capacity];


            prvFree(capacity);
        }
    }

    ~BSTDictionary(){
        if(nTrees == 1){
            delete[[maybe_unused]][] left;
            delete[[maybe_unused]][] right;
        }
    }

    BSTDictionary(const BSTDictionary &other){
        if(nTrees == 0){
            capacity = other.capacity;
            left = new int[capacity];
            right = new int[capacity];
            prvFree(capacity);
        }
        nTrees++;
        root = prvCopy(other.root);
    }

    BSTDictionary &operator=(const BSTDictionary &other){
        if(this != &other){
            if(nTrees == 1){
                delete[] left;
                delete[] right;
            }
            nTrees = 0;
            capacity = other.capacity;
            left = new int[capacity];
            right = new int[capacity];
            prvFree(capacity);
            nTrees++;
            root = prvCopy(other.root);
        }
        return *this;
    }

    







};

template <typename KeyType,typename ValueType>
int *BSTDictionary<KeyType,ValueType>::counts = nullptr;

template <typename KeyType,typename ValueType>
int *BSTDictionary<KeyType,ValueType>::heights = nullptr;

template <typename KeyType,typename ValueType>
int *BSTDictionary<KeyType,ValueType>::left = nullptr;

template <typename KeyType,typename ValueType>
int *BSTDictionary<KeyType,ValueType>::right = nullptr;

template <typename KeyType,typename ValueType>
int BSTDictionary<KeyType,ValueType>::nTrees = 0;

template <typename KeyType,typename ValueType>
int BSTDictionary<KeyType,ValueType>::capacity = 0;

template <typename KeyType,typename ValueType>
int BSTDictionary<KeyType,ValueType>::freeListHead = 0;

template <typename KeyType,typename ValueType>
KeyType *BSTDictionary<KeyType,ValueType>::keys = nullptr;

template <typename KeyType,typename ValueType>
ValueType *BSTDictionary<KeyType,ValueType>::values = nullptr;

#endif