from flask import Flask, render_template, request
import matrix


app = Flask(__name__)


all_posts = [{"Title":"Post 1","Body":"This is post 1","Author":"Mickey"}, {"Title":"Post 2","Body":"This is post 2"}]

@app.route("/matrix", methods=["POST","GET"])
def showMatrix():
    return render_template("matrix.html")

@app.route("/result", methods=["POST","GET"])
def showResult():
    if request.method == "POST":
        #declare
        input = []
        targetSum=int()
        sumRow = []

        input.append(request.form["digit1"])
        input.append(request.form["digit2"])
        input.append(request.form["digit3"])
        input.append(request.form["digit4"])
        input.append(request.form["digit5"])

        targetSum = int(request.form["total"])

        sumRow.append(int(request.form["lenght"]))
        sumRow.append(int(request.form["suma"]))

        # print(input)
        # print(sumRow)
        # print(targetSum)
        result = matrix.calculateMatrix(input, targetSum, sumRow)
    return render_template("result.html", result = result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts=all_posts)

@app.route("/home/<string:name>")
def hello(name):
    return("Hello world new " + name)

if __name__=="__main__":
    app.run(debug=True)
