kor_score = []
math_score = []
eng_score = []
midterm_score = [kor_score, math_score, eng_score]
student_score = []
student_average = []
string_temp = ['eng_score', 'math_score', 'kor_score']


def show_who_I_am(name, dept="소프트웨어학과"):
    print("학과: {0}, 이름: {1}".format(dept, name))


def initialize_list():
    for i in range(num):
        kor_score.append(0)
        math_score.append(0)
        eng_score.append(0)
        student_score.append(0)
        student_average.append(0)


def input_and_save_score():
    for subject in midterm_score:
        print(string_temp.pop())
        for i in range(len(subject)):
            subject[i] = int(input(str(i+1) + "번 점수입력:"))


def sum_and_average():
    for subject in midterm_score:
        i = 0
        for n in subject:
            student_score[i] += n
            i += 1

    for i in range(len(subject)):
        student_average[i] = student_score[i]/len(midterm_score)


dept = input("당신의 학과를 입력하세요(생략가능) : ")
name = input("당신의 이름을 입력하세요(필   수) : ")

if dept == "":
    show_who_I_am(name)
else:
    show_who_I_am(name, dept)

num = int(input("점수를 입력할 학생은 몇명입니까? : "))

initialize_list()
input_and_save_score()
sum_and_average()

print(midterm_score)
print(student_score)
print(student_average)