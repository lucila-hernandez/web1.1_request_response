from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'One day, a {adjective} {noun} decided to enter a karaoke contest at the park. It sang so loudly, even the squirrels joined in!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit():
        n = int(n)
        repeat_str = (word + ' ') * n
        return repeat_str.strip()
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dicegame():
    random_number = random.randint(1, 6)
    if random_number == 6:
        result = f'You rolled a {random_number}. You won!'
    else:
        result = f'You rolled a {random_number}. You lost!'
    return result

if __name__ == '__main__':
    app.run(debug=True)
