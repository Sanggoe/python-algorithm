import numpy as np
import cv2

img = np.full((500,500,3), 255, dtype=np.uint8)
cv2.imwrite('img/blank_500.jpg', img)