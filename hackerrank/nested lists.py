if __name__ == '__main__':
    student = []
    s = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
        s.add(score)
        
    low_score = sorted(s)[1]
    low_names = []
    
    for name,score in student:
        if score == low_score:
            low_names.append(name)
    
    for name in sorted(low_names):
        print(name) 
