"""
There are n newly constructed buildings evenly lined-up in vit. Each building is painted beautifully. You are given n inputs, where each value represents color of the ith building. Your task is to return the maximum distance between two buildings with different color. The distance between the ith and jth building is abs(i - j), where abs(n) is the absolute value of n. Note - There are atleast two different colors in colors in input.

Input Format

The first line contains one integer n, the number of buildings. Each of the next n lines each contain one integer m, the color code painted on buildings.

Constraints

n == colors.length, 2 <= n <= 100, 0 <= colors[i] <= 100

Output Format

Print integer which denotes the maximum distance between two buildings with different color.

Sample Input 0

7
1
2
1
6
1
2
1
Sample Output 0

5
Sample Input 1

2
0
1
Sample Output 1

1


"""


def maxDistance(colors):
    # Write your code here
    max_dist = 0
    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            if colors[i] != colors[j]:
                max_dist = max(max_dist, abs(i - j))
    return max_dist


if __name__ == '__main__':
    n = int(input())
    colors = []
    for _ in range(n):
        colors_item = int(input())
        colors.append(colors_item)
    result = maxDistance(colors)
    print(result)

    

# Path: hr29.py
"""
