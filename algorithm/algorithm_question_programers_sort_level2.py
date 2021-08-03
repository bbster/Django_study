"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"

"""

import itertools

def solution():
    numbers = [6, 10, 2]
    numbers2 = [3, 30, 34, 5, 9]
    numbers3 = [1, 40, 3, 5, 100,  7, 60,  9, 20, 50, 70]
    answer = ''
    convert_numbers = []
    result = []

    iter_value = itertools.permutations(list(map(str, numbers)), len(numbers))

    for j in iter_value:
        iter_result = int("".join(j))
        result.append(iter_result)

    result.sort()
    answer = str(result[-1])

    print(f"answer_type: {answer}")

    return answer

solution()