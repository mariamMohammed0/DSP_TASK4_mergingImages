from flask import Flask, render_template, send_file, request, redirect, jsonify
import OOPFunctions as fn
# import functions as fn
import cv2
import numpy as np
# from termcolor import colored

app = Flask(__name__)

def download_img( img_name, index):
    print('***************************************************************')
    img = cv2.imread('static/assets/images/upload/'+img_name)
    save_img(img, index)
    return

def save_img( img_1d, index):
    print('***************************************************************')
    img_2d = cv2.resize(img_1d, (500, 500))
    cv2.imwrite("static/assets/images/inputs/input_image" +
                str(index)+'.png', img_2d)

@app.route("/", methods=["GET", "POST"])
def index():
    # print("---------------------------index")
    # cropped_indecies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # fn.images.read_images(cropped_indecies)
    return render_template('index.html')


@app.route('/crop_image1', methods=['POST'])
def crop_image1():
    # print("---------------------------crop_image1")
    output = request.get_json()
    print(output)
    cropped_indecies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cropped_indecies[0] = int(round(output['pic1']['left']))
    cropped_indecies[1] = int(round(output['pic1']['top']))
    cropped_indecies[2] = int(round(output['pic1']['width']))
    cropped_indecies[3] = int(round(output['pic1']['height']))

    cropped_indecies[4] = int(round(output['pic2']['left']))
    cropped_indecies[5] = int(round(output['pic2']['top']))
    cropped_indecies[6] = int(round(output['pic2']['width']))
    cropped_indecies[7] = int(round(output['pic2']['height']))

    cropped_indecies[8] = int(output['pic1_choice'])
    cropped_indecies[9] = int(output['pic2_choice'])
    cropped_indecies[10] = int(output['outside'])
    print("first", cropped_indecies)
    processing = fn.ImageProcessing(cropped_indecies)
    processing.read_images()
    return output


@app.route('/save_image', methods=['POST'])
def save_image():
    # print(colored("---------------------------save_image",'blue'))
    # print('***************************************************************')
    output = request.get_json()


    download_img(output['pic'],output['index'])
    return output



if __name__ == "__main__":

    app.run(debug=True, threaded=True)
