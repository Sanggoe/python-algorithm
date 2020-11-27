# 문자열 내 p와 y의 개수

<br/>

#### 문제 설명

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

<br/>

#### 제한사항

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

<br/>

#### 입출력 예

| s       | answer |
| ------- | ------ |
| pPoooyY | true   |
| Pyy     | false  |

<br/>

#### 입출력 예 #1

'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

<br/>

#### 입출력 예 #2

'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

<br/>

#### 내가 작성한 코드1

```python
def solution(s):
    p=0
    y=0
    
    for i in s.lower():
        if i is 'p':
            p += 1
        elif i is 'y':
            y += 1
    
    return True if p==y else False
```

* 처음엔 고전적인 for loop 탐색 형식으로 구현했다.
* 물론 실행속도는 Case의 최대 0.01ms 였지만, 파이썬스럽지 않은 코드여서 다시 변경

<br/>

#### 내가 작성한 코드2

```python
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
```

* 한줄로 끝. 대소문자를 구분하지 않으니 먼저 소문자로 만들어준다.
* 문자열 내장함수 count를 이용해 존재하는 모든 문자열의 개수를 찾아 비교하여 반환!

<br/>

#### 다른 사람이 작성한 맘에 드는 코드

```python
없다..! 가장 간단한 방법으로 보임
```

<br/>