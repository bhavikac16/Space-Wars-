import turtle
#import menu_screen

def ins_screen():
    wn=turtle.Screen()
    wn.clear()
    wn.title("SPACE WARS")
    wn.bgpic("C:/Users/pranjal/Desktop/Space Wars/Space Art Wallpaper-761517.gif")
    #wn.setup(width=1.0,height=1.0)

    main_text=turtle.Turtle()
    main_text.hideturtle()
    main_text.penup()
    main_text.color("white")
    main_text.setposition(-150,250)
    main_text.write("Space Wars", move=False,align="Left", font=("Dead Kansas",40))


    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.setpos(-350,100)
    pen.pendown()
    pen.write("INSTRUCTIONS TO PLAY:",move=True,font=("Dead Kansas",20))

    pen.penup()
    pen.setpos(-350,50)
    pen.pendown()
    pen.write("~ To move the player upwards, use UP ARROW KEY.",font=("Arial",15))

    pen.penup()
    pen.setpos(-350,0)
    pen.pendown()
    pen.write("~ To move the player downwards, use DOWN ARROW KEY.",font=("Arial",15))

    pen.penup()
    pen.setpos(-350,-50)
    pen.pendown()
    pen.write("~ To move the player towards left, use LEFT ARROW KEY.",font=("Arial",15))

    pen.penup()
    pen.setpos(-350,-100)
    pen.pendown()
    pen.write("~ To move the player towards right, use RIGHT ARROW KEY.",font=("Arial",15))

    pen.penup()
    pen.setpos(-350,-150)
    pen.pendown()
    pen.write("~ To shoot the bullet, use SPACEBAR.",font=("Arial",15))

    pen.penup()
    pen.setpos(-350,-200)
    pen.pendown()
    pen.write("~ Each hit on enemy counts as 10 points.",font=("Arial",15))

    pen.penup()
    pen.color("white")
    pen.setpos(100,-300)
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
    pen.setpos(130,-290)
    pen.pendown()
    pen.write("Exit to Main Menu",font=("Permanent Marker",17))


    '''def exit_to_menu_btn(x,y):
        if 100<x<350 and -300<y<-210:
            wn.clear()
            menu_screen.main_menu()
    turtle.onscreenclick(exit_to_menu_btn,1)
    turtle.listen()'''
#ins_screen()        

 
