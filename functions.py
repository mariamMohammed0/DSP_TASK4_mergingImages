from glob import glob
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')

def resize_images(img1,img2):
    #----------------Resizing
    img1_resized = cv2.resize(img1, (500, 500))
    img2_resized = cv2.resize(img2, (500, 500))
    cv2.imwrite("static/assets/images/front/resized_img1.png", img1_resized)
    cv2.imwrite("static/assets/images/front/resized_img2.png", img2_resized)
    return img1_resized,img2_resized


def Process_images(img1,img2,choices):
    print("---------------------------choices",choices)
    print("-----------------img1",len(img1[0]))
    print("-----------------img2",len(img2[0]))

     #---------converting it to a 1d array
    img1_1dArray=img1.flatten()
    img2_1dArray=img2.flatten()
    print("-----------------img1",len(img1_1dArray))
    print("-----------------img2",len(img1_1dArray))
    #-------------- fourier transform
    f  = np.fft.fft(img1_1dArray)
    f2 = np.fft.fft(img2_1dArray)
    print("-----------------img1",len(f))
    print("-----------------img2",len(f2))
    
    if (choices[8]==1 and choices[9]==1 ):
        print("choice1 phase choice2 phase")
        combined_img1 = np.multiply(np.exp(1j*np.angle(f)), np.exp(1j*np.angle(f2)))
        
    elif (choices[8]==0 and choices[9]==1 ):
        print("choice1 mag choice2 phase")      
        combined_img1 = np.multiply(np.abs(f), np.exp(1j*np.angle(f2)))


    elif (choices[8]==1 and choices[9]==0 ):
        print("choice1 phase choice2 mag")
        combined_img1 = np.multiply(np.abs(f2), np.exp(1j*np.angle(f)))

    elif (choices[8]==0 and choices[9]==0 ):
        print("choice1 mag choice2 mag")
        combined_img1 = np.multiply(np.abs(f), np.abs(f2))
   

    imgCombined = np.real(np.fft.ifft(combined_img1))
    img_2d=imgCombined.reshape((500, 500))
    cv2.imwrite("static/assets/images/outputs/"+'output_image1'+'.png', img_2d)

    return  img_2d 


def read_images(cropped_indecies):

    # --------reading files by matplot and opencv
    images_files = glob('static/assets/images/inputs/*.jpg')
    img_file1=images_files[1]
    img_file2=images_files[4]
    
    img1_mpl = plt.imread(img_file1)
    img1_cv2 = cv2.imread(img_file1)
    img2_mpl = plt.imread(img_file2)
    img2_cv2 = cv2.imread(img_file2)

    # -------- gray scaled
    img2_gray = cv2.cvtColor(img2_cv2, cv2.COLOR_RGB2GRAY)
    img1_gray = cv2.cvtColor(img1_cv2, cv2.COLOR_RGB2GRAY)

    # ---------resize images
    img1,img2=resize_images(img1_gray,img2_gray)
    Process_images(img1,img2,cropped_indecies)



def minimum(a, b):
    if a <= b:
        return a
    else:
        return b


def save_img(img_1d, img_height, img_width, file_name):
    img_2d = img_1d.reshape((img_height, img_width))
    cv2.imwrite("static/assets/images/outputs/"+file_name+'.png', img_2d)


def blur_image(img, cropped_indecies, file_name):
    print(cropped_indecies)
    left = cropped_indecies[0]
    top = cropped_indecies[1]
    width = cropped_indecies[2]
    height = cropped_indecies[3]

    kept_part = img[top:top+height, left:left+width]
    blurred_part = cv2.blur(img, ksize=(30, 30))
    result = blurred_part.copy()
    result[top:top+height, left:left+width] = kept_part
    cv2.imwrite("static/assets/images/after_blurring/" +
                file_name+'.png', result)
    print('doneeeee')
    return result

<<<<<<< HEAD
def process_1dImage(img1_gray,img2_gray,img_height,img_width):

    #----------------Resizing
=======

def process_1dImage(img1_gray, img2_gray, img_height, img_width):

    # ----------------Resizing
>>>>>>> 7d637521e63c9d61c9fe7fd10d084a668ec46af5
    img1_resized = cv2.resize(img1_gray, (img_width, img_height))
    img2_resized = cv2.resize(img2_gray, (img_width, img_height))
    # ---------converting it to a 1d array
    img1_1dArray = img1_resized.flatten()
    img2_1dArray = img2_resized.flatten()
    # -------------- fourier transform
    f = np.fft.fft(img1_1dArray)
    f2 = np.fft.fft(img2_1dArray)

    combined_img1 = np.multiply(np.abs(f), np.exp(1j*np.angle(f2)))
    combined_img2 = np.multiply(np.abs(f2), np.exp(1j*np.angle(f)))

    imgCombined1 = np.real(np.fft.ifft(combined_img1))
    imgCombined2 = np.real(np.fft.ifft(combined_img2))

    return imgCombined1, imgCombined2


def read_2images(cropped_indecies):

    # --------reading files by matplot and opencv
    images_files = glob('static/assets/images/inputs/*.jpg')
    img_file1 = images_files[1]
    img_file2 = images_files[3]

    img1_mpl = plt.imread(img_file1)
    img1_cv2 = cv2.imread(img_file1)
    img1_gray = cv2.cvtColor(img1_cv2, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("static/assets/images/outputs/original_img1.png", img1_gray)

    img2_mpl = plt.imread(img_file2)
    img2_cv2 = cv2.imread(img_file2)
    img2_gray = cv2.cvtColor(img2_cv2, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("static/assets/images/outputs/original_img2.png", img2_gray)

    # --------getting height width
    img1_height = len(img1_mpl)
    img1_width = len(img1_mpl[0])

    img2_height = len(img2_mpl)
    img2_width = len(img2_mpl[0])

    # --------------- processing then display output
    new_height = minimum(img1_height, img2_height)
    new_width = minimum(img1_width, img2_width)

    if(cropped_indecies[1] == 0):
        print('nothing')
        # img1_gray=blur_image(img1_gray,[100,100,150,250],'blurr1')
        # img2_gray=blur_image(img2_gray,[100,100,150,250],'blurr2')

    else:
        img1_gray = blur_image(img1_gray, cropped_indecies[:4], 'blurr1')
        img2_gray = blur_image(img2_gray, cropped_indecies[4:], 'blurr2')

    img1, img2 = process_1dImage(img1_gray, img2_gray, new_height, new_width)

    save_img(img1, new_height, new_width, 'output_image1')
    save_img(img2, new_height, new_width, 'output_image2')

    # display_2grayimgs(img1,img2,new_height,new_width,new_height,new_width)
