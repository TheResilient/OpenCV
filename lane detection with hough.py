import cv2
from matplotlib import pyplot as plt
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color=255
    cv2.fillPoly(mask, vertices,match_mask_color)
    masked_image= cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_img, (x1,y1),(x2,y2), (255,0,0), 2)
    img=cv2.addWeighted(img, 0.8, line_img, 1, 0.0)
    return img

img=cv2.imread('road.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
height=img.shape[0]
width=img.shape[1]

region_of_interest_vertices= [
    (0,height),
    (width/2,height/2),
    (width,height)
]

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray, 100,100)


cropped_image = region_of_interest(canny, np.array([region_of_interest_vertices], np.int32))
lines=cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)
image_with_lines=draw_lines(img,lines)

plt.imshow(image_with_lines)
plt.show()
