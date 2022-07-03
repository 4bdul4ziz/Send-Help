#binary to string converter
#!/usr/bin/env python3

def main():
    N = int(input())
    binary = bin(N)[2:]
    print(binary)
    print(len(binary))
    print(int(binary, 2))

main()

