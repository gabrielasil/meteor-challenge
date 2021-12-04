import cv2 as cv

img = cv.imread("meteor_challenge_01.png")

white = (255, 255, 255)

#OpenCV uses BGR color format
red = (0, 0, 255)
blue = (255, 0, 0)

stars = 0
meteors = 0
temp_meteors = 0
meteors_in_water = 0
is_water = 0


#.shape of OpenCV returns a tuple with the number of rows, columns, and channels (if the image is color)
print(img.shape[0], img.shape[1])

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if(tuple(img[j, i]) == white):
            stars += 1

        if(tuple(img[j, i]) == red):
            temp_meteors += 1
        
        if(tuple(img[j, i]) == blue):
            is_water = 1
            break

    if is_water == 1:
        meteors_in_water = temp_meteors + meteors_in_water
        is_water = 0
    meteors += temp_meteors
    temp_meteors = 0
    temp_stars = 0
    is_star = 0
    is_meteor = 0

print("Stars: " + str(stars))
print("Meteors: " + str(meteors))
print("Meteors in water: " + str(meteors_in_water))
