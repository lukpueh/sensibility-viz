from flask import Flask, render_template
import csv, json
app = Flask(__name__)

@app.route("/")
def hello():
  lines_gps = []
  lines_nw = []
  lines_fused = []

  with open("data/locations_1464904913.56") as f:
    rd = csv.reader(f, delimiter=",")
    for row in rd:
      if row[0] == "gps":
        lines_gps.append([float(row[6]), float(row[7])])
      if row[0] == "network":
        lines_nw.append([float(row[6]), float(row[7])])

      if row[0] == "fused":
        lines_fused.append([float(row[6]), float(row[7])])

  return render_template('main.html', lines=json.dumps({"gps": lines_gps, 
                                                        "nw" : lines_nw, 
                                                        "fused": lines_fused}))
if __name__ == "__main__":
    app.run()