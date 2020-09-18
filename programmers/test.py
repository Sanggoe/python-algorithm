def solution(numbers):
    a = list()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a.append(numbers[i] + numbers[j])

    return list(set(a))

print(solution([5,0,2,7]))
