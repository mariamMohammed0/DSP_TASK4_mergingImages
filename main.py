from flask import Flask, render_template, send_file, request, redirect,jsonify
import functions as fn 
import json
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    fn.read_2images()

        # if request.method == "POST":
 

    return render_template('index.html')
        
@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    fn.read_2images()
    return output


if __name__ == "__main__":
    app.run(debug=True, threaded=True)