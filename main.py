from flask import Flask, render_template, send_file, request, redirect,jsonify
import functions as fn 
import numpy as np


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    cropping_info=[0,0,0,0,0,0,0,0,0,0,0]

    fn.images.read_images(    cropping_info) 
    return render_template('index.html')
        
@app.route('/crop_image1', methods=['POST'])
def crop_image1():
    
    output = request.get_json()

    cropping_info=[0,0,0,0,0,0,0,0,0,0,0]
    cropping_info[0]=int(round(output['pic1']['left']))
    cropping_info[1]=int(round(output['pic1']['top'] ))
    cropping_info[2]=int(round(output['pic1']['width']))
    cropping_info[3]=int(round(output['pic1']['height']))

    cropping_info[4]=int(round(output['pic2']['left']))
    cropping_info[5]=int(round(output['pic2']['top'] ))
    cropping_info[6]=int(round(output['pic2']['width']))
    cropping_info[7]=int(round(output['pic2']['height']))

    cropping_info[8]=int(output['pic1_choice'])
    cropping_info[9]=int(output['pic2_choice'])
    cropping_info[10]=1



    fn.images.read_images(cropping_info)
    return output


@app.route('/save_image', methods=['POST'])
def save_image():
    output = request.get_json()
    # print(output['pic'])
    # print(output['index'])
    fn.images.download_img(output['pic'],output['index'])
    return output
    
if __name__ == "__main__":
    
    app.run(debug=True, threaded=True)