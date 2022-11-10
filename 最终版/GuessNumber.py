import easygui as g
import random as r
import sys
import time
#a = int(input("是否开始游戏（是输入1，否输入2）"))
while True:
    password = g.buttonbox(msg="是否开始游戏（是输入1，否输入2）",title = "猜拳游戏",choices = ("1","2"),
                                 image = "img/guess.gif")
    a = 0
    if password=="1":
        while True:
            a = a+1
            if a==1:
                break
            else:
                password2 = g.buttonbox(msg="要开始游戏吗？（是输入1，否输入2）", title="猜拳游戏", choices=("1", "2"),
                            image="img/guess.gif")
                '''g.msgbox("要开始游戏吗？", title="猜拳游戏", image=
                "img/guess.gif")'''
                if password2=="1":
                    break
                else:
                    print("感谢你的支持，欢迎下次再玩！\n关注PECompact获得更多python程序\nQQ\t3139373615")
                    sys.exit()
        rand = r.randint(1,3)#电脑随机生成的数
        computer = "电脑输入的拳"
        if rand == 1:
            computer = "石头"
        elif rand == 2:
            computer = "剪刀"
        else:
            computer = "布"
        person = g.buttonbox(msg="请出拳",title = "猜拳游戏",choices = ("石头","剪刀","布"),
                             image = "img/guess.gif")

        if person == computer:
            g.msgbox("你出的是"+person+",电脑出的是"+computer+",平局",title = "猜拳游戏",
                     image = "img/h.gif")
        elif (rand == 1 and person == "布")or(rand == 2 and person == "石头")or(rand == 3
            and person == "剪刀"):
            g.msgbox("你出的是"+person+",电脑出的是"+computer+"恭喜你，你赢了",title = "猜拳游戏",
                     image = "img/y.gif")
        else:
            g.msgbox("你出的是"+person+",电脑出的是"+computer+"很遗憾，你输了",title = "猜拳游戏",
                     image = "img/s.gif")
    else:
        print("感谢你的支持，欢迎下次再玩！\n关注PECompact获得更多python程序\nQQ\t3139373615")
        time.sleep(5)
        sys.exit()
        #break