import socket
import blockscore

numericInput = int(input())
n = numericInput 
ct = 0 
while n:
    rmind = n%10
    if rmind == 1:
        ct += 1
    n = n//10;
if ct % 2 == 0:
    numericInput = numericInput * 10
else:
    numericInput = numericInput * 10 + 1
print(numericInput)