import turtle
import math
import random
from playsound import playsound
import menu_screen
import mysql.connector as ms

bulletstate="ready"
def start():
    mycon=ms.connect(host="localhost",user="root",passwd="bhavika",database="players")
    mycursor=mycon.cursor()

    #background
    sc=turtle.Screen()
    sc.clear()
    sc.bgcolor("black")
    sc.title("SPACE WARS")
    sc.bgpic("C:/Users/pranjal/Desktop/Space Wars/bgpic.gif")
    #sc.setup(width=1.0,height=1.0)

    #adding enemy & player shape to the screen 
    sc.addshape("C:/Users/pranjal/Desktop/Space Wars/player.gif")
    sc.addshape("C:/Users/pranjal/Desktop/Space Wars/enemy.gif")

    #drawing border
    proj=turtle.Turtle()
    proj.speed(0)
    proj.color("yellow")
    proj.penup()
    proj.setposition(-350,-250)
    proj.pendown()
    proj.pensize(5)
    proj.fd(700)
    proj.lt(90)
    proj.fd(560)
    proj.lt(90)
    proj.fd(700)
    proj.lt(90)
    proj.fd(560)
    proj.hideturtle()

    #creating player
    player=turtle.Turtle()
    player.color("red")
    player.shape("C:/Users/pranjal/Desktop/Space Wars/player.gif")
    player.turtlesize(1.5)
    player.penup()
    player.speed(10)
    player.setposition(0,-220)
    player.setheading(90)

    playerspeed=20

    #creating bullet
    bullet=turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5,0.5)
    bullet.hideturtle()
    bullet.setpos(0,-1200)
    bulletspeed=50

    #bulletstate="ready"

    #creating enemies
    number_of_enemies=5
    enemies=[]

    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())
            
    for enemy in enemies:
        enemy.color("green")
        enemy.shape("C:/Users/pranjal/Desktop/Space Wars/enemy.gif")
        enemy.penup()
        x=random.randint(-200,200)
        y=random.randint(150,250)
        enemy.setposition(x,y)
        
    enemyspeed=10

    #Scores
    score="0"
    s=0

    score_pen=turtle.Turtle()
    score_pen.speed(0)
    score_pen.penup()
    score_pen.color("white")
    score_pen.setposition(-350,-300)
    write_score="SCORE:"+score
    score_pen.pendown()
    score_pen.write(write_score,move=False,align="Left",font=("Arial",20,"bold"))
    score_pen.hideturtle()

    #Game over text
    game_over=turtle.Turtle()
    game_over.penup()
    game_over.color("white")
    game_over.setposition(0,0)
    game_over.hideturtle()

    #exit to main menu button
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.setpos(100,-320)
    pen.pendown()
    pen.fd(250)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.fd(250)
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)

    pen.penup()
    pen.setpos(130,-310)

    pen.pendown()
    pen.write("Exit to Main Menu",font=("Permanent Marker",17))

    #defining functions 

    #moving player left, right, up and down
    def move_left():
        x=player.xcor()
        if x>-300:
            x=x-playerspeed
            player.setx(x)

    def move_right():
        x=player.xcor()
        if x<300:
            x=x+playerspeed
            player.setx(x)

    def move_up():
        y=player.ycor()
        if y<280:
            y=y+playerspeed
            player.sety(y)

    def move_down():
        y=player.ycor()
        if y>-220:
            y=y-playerspeed
            player.sety(y)
        
            
    #firing bullets
    def fire_bullet():
        global bulletstate
        if bulletstate=="ready":
            bulletstate="fire"
            playsound("C:/Users/pranjal/Desktop/Space Wars/How To Recreate The STAR WARS Laser Sound_00 02 25-00 02 27 - oDownloader.mp3", False)
            x=player.xcor()
            y=player.ycor()+10
            bullet.setposition(x,y)
            bullet.showturtle()
            bulletstate="ready"

    #collision checking
    def collision_happens(a,b):
        distance=math.sqrt(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2))
        if distance<60:
            return True
        else:
            return False


    #keyboard bindings
    turtle.listen()
    turtle.onkeypress(move_left,"Left")
    turtle.onkeypress(move_right,"Right")
    turtle.onkeypress(move_up,"Up")
    turtle.onkeypress(move_down,"Down")
    turtle.onkey(fire_bullet,"space")


    def exit_to_menu_btn(x,y):
        if 130<x<380 and -310<y<-260:
            sc.clear()
            menu_screen.main_menu()
    turtle.onscreenclick(exit_to_menu_btn,1,add=True)
    turtle.listen()



    #main loop of the game
    while True:
        for enemy in enemies:
            x=enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)

            #moving the enemy
            if enemy.xcor()>300 or enemy.xcor()<-300:
                for i in enemies:
                    y=i.ycor()
                    y-=40
                    i.sety(y)
                enemyspeed*=-1
        
            if enemy.ycor()<-220:
                enemy.hideturtle()
                x=random.randint(-200,200)
                y=random.randint(150,250)
                enemy.setposition(x,y)
                enemy.showturtle()
                

            #collision checking between enemy & bullet              
            if collision_happens(bullet,enemy):
                bullet.hideturtle()
                bulletstate="ready"
                bullet.setposition(-3000,1200)

                playsound("C:/Users/pranjal/Desktop/Space Wars/Star Wars explosion sound effects part 3_00 00 00-00 00 01 - oDownloader.mp3",False)
        
                enemy.hideturtle()
                x=random.randint(-200,200)
                y=random.randint(150,250)
                enemy.setposition(x,y)
                enemy.showturtle()

                #updating score
                s=eval(score)
                s=s+10
                score=str(s)
                write_score="SCORE:"+score
                score_pen.clear()
                score_pen.write(write_score,move=False,align="Left",font=("Arial",20,"bold"))
                score_pen.hideturtle()
                
           
        #moving bullet
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
           
        #border checking bullet
        if bullet.ycor()>330:
            bullet.hideturtle()
            bulletstate="ready"

     

        #collision checking between player & enemy
        if collision_happens(player,enemy):
            playsound("C:/Users/pranjal/Desktop/Space Wars/27_5s_to_2_327_5s_Game_Over_Sound_Effects_All_Soun.mp3",False)
            enemy.hideturtle()
            player.hideturtle()
            game_over.write("GAME OVER",move=False,align="center",font=("Arial",40,"bold"))
            game_over.hideturtle()
            game_over.penup()
            mycursor.execute("insert into data values({})".format(s))
            mycon.commit()
            mycursor.execute("select max(High_score) from data")
            x=mycursor.fetchall()
            game_over.setpos(-100,-50)
            game_over.pendown()
            game_over.write("Your Score: "+str(s),move=False,align="Left",font=("Arial",25,"bold"))
            game_over.penup()
            game_over.setpos(-100,-100)
            game_over.pendown()
            game_over.write("Highscore  : "+str(x[0][0]),move=False,align="Left",font=("Arial",25,"bold"))
            break


#bibliography
#Christian Thompson, youtube.com
#Programmers' Colloqouy, youtube.com
#Zamzar.com, file conversion
#resizeimage.net, Online Image Resizer
#kindpng.com
#pixabay.com    
#oDownloader.com, sound audio cropper
    



