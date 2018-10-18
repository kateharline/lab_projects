# import python packages
import os

# import imagej packages
from ij import IJ
from ij import WindowManager as WM

# change these w each run #
input_path = '/Users/kateharline/Documents/roeder_lab/imaging/leaf_live_beta/pAR169xpAR229_20180823'

# probably don't change -- unless you are changing code functionality
start_extension = '.lsm'
new_extension = '.tif'

def load(path):
    IJ.open(path)
    img = WM.getCurrentImage()
    return img

def process(filename, output_path):
    IJ.run("Z Project...", "projection=[Max Intensity]");
    # the number of channels is one (orig image) less than the number of images opened
    IJ.saveAs("Tiff", os.path.join(output_path, 'maxint_'+ str(i+1) + '_' + filename))
    curr_img.close()
    return

def batch_process(extension, source_dir):
    for folder, subs, files in os.walk(source_dir):
        output_path = os.path.join(folder, 'channels_separated')
        for filename in files:
            if filename.endswith(extension):
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                img = load(os.path.join(folder, filename))
                process(filename, output_path)
                img.close()
    return

batch_process(start_extension, input_path)
