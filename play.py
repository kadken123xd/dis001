count=int(input("ป้อนตัวเลขของคุณ : "))

i=1  #จำนวนครั้ง
summation=0 #ค่าสะสม
average=0   #ค่าเฉลี่ย
while i<=count:
      summation+=i
      print("รอบที่=",i,"ค่าสะสม =",summation)
      i=i+1
      average=summation/count

print("ผลรวมทั้งหมด",summation,"ค่าเฉลี่ย",average)    

    