'''
10, [9,4,4,4,7], [2,7,8,10,6]
[1,2,3,5,7]

2 9
4 6 7 8 10
1
3
5



1 3 4 5
2 10
6 7
8
9

2 3 6 8 9
'''

def solution(n, t1, t2):
    answer = list(set([i for i in range(1, n+1)]) - set(t1 + t2))
    group = []

    for j in range(len(t1)):
        if t1[j] in group or t2[j] in group:
            continue

        group = [t1[j], t2[j]]

        for i in range(len(t1)):
            if t1[i] in group:
                if t2[i] not in group:
                    group.append(t2[i])
            if t2[i] in group:
                if t1[i] not in group:
                    group.append(t1[i])

        group.sort()

        if len(group) % 2 == 0:
            answer.append(group[(len(group) // 2) - 1])
        else:
            answer.append(group[len(group) // 2])

    return sorted(list(set(answer)))


print(solution(10, [1,3,3,2,7], [4,4,5,10,6]))
