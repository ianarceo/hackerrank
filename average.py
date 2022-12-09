if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    x, y = 0, 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key == query_name:
            for x in student_marks[key]:
                y=y+x
            ave = y / len(student_marks[key])
    
    print(f"{ave:.2f}")