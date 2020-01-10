if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)


    any_left = False
    winner = max(scores)
    scores.remove(winner)
    while not any_left:
        if winner == max(scores):
            scores.remove(max(scores))

        else:
            any_left = True

    print(max(scores))










