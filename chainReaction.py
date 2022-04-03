'''
Wile lives alone in the desert, so he entertains himself by building complicated machines that run on chain reactions. Each machine consists of N modules indexed 1,2,…,N. Each module may point at one other module with a lower index. If not, it points at the abyss.

Modules that are not pointed at by any others are called initiators. Wile can manually trigger initiators. When a module is triggered, it triggers the module it is pointing at (if any) which in turn may trigger a third module (if it points at one), and so on, until the chain would hit the abyss or an already triggered module. This is called a chain reaction.

Each of the N modules has a fun factor Fi. The fun Wile gets from a chain reaction is the largest fun factor of all modules that triggered in that chain reaction. Wile is going to trigger each initiator module once, in some order. The overall fun Wile gets from the session is the sum of the fun he gets from each chain reaction.

For example, suppose Wile has 4 modules with fun factors F1=60,F2=20,F3=40, and F4=50 and module 1 points at the abyss, modules 2 and 3 at module 1, and module 4 at module 2. There are two initiators (3 and 4) that Wile must trigger, in some order.

As seen above, if Wile manually triggers module 4 first, modules 4, 2, and 1 will get triggered in the same chain reaction, for a fun of max(50,20,60)=60. Then, when Wile triggers module 3, module 3 will get triggered alone (module 1 cannot get triggered again), for a fun of 40, and an overall fun for the session of 60+40=100.

However, if Wile manually triggers module 3 first, modules 3 and 1 will get triggered in the same chain reaction, for a fun of max(40,60)=60. Then, when Wile triggers module 4, modules 4 and 2 will get triggered in the same chain reaction, for a fun of max(50,20)=50, and an overall fun for the session of 60+50=110.

Given the fun factors and the setup of the modules, compute the maximum fun Wile can get if he triggers the initiators in the best possible order.

Input
The first line of the input gives the number of test cases, T. T test cases follow, each described using 3 lines. Each test case starts with a line with a single integer N, the number of modules Wile has. The second line contains N integers F1,F2,…,FN where Fi is the fun factor of the i-th module. The third line contains N integers P1,P2,…PN. If Pi=0, that means module i points at the abyss. Otherwise, module i points at module Pi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum fun Wile can have by manually triggering the initiators in the best possible order.

'''


def calc():
    n = int(input())
    dices = [int(x) for x in input().split()]
    maxNum = max(dices)
    m = [0] * (maxNum+1)
    for i in range(n):
        m[dices[i]] += 1
    result = 0
    left = 0
    for i in range(maxNum, 0, -1):
        left += m[i]
        if left > 0:
            left -= 1
            result += 1
    return result


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, calc()))
