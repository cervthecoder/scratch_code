from typing import List

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores: List[float] = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum = 0
cycle_count = 0

for n in student_marks[query_name]:
    cycle_count += 1
    sum += n

print(sum / cycle_count)


