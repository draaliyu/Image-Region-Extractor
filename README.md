# Image-Region-Extractor


ImageRegionExtractor is a Python-based tool that allows users to interactively select regions of an image, cut them out, and save the extracted regions as new image files. This program is very useful for tasks such as object extraction, dataset creation, manual feature extraction and more.
Getting Started

# Prerequisites
You will need Python 3.7+ and OpenCV installed on your machine. You can install OpenCV using pip:
    pip install opencv-python

Run the script:
python ImageRegionExtractor.py


A window will appear displaying the first image from the specified directory.

Select a region in the image by left-clicking and dragging your mouse. When you release the mouse button, the selected region will be saved as a new image with a timestamp appended to the filename to avoid overwriting previous cutouts.

Press 'n' to move to the next image. If there are no more images, a message will be printed in the console.

Press 'q' to quit the program.
