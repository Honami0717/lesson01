import cv2

img = cv2.imread ('./maple.jpg',cv2.IMREAD_REDUCED_COLOR_2)

print(img.shape, ima.size)

roi = img2(150:490, 450:600)
img(100:200, 300:450) = roi

cv2.imshow('maple', img)
cv2.waitKey(0)
cv2.destroyAllWindows()