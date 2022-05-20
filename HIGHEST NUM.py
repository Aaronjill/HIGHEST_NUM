student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
num=0
highest_num=0
for n in student_scores:
  num=n
  if n>highest_num:
    highest_num=n
print(highest_num)