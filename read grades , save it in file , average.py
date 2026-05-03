# inserts grades and prints average 

infile = open("C:\\Users\\lenovo\\Desktop\\ban\\first26\\py\\file.txt","w")

names = input("Enter the name of a student: ")
grade = input("Enter his/her grade: ")

list1=[]

while names !="" and grade != "":
   
   list1.append([names,float(grade)])
   infile.write(names) 
   print(grade,file=infile) 
   names = input("Enter the name of a student: ")
   grade = input("Enter his/her grade: ") 

count = 0
for i in range (len(list1)):
    grades = list1[i][1]
    count+=1

average=grades/count

print(average)    
    
print(list1)    


infile.close()   







