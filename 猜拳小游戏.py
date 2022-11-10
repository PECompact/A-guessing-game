import easygui as g
import random as r
g.msgbox("要开始游戏吗？",title = "猜拳小游戏",image = "C:\石头剪刀布图片PYTHON/guess.gif")
rand = r.randint(1,3)
person = g.buttonbox("请出拳",title = "猜拳小游戏",choices = ("石头","剪刀","布"),image = "C:\石头剪刀布图片PYTHON/guess.gif")
if rand == 1:
    computer = "石头"
elif rand == 2:
    computer = "剪刀"
else:computer = "布"
if computer == person:
    g.msgbox("电脑出的是"+computer+"，你出的是"+person+"，平局",title = "猜拳小游戏",image = "C:\石头剪刀布图片PYTHON/p.gif")
elif (computer =="石头" and person == "布") or(computer == "剪刀" and person == "石头") or (computer == "布" and person == "剪刀"):
    g.msgbox("电脑出的是"+computer+"，你出的是"+person+"，恭喜你，你赢了！",title = "猜拳小游戏",image = "C:\石头剪刀布图片PYTHON/y.gif")
else:
    g.msgbox("电脑出的是"+computer+"，你出的是"+person+"，你输了",title = "猜拳小游戏",image = "C:\石头剪刀布图片PYTHON/s.gif")
quit()    
                     
