from flask import Flask, render_template, send_file, request, redirect,jsonify
import functions as fn 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    fn.read_2images()

        # if request.method == "POST":
 

    return render_template('index.html')
        


if __name__ == "__main__":
    app.run(debug=True, threaded=True)