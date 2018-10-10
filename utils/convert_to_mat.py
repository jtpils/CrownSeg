import argparse
import logging
from os import listdir, mkdir, rmdir, sep
from os.path import abspath, dirname, isfile, join
from shutil import rmtree

import numpy
from scipy.io import savemat

import gdal
from datapaths import DATASET_PATH, HYPER_FOLDER_PATH, LIDAR_FOLDER_PATH, RGB_FOLDER_PATH

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(message)s')
log = logging.getLogger(__file__)


def get_file_names(source_path):
    return sorted([f for f in
                   [f for f in listdir(source_path) if isfile(
                       join(source_path, f))]
                   if 'tif' in f and 'aux.xml' not in f])


def cast_to_mat(input_files, source_path, dest_path):
    log.info('Casting .tiff to .mat')
    for f in input_files:
        # Read GeoTIFF Hyperspectral Image Files
        image = gdal.Open(
            source_path + f).ReadAsArray().T
        # Normalize
        image /= image.max()
        # Write as .mat file
        savemat(dest_path + f.split('.')
                [0] + '.mat', {'image': image})


def get_configured_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-type', default='hyper', dest='file_type',
                        choices=['rgb', 'hyper', 'lidar'], help="rgb, hyper or lidar")
    return parser


if __name__ == "__main__":
    log.info('Starting Execution')
    parser = get_configured_parser()
    args = parser.parse_args()

    if args.file_type == 'hyper':
        # Read HyperImage filenames
        input_files = get_file_names(HYPER_FOLDER_PATH)
        source_path = HYPER_FOLDER_PATH
    elif args.file_type == 'lidar':
        # Read LIDAR filenames
        input_files = get_file_names(LIDAR_FOLDER_PATH)
        source_path = LIDAR_FOLDER_PATH
    else:
        # Read RGB filenames
        input_files = get_file_names(RGB_FOLDER_PATH)
        source_path = RGB_FOLDER_PATH

    log.info('Deleting Output Directory Contents if any exist recursively')
    try:
        rmtree(source_path + 'MAT')
    except FileNotFoundError as e:
        log.info("Out Directory doesn't exist. Gonna create one.")
    # Create Output Directory
    mkdir(source_path + 'MAT')

    cast_to_mat(input_files, source_path, source_path + 'MAT' + sep)
    log.info('Execution Complete')