# Function: Create GIF image with each frame having user specified duration time.

import os
import re

import imageio


# 1. Specify user settings.

# Set the path of input/output images.
PATH_INPUT_IMAGE = 'IMAGE/'
PATH_OUTPUT_IMAGE = 'IMAGE_GIF/'

# Create the path for saving output images.
# Check if the path exists. If not, create it.
if os.path.exists(PATH_OUTPUT_IMAGE) is False:
    os.mkdir(PATH_OUTPUT_IMAGE)

# Set the format of input static images.
FORMAT_INPUT_IMAGE = '.png'

# Set the name of output GIF images.
GIF_NAME_SAME = "imgGIF_SAME.gif"
GIF_NAME_DIFF = "imgGIF_DIFF.gif"

# Set the duration time of each frame in GIF image.
DURATION_TIME_FRAME = 0.5

# Set the repeat times of the first and the last frames in GIF image.
REPEAT_TIMES_FRAME = 3

# Set the pattern for creating GIF image.
PATTERN_GIF_IMAGE = 2
# Note:
#     PATTERN_GIF_IMAGE = 1 - Create GIF image with each frame having the same duration time.
#     PATTERN_GIF_IMAGE = 2 - Create GIF image with each frame having different duration time.


# 2. Create GIF image.

print('\nStart creating GIF image...')

if PATTERN_GIF_IMAGE == 1:
    # 2.1 Create GIF image with each frame having the SAME duration time.

    print('\nPattern: %d - Each frame of GIF image has the same duration time.' % PATTERN_GIF_IMAGE)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    # Note:
    #     The serial number in the input image name should have the same length (e.g., '00', '01', ...).
    #     If not, the 'sorted()' function will return the wrong order of image names.

    for imgName in imgNames:
        imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_SAME, imgGIF, duration=DURATION_TIME_FRAME)

elif PATTERN_GIF_IMAGE == 2:
    # 2.2 Create GIF image with the first and the last frames having LONG duration time.

    print('\nPattern: %d - Each frame of GIF image has different duration time.' % PATTERN_GIF_IMAGE)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    # Note:
    #     The serial number in the input image name should have the same length (e.g., '00', '01', ...).
    #     If not, the 'sorted()' function will return the wrong order of image names.

    for imgName in imgNames:
        tmpName = re.split(r"[_.]", imgName)[2]  # 'tmpName' <str>
        # Note:
        #     Split image name by '_' and '.'.
        #     Select the 2-nd part of image name (i.e., '00', '01', ...).

        if tmpName == '00' or tmpName == '99':
            # '00' in _00.png - The first frame in GIF image.
            # '99' in _99.png - The last frame in GIF image.
            tt = 0
            while tt < REPEAT_TIMES_FRAME:
                imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))
                tt += 1
        else:
            imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_DIFF, imgGIF, duration=DURATION_TIME_FRAME)

print('\nComplete!\n')
