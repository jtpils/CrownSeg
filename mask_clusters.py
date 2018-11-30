from cv2 import bitwise_and
from configparser import ConfigParser
from scipy.io import loadmat, savemat

import logging

from utils.datapaths import *
from commons import get_mat_file_names, clean_create

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(message)s')
log = logging.getLogger(__file__)


def get_matching_file(m, clust_outs):
    for clust in clust_outs:
        if m[:8] in clust:
            return clust


if __name__ == "__main__":
    config = ConfigParser()
    config.read(CONFIG_FILE)
    algorithms = config['CLUSTERING']['ALGORITHMS'].split(',')
    for algo in algorithms:
        log.info('Algorithm=%s', algo)
        if algo == 'KMeans':
            log.info('Tackling KMeans Cluster Outputs')
            clean_create(KMEANS_MASKED_FOLDER_PATH[:-1])
            clust_outs = get_mat_file_names(KMEANS_FOLDER_PATH)
            ndvi_lidar_masks = get_mat_file_names(NDVI_LIDAR_FOLDER_PATH)
            for mask in ndvi_lidar_masks:
                clust = get_matching_file(mask, clust_outs)
                savemat(KMEANS_MASKED_FOLDER_PATH + 'MASKED_' + clust, {'image': bitwise_and(
                    src1=loadmat(KMEANS_FOLDER_PATH + clust)['image'].astype(int), src2=loadmat(NDVI_LIDAR_FOLDER_PATH + mask)['image'].astype(int))})
        elif algo == 'FCM':
            log.info('Tackling FCM Cluster Outputs')
            clean_create(FCM_MASKED_FOLDER_PATH[:-1])
            clust_outs = get_mat_file_names(FCM_FOLDER_PATH)
            ndvi_lidar_masks = get_mat_file_names(NDVI_LIDAR_FOLDER_PATH)
            for mask in ndvi_lidar_masks:
                clust = get_matching_file(mask, clust_outs)
                savemat(FCM_MASKED_FOLDER_PATH + 'MASKED_' + clust, {'image': bitwise_and(
                    src1=loadmat(FCM_FOLDER_PATH + clust)['image'].astype(int), src2=loadmat(NDVI_LIDAR_FOLDER_PATH + mask)['image'].astype(int))})
        elif algo == 'SOM':
            log.info('Tackling SOM Cluster Outputs')
            clean_create(SOM_MASKED_FOLDER_PATH[:-1])
            clust_outs = get_mat_file_names(SOM_FOLDER_PATH)
            ndvi_lidar_masks = get_mat_file_names(NDVI_LIDAR_FOLDER_PATH)
            for mask in ndvi_lidar_masks:
                clust = get_matching_file(mask, clust_outs)
                savemat(SOM_MASKED_FOLDER_PATH + 'MASKED_' + clust, {'image': bitwise_and(
                    src1=loadmat(SOM_FOLDER_PATH + clust)['image'].astype(int), src2=loadmat(NDVI_LIDAR_FOLDER_PATH + mask)['image'].astype(int))})
        elif algo == 'GMM':
            log.info('Tackling GMM Cluster Outputs')
            clean_create(GMM_MASKED_FOLDER_PATH[:-1])
            clust_outs = get_mat_file_names(GMM_FOLDER_PATH)
            ndvi_lidar_masks = get_mat_file_names(NDVI_LIDAR_FOLDER_PATH)
            for mask in ndvi_lidar_masks:
                clust = get_matching_file(mask, clust_outs)
                savemat(GMM_MASKED_FOLDER_PATH + 'MASKED_' + clust, {'image': bitwise_and(
                    src1=loadmat(GMM_FOLDER_PATH + clust)['image'].astype(int), src2=loadmat(NDVI_LIDAR_FOLDER_PATH + mask)['image'].astype(int))})
        elif algo == 'Spectral':
            log.info('Tackling Spectral Cluster Outputs')
            clean_create(SPECTRAL_MASKED_FOLDER_PATH[:-1])
            clust_outs = get_mat_file_names(SPECTRAL_FOLDER_PATH)
            ndvi_lidar_masks = get_mat_file_names(NDVI_LIDAR_FOLDER_PATH)
            for mask in ndvi_lidar_masks:
                clust = get_matching_file(mask, clust_outs)
                savemat(SPECTRAL_MASKED_FOLDER_PATH + 'MASKED_' + clust, {'image': bitwise_and(
                    src1=loadmat(SPECTRAL_FOLDER_PATH + clust)['image'].astype(int), src2=loadmat(NDVI_LIDAR_FOLDER_PATH + mask)['image'].astype(int))})
    log.info('Execution Complete')
