import turtle
import instruction_screen
import start_game


def main_menu():
    #main screen
    wn=turtle.Screen()
    wn.title("SPACE WARS")
    wn.bgpic("C:/Users/pranjal/Desktop/Space Wars/Space Art Wallpaper-761517.gif")
    
    #title of the game 
    main_text=turtle.Turtle()
    main_text.hideturtle()
    main_text.penup()
    main_text.color("white")
    main_text.setposition(-150,250)
    main_text.write("Space Wars", move=False,align="Left", font=("Dead Kansas",40))

    #drawing and writing the menu screen options 
    pen1=turtle.Turtle()
    pen1.hideturtle()
    pen1.penup()
    pen1.setpos(-150,0)
    pen1.speed(0)
    pen1.color("white")
    pen1.pendown()
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)
    pen1.lt(90)
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)



    pen1.penup()
    pen1.lt(90)
    pen1.setpos(-150,-120)
    pen1.speed(0)
    pen1.pendown()
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)
    pen1.lt(90)
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)



    pen1.penup()
    pen1.lt(90)
    pen1.setpos(-150,-240)
    pen1.speed(0)
    pen1.pendown()
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)
    pen1.lt(90)
    pen1.fd(300)
    pen1.lt(90)
    pen1.fd(100)


    #writing buttons
    pen2=turtle.Turtle()
    pen2.hideturtle()
    pen2.color("white")
    pen2.penup()
    pen2.setpos(-50,35)
    pen2.pendown()
    pen2.write("START",font=("Permanent Marker",20,"bold"))


    pen2.penup()
    pen2.setpos(-100,-85)
    pen2.pendown()
    pen2.write("HOW TO PLAY",font=("Permanent Marker",20,"bold"))

    pen2.penup()
    pen2.setpos(-90,-205)
    pen2.pendown()
    pen2.write("QUIT GAME",font=("Permanent Marker",20,"bold"))

    #defining functions of the buttons
    def start_btn(x,y):
        if -150<x<150 and 0<y<100:
            start_game.start()

    def ins_btn(x,y):
        if -150<x<150 and -120<y<-20:
            instruction_screen.ins_screen()
            def exit_to_menu_btn(x,y):
                if 100<x<350 and -300<y<-210:
                    wn.clear()
                    main_menu()
            turtle.onscreenclick(exit_to_menu_btn,1,add=True)
            turtle.listen()

    
    def quit_btn(x,y):
        if -150<x<150 and -240<y<-140:
            turtle.bye()

    #binding functions to left mouse click        
    turtle.onscreenclick(start_btn,1,add=True)
    turtle.onscreenclick(ins_btn,1,add=True)
    turtle.onscreenclick(quit_btn,1,add=True)
    turtle.listen()
        
main_menu()
    
