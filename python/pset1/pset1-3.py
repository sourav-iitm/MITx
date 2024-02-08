lngst=s[0]
for i in range(len(s)):
    for j in range(i, len(s)-1):
        subs=s[i:j+2]
        if s[j+1]>=s[j] and len(subs)>len(lngst):
            lngst=subs
        if s[j+1]<s[j]:
            break
print(lngst)