from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = -1
        with open('data.txt') as file:
            self.high_score = file.read()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} High Score :{self.high_score}", align="center", font=("Courier", 15, "italic"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Courier", 25, "italic"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', mode= 'w') as file:
                file.write(f"{self.high_score}")
        self.score = -1
        self.update_score()
