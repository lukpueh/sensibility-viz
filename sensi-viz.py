from flask import Flask, render_template
import csv, json
app = Flask(__name__)

@app.route("/")
def hello():
  lines = []

  with open("data/gps.csv") as f:
    rd = csv.reader(f, delimiter=",")

    a = None
    b = None
    while True:
      try:
        b = rd.next()
        if not a:
          a = b
          continue
      except StopIteration:
        break

      lines.append([
                  [float(a[6]), float(a[7])],
                  [float(b[6]), float(b[7])]
                  ])
      a = b
  return render_template('main.html', lines=json.dumps(lines))

if __name__ == "__main__":
    app.run()