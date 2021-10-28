def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    pos = (sum(month[:a-1])+b) % 7
    
    answer += week[pos-1]
    
    return answer