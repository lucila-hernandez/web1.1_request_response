
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_desert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

if __name__ == '__main__':
    app.run(debug=True)
