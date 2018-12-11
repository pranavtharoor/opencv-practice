import cv2

img_color = cv2.imread('media/opencv.png')
img_unchanged = cv2.imread('media/opencv.png', -1)
img_grayscale = cv2.imread('media/opencv.png', 0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow('image', img_color)
cv2.waitKey(0)
cv2.imshow('image', img_unchanged)
cv2.waitKey(0)
cv2.imshow('image', img_grayscale)
cv2.waitKey(0)

cv2.imwrite('./out/img_color.png', img_color)
cv2.imwrite('./out/img_unchanged.png', img_unchanged)
cv2.imwrite('./out/img_grayscale.png', img_grayscale)

cv2.destroyAllWindows()
