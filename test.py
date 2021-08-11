import cv2

img = cv2.imread('./maple.jpg', 1)

cv2.imshow('./maple.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./maple.jpg',img)