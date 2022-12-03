from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")

def index():
    return render_template(
        "index.html",
        this_map="Google Map",
        planes=get_planes()
    )

def get_planes():
    planes = ["Cessna Jeff", "RV-10 Bob", "RV-12 Dave"]
    return planes

if __name__ == '__main__':
    app.run(debug=True)