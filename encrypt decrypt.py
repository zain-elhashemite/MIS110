def encrypt():
    res = []
    msg = input("Enter a message")
    print(msg)
    key = 5
    for i in msg:
        x = ord(i)
        res.append(x+key)

    return(res)

def decrypt():
    ans = []
    for i in res:
        code = i - key
        ans.append(chr(code))
    print("".join(ans))
