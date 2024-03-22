def solution(myString, pat):
    string = ''
    for i in myString:
        if i == 'A':
            string += 'B'
        else:
            string += 'A'
    if pat in string:
        answer = 1
    else:
        answer = 0
    return answer