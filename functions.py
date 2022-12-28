from glob import glob
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')
class images:

    def resize_images(img1, img2):
        # ----------------Resizing
        img1_resized = cv2.resize(img1, (500, 500))
        img2_resized = cv2.resize(img2, (500, 500))
        cv2.imwrite("static/assets/images/front/resized_img1.png", img1_resized)
        cv2.imwrite("static/assets/images/front/resized_img2.png", img2_resized)
        return img1_resized, img2_resized


    def cropping_fourier(F_img1, choice_img1, F_img2, choice_img2, cropping_indecies):

        F1_2d = F_img1
        F2_2d = F_img2

        left1 = cropping_indecies[0]
        top1 = int(cropping_indecies[1]*500/300)
        width1 = cropping_indecies[2]
        height1 = int(cropping_indecies[3]*500/300)
        left2 = cropping_indecies[4]
        top2 = int(cropping_indecies[5]*500/300)
        width2 = cropping_indecies[6]
        height2 = int(cropping_indecies[7]*500/300)

        chosen_part1 = F1_2d[top1:top1+height1, left1:left1+width1]
        chosen_part2 = F2_2d[top2:top2+height2, left2:left2+width2]

        if(choice_img1 == 1):
            rejected_part1 = F1_2d*0
            rejected_part1 =np.exp(1j*rejected_part1)
        elif (choice_img1 == 0):
            rejected_part1 =np.ones((500,500))

        if(choice_img2 == 1):
            rejected_part2 = F2_2d*0
            rejected_part2 =np.exp(1j*rejected_part2)

        elif (choice_img2 == 0):
            rejected_part2=np.ones((500,500))


        print(rejected_part1)
        print(rejected_part2)

        result1 = rejected_part1.copy()
        result2 = rejected_part2.copy()

        result1[top1:top1+height1, left1:left1+width1] = chosen_part1
        result2[top2:top2+height2, left2:left2+width2] = chosen_part2

        return result1, result2


    def Process_images(img1, img2, choices):
        print("---------------------------choices", choices)

        # -------------- fourier transform
        f = np.fft.fft2(img1)
        f = np.fft.fftshift(f)
        f2 = np.fft.fft2(img2)
        f2 = np.fft.fftshift(f2)

        if (choices[8] == 1 and choices[9] == 1):
            print("choice1 phase choice2 phase")
            f, f2 = images.cropping_fourier(
                np.exp(1j*np.angle(f)), 1, np.exp(1j*np.angle(f2)), 1, choices)
            combined_img1 = np.multiply(f, f2)

        elif (choices[8] == 0 and choices[9] == 1):
            print("choice1 mag choice2 phase")
            f, f2 = images.cropping_fourier(
                np.abs(f), 0, np.exp(1j*np.angle(f2)), 1, choices)
            combined_img1 = np.multiply(f, f2)

        elif (choices[8] == 1 and choices[9] == 0):
            print("choice1 phase choice2 mag")
            f, f2 = images.cropping_fourier(
                np.exp(1j*np.angle(f)), 1, np.abs(f2), 0, choices)
            combined_img1 = np.multiply(f, f2)
            print(combined_img1)

        elif (choices[8] == 0 and choices[9] == 0):
            print("choice1 mag choice2 mag")
            f, f2 = images.cropping_fourier(np.abs(f), 0, np.abs(f2), 0, choices)
            combined_img1 = np.multiply(f, f2)

        imgCombined = np.real(np.fft.ifft2(np.fft.fftshift(combined_img1)))
        cv2.imwrite("static/assets/images/outputs/output_image1.png", imgCombined)

        return imgCombined


    def read_images(cropped_indecies):

        # --------reading files by matplot and opencv
        print("-----------------------------------------------------------------start")
        images_files = glob('static/assets/images/inputs/*.jpg')
        print(images_files)
        img_file1 = 'static/assets/images/inputs/input_image0.png'
        img_file2 = 'static/assets/images/inputs/input_image1.png'

        img1_mpl = plt.imread(img_file1)
        img1_cv2 = cv2.imread(img_file1)
        img2_mpl = plt.imread(img_file2)
        img2_cv2 = cv2.imread(img_file2)

        # -------- gray scaled
        img2_gray = cv2.cvtColor(img2_cv2, cv2.COLOR_RGB2GRAY)
        img1_gray = cv2.cvtColor(img1_cv2, cv2.COLOR_RGB2GRAY)

        # ---------resize images
        img1, img2 = images.resize_images(img1_gray, img2_gray)
        images.Process_images(img1, img2, cropped_indecies)

    def download_img(img_name,index):
        img=cv2.imread('static/assets/images/upload/'+img_name)
        images.save_img(img,index)
        return

    def save_img(img_1d,index):
        img_2d=cv2.resize(img_1d, (500, 500))
        cv2.imwrite("static/assets/images/inputs/input_image"+str(index)+'.png', img_2d)

# -----------------------------------------Cropping in time ---------------------=

# def minimum(a, b):
#     if a <= b:
#         return a
#     else:
#         return b

# def save_img(img_1d, index):
#     img_2d = cv2.resize(img_1d, (500, 500))
#     cv2.imwrite("static/assets/images/inputs/input_image" +
#                 str(index)+'.png', img_2d)

# def blur_image(img, cropped_indecies, file_name):
#     print(cropped_indecies)
#     left = cropped_indecies[0]
#     top = cropped_indecies[1]
#     width = cropped_indecies[2]
#     height = cropped_indecies[3]

#     kept_part = img[top:top+height, left:left+width]
#     blurred_part = cv2.blur(img, ksize=(30, 30))
#     result = blurred_part.copy()
#     result[top:top+height, left:left+width] = kept_part
#     cv2.imwrite("static/assets/images/after_blurring/" +
#                 file_name+'.png', result)
#     print('doneeeee')
#     return result

# def process_1dImage(img1_gray, img2_gray, img_height, img_width):

#     # ----------------Resizing
#     img1_resized = cv2.resize(img1_gray, (img_width, img_height))
#     img2_resized = cv2.resize(img2_gray, (img_width, img_height))
#     # ---------converting it to a 1d array
#     img1_1dArray = img1_resized.flatten()
#     img2_1dArray = img2_resized.flatten()
#     # -------------- fourier transform
#     f = np.fft.fft(img1_1dArray)
#     f2 = np.fft.fft(img2_1dArray)

#     combined_img1 = np.multiply(np.abs(f), np.exp(1j*np.angle(f2)))
#     combined_img2 = np.multiply(np.abs(f2), np.exp(1j*np.angle(f)))

#     imgCombined1 = np.real(np.fft.ifft(combined_img1))
#     imgCombined2 = np.real(np.fft.ifft(combined_img2))

#     return imgCombined1, imgCombined2

# def read_2images(cropped_indecies):

#     # --------reading files by matplot and opencv
#     images_files = glob('static/assets/images/inputs/*.jpg')
#     img_file1 = 'static/assets/images/inputs/input_image0.png'
#     img_file2 = 'static/assets/images/inputs/input_image1.png'

#     img1_mpl = plt.imread(img_file1)
#     img1_cv2 = cv2.imread(img_file1)
#     img1_gray = cv2.cvtColor(img1_cv2, cv2.COLOR_RGB2GRAY)
#     cv2.imwrite("static/assets/images/outputs/original_img1.png", img1_gray)

#     img2_mpl = plt.imread(img_file2)
#     img2_cv2 = cv2.imread(img_file2)
#     img2_gray = cv2.cvtColor(img2_cv2, cv2.COLOR_RGB2GRAY)
#     cv2.imwrite("static/assets/images/outputs/original_img2.png", img2_gray)

#     # --------getting height width
#     img1_height = len(img1_mpl)
#     img1_width = len(img1_mpl[0])

#     img2_height = len(img2_mpl)
#     img2_width = len(img2_mpl[0])

#     # --------------- processing then display output
#     new_height = minimum(img1_height, img2_height)
#     new_width = minimum(img1_width, img2_width)

#     if(cropped_indecies[1] == 0):
#         print('nothing')
#         # img1_gray=blur_image(img1_gray,[100,100,150,250],'blurr1')
#         # img2_gray=blur_image(img2_gray,[100,100,150,250],'blurr2')

#     else:
#         img1_gray = blur_image(img1_gray, cropped_indecies[:4], 'blurr1')
#         img2_gray = blur_image(img2_gray, cropped_indecies[4:], 'blurr2')

#     img1, img2 = process_1dImage(img1_gray, img2_gray, new_height, new_width)

#     save_img(img1, new_height, new_width, 'output_image1')
#     save_img(img2, new_height, new_width, 'output_image2')

#     # display_2grayimgs(img1,img2,new_height,new_width,new_height,new_width)


# def download_img(img_name, index):
#     img = cv2.imread('static/assets/images/inputs/'+img_name)
#     save_img(img, index)
#     return

# def crop(self, corodinates):
