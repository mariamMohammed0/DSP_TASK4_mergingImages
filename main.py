from flask import Flask, render_template, send_file, request, redirect,jsonify
import functions as fn 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    fn.read_2images()

        # if request.method == "POST":
 

    return render_template('index.html')
        
@app.route('/crop_image1', methods=['POST'])
def crop_image1():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    print(round(output['left']))
    print(round(output['top']))
    print(round(output['width']))
    print(round(output['height']))
    fn.read_2images()
    return output

@app.route('/crop_image2', methods=['POST'])
def crop_image2():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    print(round(output['left']))
    print(round(output['top']))
    print(round(output['width']))
    print(round(output['height']))
    fn.read_2images()
    return output

if __name__ == "__main__":
    app.run(debug=True, threaded=True)