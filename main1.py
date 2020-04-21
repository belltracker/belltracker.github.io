from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/bells/<bellsINPUT>")
def bellsSave(bellsINPUT):

    
    bellsFile = open("bells.txt", "r")
    isEmpty = bellsFile.read()

    if isEmpty == "this broke so yeah :(":

        bellsFile = open("bells.txt", "w")
        bellsFile.write(bellsINPUT)

        bellsFile.close()

    else:

        

        bellsFile = open("bells.txt", "w")

        bellsBefore = int(isEmpty)

        bellsCurrent = int(bellsINPUT)

        bellsAfter = bellsBefore + bellsCurrent
        bellsSum = str(bellsAfter)

        bellsFile.write(bellsSum)
        bellsFile.close()

    return render_template("saved.html")



@app.route("/.well-known/security.txt")
def security():

    return render_template("security.html")

if __name__ == "__main__":
    app.run()