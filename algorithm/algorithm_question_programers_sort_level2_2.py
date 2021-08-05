#
# def solution():
#     citations = [3, 0, 6, 1, 5]
#     another = [20,18,19]
#     answer = 0
#     n = len(citations)
#     high_count = 0
#     low_count = 0
#
#     for j in range(n):
#         for i in citations:
#
#             if citations[j] > i:
#                 high_count += 1
#
#             elif citations[j] < i:
#                 low_count += 1
#
#             elif citations[j] == i:
#                 high_count += 1
#                 low_count += 1
#
#         if high_count == low_count:
#             answer = low_count
#
#         high_count = 0
#         low_count = 0
#
#     print(f"result: {answer}")
#     return answer

# solution()

def solution2():
    citations = [21,22,23,24,25,26]
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        print(f"idx: {idx}")
        print(f"citation: {citation}")
        if idx >= citation:
            print(f"results: {idx}")
            return idx
    print(f"another_result: {len(citations)}")
    return len(citations)

solution2()

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
#
# 0 1 2  3    4 5
#
# 12 8 5 3    1 0
"""
이 과학자가 발표한 논문의 수는 5편이고, 
그중 3편의 논문은 3회 이상 인용되었습니다. 
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다
"""