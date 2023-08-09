from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.up, 'w')
screen.onkey(snake.up, 'W')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.down, 's')
screen.onkey(snake.down, 'S')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.right, 'D')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.left, 'A')
screen.onkey(snake.left, 'a')

is_game_on = True


def exit_game():
    score.reset()
    global is_game_on
    is_game_on = False



screen.onkey(exit_game, 'e')

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        score.reset()
        snake.reset()

    # detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

# screen.exitonclick()
