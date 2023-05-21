import cv2
import numpy as np
import os

# global variables
ix, iy = -1, -1
drawing = False
img = None
img_copy = None
img_index = 0
image_files = []

from datetime import datetime

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = img_copy.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        new_img = img_copy[iy:y, ix:x]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Get current date and time
        cv2.imwrite(f'./images/cutout_{timestamp}.png', new_img)

def main():
    global img, img_copy, img_index, image_files

    # read image files from directory
    directory_path = './imgae_data' # replace with your directory path
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.jpg', '.png'))]
    if not image_files:
        print("No image files found in the directory.")
        return

    img = cv2.imread(os.path.join(directory_path, image_files[img_index])) # load the first image
    img_copy = img.copy()

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'): # press 'q' to quit
            break
        elif k == ord('n'): # press 'n' to go to next image
            img_index += 1
            if img_index < len(image_files): # if there are more images
                img = cv2.imread(os.path.join(directory_path, image_files[img_index]))
                img_copy = img.copy()
            else:
                print("No more images left.")
                img_index -= 1

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
