if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maxscore = max(arr)
    newScore = []
    for score in arr:
        if score != maxscore:
            newScore.append([score])
            runnerUp = max(newScore)
            Result = runnerUp[0]
print(Result)
