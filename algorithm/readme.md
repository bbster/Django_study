**알고리즘 연습**
---
* Level2 문제에서 조합 관련 정리
* itertools
    * 파이썬 기본제공하는 라이브러리
    * 이 모듈은 자체적으로 혹은 조합하여 메모리 효육적인 도구들의 집합
 
* 그 중 일부만 정리 해봄
```python
* 조합형 이터레이터 *
product(): 데카르트의 곱, 중첩 루프와 동등
    ㄴ product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations(): 모든 가능한 순서, 반복되는 요소 없음
    ㄴ  permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
combinations(): 정렬된 순서, 반복되는 요소 없음
    ㄴ combinations('ABCD', 2) => AB AC AD BC BD CD
combinations_with_replacement(): 정렬된 순서, 반복되는 요소 있음, 중복제거
    ㄴ combinations_with_replacement('ABCD', 2) => AA AB AC AD BB BC BD CC CD DD

```
---
* **https://programmers.co.kr/learn/challenges**
* **https://wikidocs.net/book/922**