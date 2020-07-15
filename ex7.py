"""
Zipped!

The National University conducts an examination of ```N``` students in ```X``` subjects.
Your task is to compute the average scores of each student.
"""
if __name__ == "__main__":
    N, X = map(int, input().split())

    scores = []
    for i in range(X):
        scores += [list(map(float, input().split()))]

    scores = zip(*scores)

    for score in scores:
        print(sum(score)/len(score))