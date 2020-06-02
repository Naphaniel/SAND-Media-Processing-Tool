# Import system packages
import os
import sys
import json

from packages import VideoProcessing
from packages import SAND

with open('parameters.json') as json_file:
    DATA = json.load(json_file)

# Getting parameters from parameters JSON doc
VIDEO_NAME = DATA['videoName']
UNPROCESSED_PATH = DATA['unprocessedImageDir']
PROCESSED_PATH = DATA['processedImageDir']
MODEL_NAME = DATA['sandModel']
SPLIT_FLAG = DATA['splitVideoFlag']
SAND_FLAG = DATA['SANDProcessFlag']
COMBINE_FLAG = DATA['combineImagesFlag']
IMG_INDEX_RANGE = DATA['imgIndexRange']
VIDEO_NO_TYPE = VIDEO_NAME.split('.')[0]


if not os.path.exists(UNPROCESSED_PATH) or not os.path.exists(PROCESSED_PATH):
    sys.exit('File paths do not exist')


def main():
    vp_wrapper = VideoProcessing(
        VIDEO_NAME, UNPROCESSED_PATH, PROCESSED_PATH)
    sand_wrapper = SAND(UNPROCESSED_PATH + '/' + VIDEO_NO_TYPE,
                        PROCESSED_PATH + '/' + VIDEO_NO_TYPE, MODEL_NAME, IMG_INDEX_RANGE)
    if SPLIT_FLAG:
        vp_wrapper.split_video()
    elif SAND_FLAG:
        sand_wrapper.process_image()


if __name__ == '__main__':
    main()
