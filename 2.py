def count_words(s):
    c=0
    for i in s:
        if i==' ':
            c+=1
    if s[-1]==' ':
        c-=1
    c+=1
    print(c)
s=input()
count_words(s)
