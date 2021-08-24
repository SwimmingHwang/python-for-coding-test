'''
프로그래머스 위클리 4주차 
https://programmers.co.kr/learn/courses/30/lessons/84325
'''


def solution(table, languages, preference):
    answer = ''
    max_s = -1
    for t in table:
        t = t.split(' ')
        b =  {t[1] : 5, t[2] : 4, t[3] : 3, t[4] : 2, t[5] : 1}
        s = 0
        for index, l in enumerate(languages):
            s += (l in b and b[l] or 0) * preference[index]
        if (s > max_s):
            max_s = s
            answer = t[0]
        elif(s == max_s):
            if (answer >= t[0]):
                max_s = s
                answer = t[0]
                
    return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

solution(table, languages, preference)
