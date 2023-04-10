from flask import Flask, render_template 

app = Flask(__name__)

Devices = [
  {
    'id': 1,
    'device name': 'A',
    'risk' : 'a',
  },
  {
    'id': 2,
    'device name': 'B',
    'risk' : 'b',
  },
  {
    'id': 3,
    'device name': 'C',
    'risk' : 'c',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', devices=Devices)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
  