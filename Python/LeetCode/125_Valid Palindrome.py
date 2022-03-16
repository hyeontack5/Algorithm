# 리스트로 변환

def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # 영문자, 숫자 여부를 판별
            str.append(char.lower()) # 대소문자를 구분하지 않으므로 모두 소문자로 변환

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():          
            return False
    
    return True

# 데크 자료형을 이용한 최적화

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True
