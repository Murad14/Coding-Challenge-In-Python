from flask import Flask
import random

random_num = random.randint(0,9)
print(random_num)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://camo.githubusercontent.com/16741c65a48048b329261c62921f8e501ce08a5c9bb1e77aee9dd7c58e9bb61a/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f336f376143535071584535433654387442432f67697068792e676966" width= 500>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"





if __name__ == "__main__":
    app.run(debug=True)