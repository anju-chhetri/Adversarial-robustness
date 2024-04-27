import cv2
import numpy as np
from matplotlib import pyplot as plt

fn3= '/home/anju_chhetri/Downloads/pexels-michael-li-483163181-20755700.jpg'

def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.uint8(ycbcr)

def show(im):
    plt.imshow(im)
    plt.show()


img = cv2.imread(fn3)
imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y,Cr,Cb = cv2.split(imgYCrCb)
onlycr = imgYCrCb.copy()
onlycr[:,:,0] = 128
onlycr[:,:,2] = 128
onlycr_as_bgr = cv2.cvtColor(onlycr, cv2.COLOR_YCrCb2BGR)
onlyCb = imgYCrCb.copy()
onlyCb[:, :, 0] = 128
onlyCb[:, :, 1] = 128
onlyCb_as_bgr = cv2.cvtColor(onlyCb, cv2.COLOR_YCrCb2BGR)  # Convert to BGR - used for display as false color

cv2.imshow('img', img)
cv2.imshow('Y', Y)
cv2.imshow('onlyCb_as_bgr', onlyCb_as_bgr)
cv2.imshow('onlyCr_as_bgr', onlycr_as_bgr)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('/home/anju_chhetri/Downloads/Y.png', Y)
cv2.imwrite('/home/anju_chhetri/Downloads/onlyCb_as_bgr.png', onlyCb_as_bgr)
cv2.imwrite('/home/anju_chhetri/Downloads/onlyCr_as_bgr.png', onlycr_as_bgr)
# # image = cv2.imread(fn3)
# # im = rgb2ycbcr(image)
# # show(im)
# img1 = cv2.imread(fn3)
# img2=np.zeros(img1.shape,np.uint8)
# img2[:,:,0]=img1[:,:,2]
# img2[:,:,1]=img1[:,:,1]
# img2[:,:,2]=img1[:,:,0]
# transcol=cv2.cvtColor(img1, cv2.COLOR_BGR2YCrCb)
# plt.figure()
# plt.subplot(2,3,1)
# plt.imshow(img1[:,:,2], cmap = "Reds")
# plt.title('Red')
# plt.subplot(2,3,2)
# plt.imshow(img1[:,:,1], cmap = "Greens")
# plt.title('Green')
# plt.subplot(2,3,3)
# plt.imshow(img1[:,:,0], cmap = "Blues")
# plt.title('Blue')

# plt.subplot(2,3,4)
# plt.imshow(transcol[:,:,0],cmap="gray")
# plt.title('Luminance Y')
# plt.subplot(2,3,5)
# plt.imshow(transcol[:,:,1],cmap="Reds")
# plt.title('Chrominance Cr')
# plt.subplot(2,3,6)
# plt.imshow(transcol[:,:,2],cmap="Blues")
# plt.title('Chrominance Cb')
# plt.show()
