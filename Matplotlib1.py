import matplotlib.pyplot as plt

student_names = ["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
student_marks = [35,50,20,45,25,40,25,40]

marks_perc = []
for i in student_marks:
    res = (i/50) * 100
    marks_perc.append(res)
print(marks_perc)

def linechart():
    plt.plot(student_names, student_marks, marker = "^", linestyle = "dotted", color = "blue")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.title("Student Test Results")
    plt.show()

linechart()

def bargraph():
    plt.bar(student_names, marks_perc)
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks Percentage")
    plt.title("Student Test Results")
    plt.show()

bargraph()