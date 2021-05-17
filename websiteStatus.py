from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
inloop = 0
count = 0
errcount = 0
with open(r"C:\Users\HP\OneDrive\Desktop\redditindiaURLs.txt", 'r+') as f:
    contents = f.readlines()
for i in contents:
    inloop = i
    req = Request("{}".format(inloop))
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        print(inloop)
        errcount += 1
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        print(inloop)
        errcount += 1
    else:
        print ('Website is working fine')
        count += 1
        print('Number of working websites: ', end='')
        print(count)