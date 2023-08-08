import cv2



image_path = "C:/Users/sidda/OneDrive/Desktop/py/pexels-eberhard-grossgasteiger-534164.jpg"

image = cv2.imread(image_path)



gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



cv2.imshow('Original Image', image)

cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows(
