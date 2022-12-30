from glob import glob
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')
# img1 path
# img2 path


class image:
    def __init__(self, img ,index):

        self.image = img  #image readed by cv2 
        self.index=index  #image number to be named with 


    def resize_image(self):
        # ----------------Resizing
        self.image = cv2.resize( self.image, (500, 500))
        cv2.imwrite('static/assets/images/front/resized_img'+str(self.index)+'.png',  self.image)

    def getFourier(self):
        fourier = np.fft.fft2(self.image)
        fourier = np.fft.fftshift(fourier)
        return fourier
        
    def gray_scale(self):
        # truning colored image to gray
        self.image=cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    



class ImageProcessing():

    def __init__(self, cropping_indecies):
        self.cropping_indecies = cropping_indecies

    def read_images(self):

        # --------reading files by matplot and opencv

        img_file1 = 'static/assets/images/inputs/input_image0.png'
        img_file2 = 'static/assets/images/inputs/input_image1.png'

        img1_cv2 = cv2.imread(img_file1)
        img2_cv2 = cv2.imread(img_file2)

        # creating objects

        img1 =image(img1_cv2,index=1)
        img2 =image(img2_cv2,index=2)

        img1.gray_scale()
        img2.gray_scale()

        img1.resize_image()
        img2.resize_image()

        fourier1=img1.getFourier()
        fourier2=img2.getFourier()

        self.Process_2images(fourier1,fourier2)

    def Process_2images(self,img1_fourier,img2_fourier):

        if  (self.cropping_indecies[8] == 0 and self.cropping_indecies[9] == 1):  
            print("choice1 mag choice2 phase")
            fourier1, fourier2 = self.cropping_fourier(np.abs(img1_fourier), np.exp(1j*np.angle(img2_fourier)))
            combined_img1 = np.multiply(fourier1, fourier2)

        elif (self.cropping_indecies[8] == 1 and self.cropping_indecies[9] == 0):
            print("choice1 phase choice2 mag")
            fourier1, fourier2 = self.cropping_fourier(np.exp(1j*np.angle(img1_fourier)), np.abs(img2_fourier))
            combined_img1 = np.multiply(fourier1, fourier2)
            print(combined_img1)


        imgCombined = np.real(np.fft.ifft2(np.fft.fftshift(combined_img1)))
        cv2.imwrite("static/assets/images/outputs/output_image1.png", imgCombined)

        return imgCombined

    def cropping_fourier(self, F_img1, F_img2):

        choice_img1=self.cropping_indecies[8]
        choice_img2=self.cropping_indecies[9]

        F1_2d = F_img1
        F2_2d = F_img2

        #  indecies extraction and manipulation

        left1 = self.cropping_indecies[0]
        top1 = int(self.cropping_indecies[1]*500/300)
        width1 = self.cropping_indecies[2]
        height1 = int(self.cropping_indecies[3]*500/300)
        left2 = self.cropping_indecies[4]
        top2 = int(self.cropping_indecies[5]*500/300)
        width2 = self.cropping_indecies[6]
        height2 = int(self.cropping_indecies[7]*500/300)

        # using indecies to show inside and outside part

        inside_part1 = F1_2d[top1:top1+height1, left1:left1+width1]
        outside_part1 = F1_2d
        inside_part2 = F2_2d[top2:top2+height2, left2:left2+width2]
        outside_part2 = F2_2d

        if(self.cropping_indecies[10] == 0):
            # if user chooses inside the box
            chosen_part1 = inside_part1
            chosen_part2 = inside_part2

            if(choice_img1 == 1):
                rejected_part1 = outside_part1*0
                rejected_part1 = np.exp(1j*rejected_part1)
            elif (choice_img1 == 0):
                rejected_part1 = np.ones((500, 500))

            if(choice_img2 == 1):
                rejected_part2 = outside_part2*0
                rejected_part2 = np.exp(1j*rejected_part2)

            elif (choice_img2 == 0):
                rejected_part2 = np.ones((500, 500))

            print(rejected_part1)
            print(rejected_part2)

            result1 = rejected_part1.copy()
            result2 = rejected_part2.copy()

            result1[top1:top1+height1, left1:left1+width1] = chosen_part1
            result2[top2:top2+height2, left2:left2+width2] = chosen_part2

        if(self.cropping_indecies[10] == 1):

            # if user chooses outside the box

            chosen_part1 = outside_part1
            chosen_part2 = outside_part2
            
            # choice of an image ==1 phase selection
            # choice of an image ==0 magnitude selection
           
            if(choice_img1 == 1):
                rejected_part1 = inside_part1*0
                rejected_part1 = np.exp(1j*rejected_part1)
            elif (choice_img1 == 0):
                rejected_part1 = np.ones((height1, width1))

            if(choice_img2 == 1):
                rejected_part2 = inside_part2*0
                rejected_part2 = np.exp(1j*rejected_part2)

            elif (choice_img2 == 0):
                rejected_part2 = np.ones((height2, width2))

            result1 = chosen_part1.copy()
            result2 = chosen_part2.copy()

            result1[top1:top1+height1, left1:left1+width1] = rejected_part1
            result2[top2:top2+height2, left2:left2+width2] = rejected_part2


        return result1, result2

