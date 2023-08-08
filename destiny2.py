def destiny():
    print('hello guys！')
    n = 0
    for i in range(3):
        print('welcome')
    print('输入您的生日来检查您的destiny')
    print('首先输入您的出生年份')
    a = int(input())  
    if a % 2 == 0:
        print('嗯，你有一点幸运')
        n += int(str(a)[3])
    elif a % 5 == 0:
        print('lucky dog')
        n += 5
    elif a == 2022:
        print('您的生活将会在一篇黑暗中------')
        n -= 7
    elif a % 100 == 2:
        print('你是个宝宝，希望您有美好的生活！')
        n += 6
    elif a % 10 % 2 == 0:
        print('您的生活中将会有死亡😱')
        n -= 10
    else:
        print('你只是个普通人')
        n = 6
    print('完成对您的年份的检查，现在是时候计算you的date了')
    print('现在输入您的date')
    b = int(input()) 
    if b >= 10:
        if b % 10 == a % 10 // 2 or b % 10 == a % 10:
            print('do not look behind you 😱😰🥶🥶🥶😱！')
            n -= 5
    if b == 9:
        print('您的生活很平静')
        n += 12
    if b <= 5 and a % 10 >= 2:
        print('祝您好运，you will live a long life')
        n += 7
    print('现在是时候输入您的月份了')
    print('now it is time to type in your mm')
    c = int(input())  
    if c >= 12:
        print('你不是人类！滚吧！')
        n = 0
    if c == 6:
        print('你会很6')
        n += 6
    if c // 10 == 1:
        print('你的生活将会乏味---boring')
        n -= 4
    else:
        print('您已经拥有happy和exciting的生活')
        n += 6
    if (c % 10) * (a % 100) * (a % 10) % 4 == 0:
        print('您可以退出了，you are the king')
        n += 14
    else:
        print('do not come again')
        n += 12

    print(' now check n')
    print(n)

destiny()