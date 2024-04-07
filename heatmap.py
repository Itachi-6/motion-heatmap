import cv2
from progress.bar import Bar
import numpy as np
import copy
from pathlib import Path
import re

#####################################################################################################################################################
#####################################################################################################################################################
## Helper functions to create video using frames


def sort_images(image_str):
    key = re.search(r'frame(\d+)', image_str)
    if key:
        return int(key.group(1))
    else:
        print('Did not find any match\n')

def video_from_frames(input_dir_frames, video_name):
    images = [str(img) for img in (list(Path(input_dir_frames).glob('*.jpg')))]
    images = sorted(images, key=sort_images)
    opencv_img = cv2.imread(str(images[0]))
    height, width, channels = opencv_img.shape

    video_writer_fourcc = cv2.VideoWriter.fourcc(*'mp4v')

    video_with_specs = cv2.VideoWriter(video_name, video_writer_fourcc, 30, (width, height))

    bar = Bar('Processing frame to Video....', max=len(images))

    for image in images:
        im = cv2.imread(str(image))
        video_with_specs.write(im)
        bar.next()
    
    bar.finish()
    cv2.destroyAllWindows()
    video_with_specs.release()
    
#####################################################################################################################################################
#####################################################################################################################################################





#####################################################################################################################################################
#####################################################################################################################################################
### Main script to create motion-heatmap frames

cap = cv2.VideoCapture('vid1/vid1.mp4')

#Initializing Background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=25, detectShadows=False)

#Initializing Bar from progress library
bar = Bar('Loading.... processing..', max=cap.get(cv2.CAP_PROP_FRAME_COUNT))

#Counter for reading the first frame for getting the height, width of the frame creation of Accumulation image. And also for saving each frame with its number.
i = 1
while cap.isOpened():
    #Reading the frames
    ret, frame = cap.read()
    

    if i == 1:

        first_frame = copy.deepcopy(frame)
        height, width = first_frame.shape[:2]

        #Creating accumulation image. This variable accumulates all pixels of previous frames which will help us to track it.
        accumulation_img = np.zeros((height, width), np.uint8)
        
        i += 1
        bar.next()

    #Since the i is initialized as 1 and index of frames starts with 0, we have to keep a break point when i reaches to the frame_count number.
    elif i == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        bar.next()
        break
    else:

        foreground = background_subtractor.apply(frame)


        _, threshold_img = cv2.threshold(foreground, 2, 2, cv2.THRESH_BINARY)  # only_background image, threshold value, max_value, threshold type

        accumulation_img = cv2.add(accumulation_img, threshold_img)

        color_frame = cv2.applyColorMap(accumulation_img, cv2.COLORMAP_HOT)

        final_frame = cv2.addWeighted(frame, 1, color_frame, 0.5, 0) # frame, frame_weight, color_frame, color_frame_weight, brightness
        cv2.imwrite(f'/home/dilipraj6/Dev/Environments/Heatmaps/vid1/final_frames/frame{i}.jpg', final_frame)
        i += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        bar.next()

bar.finish()

cap.release()
cv2.destroyAllWindows()

#After executing, you'll have all the final frames. Give the folder path the function below as 1st argument and the video name
video_from_frames('video_frames/', 'pushup_vid.mp4')

#####################################################################################################################################################
#####################################################################################################################################################