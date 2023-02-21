from PIL import ImageChops, Image
import matplotlib.pyplot as plt 
import numpy as np
import os
import glob


path = 'dataset'
ndp_path = os.path.join(path + '/ndp/')
bit_path = os.path.join(path + '/bit/')

actual_error = 0
ndp_pro = []
bit_pro = []

def check(img):
    im1 = Image.open(img)
    x = np.array(im1.histogram())

    for file in glob.glob(ndp_path +'*'):

        im2 = Image.open(file)
        y = np.array(im2.histogram())

        try:
            if len(x) == len(y):
                error = np.sqrt(((x - y) ** 2).mean())
                error = str(error)[:2]
                actual_error = float(100) - float(error)
            diff = ImageChops.difference(im1, im2).getbbox()
            if diff:
                # print("Not Duplicate Image")
                # print('Matching Images In percentage: ', actual_error,'\t%' )
                f = plt.figure()
                text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
                plt.suptitle(text_lable)
                f.add_subplot(1,2, 1)
                plt.imshow(im1)
                f.add_subplot(1,2, 2)
                plt.imshow(im2)
                plt.show(block=True)
            else:
                # print("Duplicate Image")
                # print('Matching Images In percentage: ', actual_error,'%' )
                f = plt.figure()
                text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
                plt.suptitle(text_lable)
                f.add_subplot(1,2, 1)
                plt.imshow(im1)
                f.add_subplot(1,2, 2)
                plt.imshow(im2)
                plt.show(block=True)
            ndp_pro.append(actual_error)
        except ValueError as identifier:
            f = plt.figure()
            text_lable = str("Matching Images Percentage " + str(actual_error)+"%")
            plt.suptitle(text_lable)
            f.add_subplot(1,2, 1)
            plt.imshow(im1)
            f.add_subplot(1,2, 2)
            plt.imshow(im2)
            plt.show(block=True)
            # print('identifier: ', identifier)


    for file in glob.glob(bit_path + '*'):

        im2 = Image.open(file)
        y = np.array(im2.histogram())

        try:
            if len(x) == len(y):
                error = np.sqrt(((x - y) ** 2).mean())
                error = str(error)[:2]
                actual_error = float(100) - float(error)
            diff = ImageChops.difference(im1, im2).getbbox()
            if diff:
                # print("Not Duplicate Image")
                # print('Matching Images In percentage: ', actual_error,'\t%' )
                f = plt.figure()
                text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
                plt.suptitle(text_lable)
                f.add_subplot(1,2, 1)
                plt.imshow(im1)
                f.add_subplot(1,2, 2)
                plt.imshow(im2)
                plt.show(block=True)
            else:
                # print("Duplicate Image")
                # print('Matching Images In percentage: ', actual_error,'%' )
                f = plt.figure()
                text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
                plt.suptitle(text_lable)
                f.add_subplot(1,2, 1)
                plt.imshow(im1)
                f.add_subplot(1,2, 2)
                plt.imshow(im2)
                plt.show(block=True)
            bit_pro.append(actual_error)
        except ValueError as identifier:
            f = plt.figure()
            text_lable = str("Matching Images Percentage " + str(actual_error)+"%")
            plt.suptitle(text_lable)
            f.add_subplot(1,2, 1)
            plt.imshow(im1)
            f.add_subplot(1,2, 2)
            plt.imshow(im2)
            plt.show(block=True)
            # print('identifier: ', identifier)

    print(ndp_pro, bit_pro)
    if (max(ndp_pro) >= max(bit_pro)):
        return True
    else:
        return False

print(check("bit.jpg"))