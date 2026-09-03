print("===== STUDENT RESULT =====")
name=input('enter your name')
tamil_mark=int(input('enter tamil mark'))
english_mark=int(input('enter english mark'))
maths_mark=int(input('enter maths mark'))
science_mark=int(input('enter science mark'))
computer_science_mark=int(input('enter computer science mark'))
total=tamil_mark+english_mark+maths_mark+science_mark+computer_science_mark
print("===== STUDENT RESULT =====")
print('name=',name)
print('total=',total)
average=total/5
print("average=",average)
if(average)>84:
    print('grade= a grade')
else:
    print('grade= b grade')
