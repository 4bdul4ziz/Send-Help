'''
Algorithm - GrowTree(D, F) - grows a feature tree from training data
Input - data D, set of features F
Output - feature tree T with labelled leaves
if Homogeneous(D) then return Label(D);
S <- BestSplit(D, F);
split D into subsets Di according to the literals in S;
for each i, do 
    if Di != phi then Ti <- GrowTree(Di, F);
    else Ti is a leaf labelled with Label(D);
end
return a tree whose root is labelled with S and whose childeren are Ti

Algorithm - BestSplit-Class(D, F) - find the best split for a decision tree
Input - data D, set of features F
Output - feature f to split on
Imin <- 1;
for each f < F do
    split D into subsets D1, ...., Dl according to the values vj of f;
    i IMp({D1,....,Dl}) < Imin then
        Imin <- Imp({D1,....,Dl});
        fbest <- f;
    end
end
return fbest;
'''

import math
import random
import sys
import time
import numpy as np
import pandas as pd


class GrowTree:
    def __init__(self, data, features):
        self.data = data
        self.features = features
        self.tree = {}
        self.tree = self.growTree(self.data, self.features)

    def growTree(self, data, features):
        if self.homogeneous(data):
            return self.label(data)
        else:
            bestSplit = self.bestSplit(data, features)
            # print("bestSplit", bestSplit)
            subsets = self.splitData(data, bestSplit)
            # print("subsets", subsets)
            tree = {}
            tree[bestSplit] = {}
            for i in range(len(subsets)):
                if subsets[i] != []:
                    tree[bestSplit][i] = self.growTree(subsets[i], features)
                else:
                    tree[bestSplit][i] = self.label(data)
            return tree

    def bestSplit(self, data, features):
        Imin = 1
        for f in features:
            subsets = self.splitData(data, f)
            I = self.impurity(subsets)
            if I < Imin:
                Imin = I
                fbest = f
        return fbest

    def splitData(self, data, feature):
        subsets = []
        for i in range(len(feature)):
            subsets.append([])
        for d in data:
            for i in range(len(feature)):
                if d[feature[i][0]] == feature[i][1]:
                    subsets[i].append(d)
        return subsets

    def impurity(self, subsets):
        total = 0
        for s in subsets:
            total += len(s)
        I = 0
        for s in subsets:
            I += (len(s) / total) * self.entropy(s)
        return I

    def entropy(self, data):
        if len(data) == 0:
            return 0
        else:
            p = self.positive(data)
            n = self.negative(data)
            if p == 0 or n == 0:
                return 0
            else:
                return -p * math.log(p, 2) - n * math.log(n, 2)

    def positive(self, data):
        p = 0
        for d in data:
            if d[-1] == 1:
                p += 1
        return p / len(data)

    def negative(self, data):
        n = 0
        for d in data:
            if d[-1] == 0:
                n += 1
        return n / len(data)

    def homogeneous(self, data):
        if len(data) == 0:
            return True
        else:
            p = self.positive(data)
            n = self.negative(data)
            if p == 0 or n == 0:
                return True
            else:
                return False

    def label(self, data):
        if self.positive(data) > self.negative(data):
            return 1
        else:
            return 0

    def getTree(self):
        return self.tree

    def printTree(self, tree, level):
        for key in tree:
            print("  " * level + str(key))
            if type(tree[key]) is dict:
                self.printTree(tree[key], level + 1)
            else:
                print("  " * (level + 1) + str(tree[key]))

    
    def classify(self, tree, data):
        for key in tree:
            if type(tree[key]) is dict:
                for i in range(len(key)):
                    if data[key[i][0]] == key[i][1]:
                        return self.classify(tree[key][i], data)
            else:
                return tree[key]

    def testTree(self, tree, data):
        correct = 0
        for d in data:
            if self.classify(tree, d) == d[-1]:
                correct += 1
        return correct / len(data)

    def crossValidate(self, data, features, k):
        random.shuffle(data)
        size = int(len(data) / k)
        accuracy = 0
        for i in range(k):
            test = data[i * size : (i + 1) * size]
            train = data[:i * size] + data[(i + 1) * size:]
            tree = GrowTree(train, features)
            accuracy += tree.testTree(tree.getTree(), test)
        return accuracy / k

def main():
    data = []
    features = []
    with open("data.txt") as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    with open("features.txt") as f:
        for line in f:
            features.append([int(x) for x in line.split()])
    tree = GrowTree(data, features)
    tree.printTree(tree.getTree(), 0)
    print(tree.testTree(tree.getTree(), data))
    print(tree.crossValidate(data, features, 10))

if __name__ == "__main__":
    main()
