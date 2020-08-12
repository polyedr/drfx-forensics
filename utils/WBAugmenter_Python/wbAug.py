#####################################################################################
# Copyright (c) 2019-present, Mahmoud Afifi
#
# This source code is licensed under the license found in the LICENSE file in the
# root directory of this source tree.
#
# Please, cite the following paper if you use this code:
# Mahmoud Afifi and Michael S. Brown. What else can fool deep learning? Addressing
# color constancy errors on deep neural network performance. ICCV, 2019
#
# Email: mafifi@eecs.yorku.ca | m.3afifi@gmail.com
######################################################################################

import os
import argparse
import utils.WBAugmenter_Python.WBAugmenter.WBEmulator as wbAug
from drfx.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL

def parse_args():
    parser = argparse.ArgumentParser(description="WB color augmenter")
    p = parser.add_argument
    p("--input_image_filename", help="Input image's full filename (for a single image augmentation)")
    p("--input_image_dir", help="Training image directory (use it for batch processing)")
    p("--out_dir", help="Output directory")
    p("--out_number", type=int, default=10, help="Number of output images for each input image")
    p("--write_original", type=int, default=1, help="Save copy of original image(s) in out_dir")
    p("--ground_truth_dir", help="Ground truth directory")
    p("--out_ground_truth_dir", help="Output directory for ground truth files")
    p("--ground_truth_ext", help="File extension of ground truth files")
    return parser.parse_args()

def augment_images(**kwargs):
    wbColorAug = wbAug.WBEmulator()  # create an instance of the WB emulator
    # args = parse_args()  # parse input arguments
    args = {
            'input_image_filename' : None,
            'input_image_dir' : None,
            'out_dir' : None,
            'out_number' : 10,
            'write_original' : 1,
            'ground_truth_dir' : None,
            'out_ground_truth_dir' : None,
            'ground_truth_ext' : None,
    }

    args.update(kwargs)
    if args["input_image_dir"] is not None and args["ground_truth_dir"] is not None:  # if input and ground truth directories are provided, augment training/ground truth files
        if args["out_dir"] is None:
            args["out_dir"] = MEDIA_ROOT + "/training_new"
        if args["out_ground_truth_dir"] is None:
            args["out_ground_truth_dir"] = MEDIA_ROOT + "/ground_truth_new"
        os.makedirs(args["out_dir"], exist_ok=True)  # create output training directory (if not exist)
        os.makedirs(args["out_ground_truth_dir"], exist_ok=True)  # create output ground truth directory (if not exist)
        wbColorAug.trainingGT_processing(args["input_image_dir"], args["out_dir"], args["ground_truth_dir"],
                                         args["out_ground_truth_dir"], args["ground_truth_ext"], args["out_number"],
                                         args["write_original"])
    elif args["input_image_dir"] is not None:  # if input directory provided, then do batch processing -- process all images inside this directory
        if args["out_dir"] is None:
            args["out_dir"] = MEDIA_ROOT + "/results"
        os.makedirs(args["out_dir"], exist_ok=True)  # create output directory (if not exist)
        wbColorAug.batch_processing(args["input_image_dir"], args["out_dir"], args["out_number"], args["write_original"])
    else: # process a single image
        if args["out_dir"] is None:
            args["out_dir"] = MEDIA_ROOT + "/results"
        os.makedirs(args["out_dir"], exist_ok=True)
        paths = wbColorAug.single_image_processing(args["input_image_filename"], args["out_dir"], args["out_number"],
                                           args["write_original"])
        print("MEDIA_ROOT", MEDIA_ROOT)
        print("MEDIA_URL", MEDIA_URL)
        print(paths)
        return paths
