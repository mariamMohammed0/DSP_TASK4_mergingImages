from glob import glob
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')

def minimum(a, b):  
    if a <= b:
        return a
    else:
        return b

def save_img(img_1d,img_height,img_width,file_name):
    img_2d=img_1d.reshape((img_height, img_width))
    fig, axs = plt.subplots( figsize=(15, 5))
    axs.imshow(img_2d, cmap='Greys')
    axs.axis('off')
    fig.savefig('static/assets/images/'+file_name)

def process_1dImage(img1_gray,img2_gray,img_height,img_width):

    #----------------Resizing
    img1_resized = cv2.resize(img1_gray, (img_width, img_height))
    img2_resized = cv2.resize(img2_gray,(img_width, img_height))
    #---------converting it to a 1d array
    img1_1dArray=img1_resized.flatten()
    img2_1dArray=img2_resized.flatten()
    #-------------- fourier transform
    f  = np.fft.fft(img1_1dArray)
    f2 = np.fft.fft(img2_1dArray)

    combined_img1 = np.multiply(np.abs(f), np.exp(1j*np.angle(f2)))
    combined_img2 = np.multiply(np.abs(f2), np.exp(1j*np.angle(f)))
   

    imgCombined1 = np.real(np.fft.ifft(combined_img1))
    imgCombined2 = np.real(np.fft.ifft(combined_img2))

    return  imgCombined1 ,imgCombined2

def read_2images():
    # --------reading files by matplot and opencv
    images_files = glob('static/assets/images/*.jpg')
    img_file1=images_files[0]
    img_file2=images_files[3]

    img1_mpl = plt.imread(img_file1)
    img1_cv2 = cv2.imread(img_file1)
    img1_gray = cv2.cvtColor(img1_cv2, cv2.COLOR_RGB2GRAY)

    img2_mpl = plt.imread(img_file2)
    img2_cv2 = cv2.imread(img_file2)
    img2_gray = cv2.cvtColor(img2_cv2, cv2.COLOR_RGB2GRAY)


    # --------getting height width
    img1_height =len(img1_mpl)
    img1_width  =len(img1_mpl[0])

    img2_height =len(img2_mpl)
    img2_width  =len(img2_mpl[0])

    #---------converting it to a 1d array
    img1_1dArray=img1_gray.flatten()
    img2_1dArray=img2_gray.flatten()

    #--------------- displaying input
    save_img(img1_1dArray,img1_height,img1_width,'original_image1')
    save_img(img2_1dArray,img2_height,img2_width,'original_image2')

     # display_2grayimgs(img1_1dArray,img2_1dArray,img1_height,img1_width,img2_height,img2_width)

    #--------------- processing then display output
    new_height  =minimum(img1_height,img2_height)
    new_width   =minimum(img1_width,img2_width)
    img1,img2=process_1dImage(img1_gray,img2_gray,new_height,new_width)  

    save_img(img1,new_height,new_width,'output_image1')
    save_img(img2,new_height,new_width,'output_image2')                 
     # display_2grayimgs(img1,img2,new_height,new_width,new_height,new_width)


