s  = input('時間を教えてください:')
x, y = s.split(':')
x = int(x)
y = int(y)
t = x * 60 + y
t_700w = t * 5 // 7
ans_m, ans_s = divmod(t_700w, 60)
print(str(ans_m) + ':' + f'{ans_s:02}')
print('test')
