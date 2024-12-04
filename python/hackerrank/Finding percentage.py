if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0 
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scorelist = student_marks[query_name]
    
    for i in scorelist:
        total += i
    
    average = total/len(scorelist)
    print("{:.2f}".format(average))
