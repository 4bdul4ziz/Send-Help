def unique_in_order(s):
    fin = [s[0]]
    for i in range(0, len(s)):
        if i == len(s) - 1:
            return fin
        if s[i] != s[i + 1]:
            print("NIGGA")
            fin.append(s[i + 1])
            print(fin)
    return fin


x = unique_in_order("AAAABBBCCDAABBB")
print(type(x))
