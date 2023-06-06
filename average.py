

averge = 0
averge_count =0

print ("nomarat ra varde kon")
print("exit")



while True:

    vorodi = input()
    if vorodi == "exit":
        break
    else:
        averge += int(vorodi)    
        averge_count += 1

    

print("moadel shoma: ",averge/averge_count)
