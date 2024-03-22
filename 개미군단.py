# 풀이1
def solution(hp):
    answer = hp // 5  
    rest = hp % 5   
    if rest != 0:
        answer += rest // 3    
        rest = rest % 3
        if rest != 0:
            answer += rest // 1
    return answer

# 풀이2
def solution(hp):
    return (hp // 5) + ((hp % 5) // 3) + ((hp % 5) % 3)