rows = ["1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
s = input()
res = ""
for char in s:
    if char != " ":
        for row in rows:
            if char in row:
                res += row.split(char)[0][-1]
    else:
        res += " "

print(res)