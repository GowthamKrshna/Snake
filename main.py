from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

Game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while Game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Collision with wall
    if snake.head.xcor() >=280 or snake.head.xcor() <= -280 or snake.head.ycor() >=280 or snake.head.ycor() <= -280:
        scoreboard.reset()
        snake.reset()

    # Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()