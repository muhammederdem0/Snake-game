import turtle,random,time
Liste=[]
skor=0
maxSkor=0
#çerçeve ayarları:
w=turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600,600)
w.bgcolor("blue")
w.tracer(0)

#Yılan kafası:
yn=turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0,0)
yn.yon = "dur"

def hareket():
    if yn.yon=="ust":
        y=yn.ycor()
        yn.sety(y+20)
    if yn.yon=="alt":
        y=yn.ycor()
        yn.sety(y-20)
    if yn.yon=="sag":
        x=yn.xcor()
        yn.setx(x+20)
    if yn.yon=="sol":
        x=yn.xcor()
        yn.setx(x-20)

def yukariGit():
    if yn.yon != "alt":
        yn.yon="ust"
def asagiGit():
    if yn.yon != "ust":
        yn.yon="alt"
def sagaGit():
    if yn.yon!="sol":
        yn.yon="sag"
def solaGit():
    if yn.yon!="sag":
        yn.yon="sol"
w.listen()
w.onkeypress(yukariGit,"Up")
w.onkeypress(asagiGit,"Down")
w.onkeypress(sagaGit,"Right")
w.onkeypress(solaGit,"Left")

yem=turtle.Turtle()
yem.speed(0)
yem.shape("turtle")
yem.color("brown")
yem.penup()
yem.goto(0,100)

def ye():
    global skor,maxSkor
    if yn.distance(yem)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        yem.goto(x,y)
        kuyruk=turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)
        skor+=5
        if skor>maxSkor:
            maxSkor=skor
            w.title(f"Skor:{skor} En yüksek skor:{maxSkor}")
    uzunluk=len(Liste)
    for indis in range (uzunluk-1,0,-1):
        x=Liste[indis-1].xcor()
        y=Liste[indis-1].ycor()
        Liste[indis].goto(x,y)
    if len(Liste)>0:
        x=yn.xcor()
        y=yn.ycor()
        Liste[0].goto(x,y)

def baslangic():
    global skor
    time.sleep(0.1)
    yn.goto(0,0)
    yn.yon="dur"
    for eklem in Liste:
        eklem.goto(1000,1000)
    Liste.clear()
    skor=0
    w.title(f"skor: {skor}, En yüksek skor:{maxSkor}")

while True:
    w.update()
    ye()
    hareket()
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        baslangic()
    for eklem in Liste:
        if eklem.distance(yn)<20:
            baslangic()
    time.sleep(0.1)

w.mainloop()