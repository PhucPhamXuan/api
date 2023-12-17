

# from flask import Flask
# from solver import PuzleSolver

# solver = PuzleSolver("./faJVTxgQnq_slice.png","./faJVTxgQnq_slice.png")
# solution = solver.get_position()
# print(solution)


from flask import Flask, render_template
from threading import Thread
from flask import request
from solver import PuzleSolver

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
      return 'Hi'
    if request.method == 'POST':
        data = request.json
        background = data['background']
        piece = data['piece']
        solver = PuzleSolver("./faJVTxgQnq_slice.png","./faJVTxgQnq_slice.png")
        solution = solver.get_position()
        print('Tọa độ cần kéo :',solution)
        return solution
        # return 'background {} piece {}'.format(background, piece)
    return 'HAHA'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
keep_alive()
