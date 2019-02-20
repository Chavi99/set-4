def count_lines(s):
    c=0
    for i in s:
        if i=='.':
            c+=1
    print(c)
s=input()
count_lines(s)
