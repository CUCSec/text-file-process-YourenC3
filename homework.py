studentID=[]

count=0

with open('log_files/201811113028.log',encoding='utf-8') as f:
    for line in f:
        student_id=line.split(',')[1]
        student_id=student_id.split()
        studentID.append(student_id)


for ids in studentID:
    a=ids
    b="['学号：201811113028']"
    if str(a)==b:
        count=count+1
        

print(count)


