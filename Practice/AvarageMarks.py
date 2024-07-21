if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for student in range(n):
        name, *lines = input().split()
        scores = list(map(float, lines))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        tot = sum(student_marks[query_name])
        num  = len(student_marks[query_name])
        result = tot/num
        print(f"{result:.2f}")
    else:
        print(f'Student not found')
    
    
