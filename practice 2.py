def check_winners(scores, student_score):
    scores.sort()
    if student_score>scores[-4]:print('Вы в тройке победителей!')
    else:print('Вы не попали в тройку победителей')
a=[20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
check_winners(a,35)