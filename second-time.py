

print("enter second :")
second =float(input())


h = int( second // 3600)

m = int(second % 3600) // 60

s = int(second % 3600) % 60

print("time",h, ":",m,":",s)





