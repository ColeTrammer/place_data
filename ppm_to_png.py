import cv2
import sys

ppm_path = 'result.ppm'
output_path = 'result.png'

if len(sys.argv) >= 2:
    ppm_path = sys.argv[1]
if len(sys.argv) >= 3:
    output_path = sys.argv[2]

img = cv2.imread(ppm_path)
cv2.imwrite(output_path, img)
