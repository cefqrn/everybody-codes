d=*map(int,open(0)),
print(sum(max(0,sum(d)//len(d)-c)for c in d))