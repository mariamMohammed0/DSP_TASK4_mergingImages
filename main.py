from flask import Flask, render_template, send_file, request, redirect,jsonify
import functions as fn 
import numpy as np


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    cropped_indecies=[0,0,0,0,0,0,0,0,0,0]
    fn.read_images(cropped_indecies) 
    return render_template('index.html')
        
@app.route('/crop_image1', methods=['POST'])
def crop_image1():
    output = request.get_json()
    cropped_indecies=[0,0,0,0,0,0,0,0,0,0]
    cropped_indecies[0]=int(round(output['pic1']['left']))
    cropped_indecies[1]=int(round(output['pic1']['top'] ))
    cropped_indecies[2]=int(round(output['pic1']['width']))
    cropped_indecies[3]=int(round(output['pic1']['height']))

    cropped_indecies[4]=int(round(output['pic2']['left']))
    cropped_indecies[5]=int(round(output['pic2']['top'] ))
    cropped_indecies[6]=int(round(output['pic2']['width']))
    cropped_indecies[7]=int(round(output['pic2']['height']))

    cropped_indecies[8]=int(output['pic1_choice'])
    cropped_indecies[9]=int(output['pic2_choice'])



    fn.read_images(cropped_indecies)
    return output


@app.route('/save_image', methods=['POST'])
def save_image():
    output = request.get_json()
    # print(output['pic'])
    # print(output['index'])
    fn.download_img(output['pic'],output['index'])
    return output
    
if __name__ == "__main__":
    
    app.run(debug=True, threaded=True)