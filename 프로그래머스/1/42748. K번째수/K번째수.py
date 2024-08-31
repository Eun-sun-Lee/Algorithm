def solution(array, commands):
    answer = []
    for s, e, k in commands:
        arr = array[s-1:e]
        arr.sort()
        answer.append(arr[k-1])
    return answer