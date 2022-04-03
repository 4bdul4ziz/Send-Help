#you have a strring consisting of digits from 0-9. However, your friend replaces all occurences of 5 by 22 and that of 6 by 33 and gave it back to you as a string S
#find the number of all possuble strigs T modulo 10^9+7 using the transformed stirng 
#constaints: 1<=N<=2*10^5
#len(S)<=2*10^5

import sys

#constaints: 1<=N<=2*10^5
#len(S)<=2*10^5
def solve(N, S):
    #initialize the result
    result = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count2 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count3 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count4 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count5 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count6 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count7 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0,1,2,3,4,5,6,7,8,9
    count8 = [0]*10
    #initialize the number of 22,33
    count22 = 0
    count33 = 0
    #initialize the number of 0

def main():
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip('\n')
    result = solve(N, S)

    print(result)
