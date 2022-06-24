from re import T
import turtle

# todo: modulize it, add end condition

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
# (-400, 400), (-300, 300)
wn.setup(width=800, height=600)
wn.tracer(0)


def create_turtle_object(goto_x: int, goto_y:int, stretch_width: int=1, stretch_len:int=1, shape: str="square", color:str="white") -> turtle.Turtle:
    o = turtle.Turtle()
    o.speed(0)
    o.shape(shape)
    o.color(color)
    o.shapesize(stretch_wid=stretch_width, stretch_len=stretch_len)
    o.penup()
    o.goto(goto_x, goto_y)
    return o

# paddles
# stretch_width 5 = size 50, stretch:len 1 = size 10
paddle_a = create_turtle_object(stretch_width=5, stretch_len=1, goto_x=-350, goto_y=0)
paddle_b = create_turtle_object(stretch_width=5, stretch_len=1, goto_x=350, goto_y=0)

# ball
ball = create_turtle_object(goto_x=0, goto_y=0)

# movements
def generate_verticle_moving_functions(turtle_obj: turtle.Turtle, moving_size: int) -> callable:
    def moving():
        y = turtle_obj.ycor()
        # overwrite y with new position
        y += moving_size
        #positive moving size indicating up moving, negative down moving
        turtle_obj.sety(y)
    return moving

paddle_a_up = generate_verticle_moving_functions(paddle_a, 20)
paddle_a_down = generate_verticle_moving_functions(paddle_a, -20)
paddle_b_up = generate_verticle_moving_functions(paddle_b, 20)
paddle_b_down = generate_verticle_moving_functions(paddle_b, -20)

# keyboard binding
wn.listen()
# onkeypress's first argument must be a function which takes no argument
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# game loop
while True:
        wn.update()

