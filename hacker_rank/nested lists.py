if __name__ == '__main__':
    name_list = []
    scores_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        scores_list.append(score)

    best_score: float = max(scores_list)
    best = name_list[scores_list.index(best_score)]
    scores_list.remove(best_score)
    name_list.remove(best)
    removed = False
    while not removed:
        if best_score == max(scores_list):
            best = name_list[scores_list.index(best_score)]
            scores_list.remove(best_score)
            name_list.remove(best)
        else:
            removed = True

    best_score: float = max(scores_list)
    best = name_list[scores_list.index(best_score)]
    final = []
    print(scores_list)
    print(name_list)

    for n in scores_list:
        if n == best_score:
            print(name_list[scores_list.index(float(n))])

#    for name in final:
#        print(name)
