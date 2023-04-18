start=int(input("ป้อนแม่สูตรคูณเริ่มค้น = "))
stop=int(input("ป้อนแม่สูตรคูณสุดท้าย = "))

for x in range(start,stop+1):
    print("แม่  = ",x)
    for y in range(1,12):
        print(x,'x',y," = ",(x*y))