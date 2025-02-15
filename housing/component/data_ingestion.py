from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HosingException
import sys,os
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
from six.moves import urllib 

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HosingException(e,sys)
        
    
    def download_housing_data(self):
        try:
            download_url = data_ingestion_config.dataset_download_url
        except Exception as e:
            raise HosingException(e,sys)
        

    def extract_tgz_file(self):
        pass

    def split_data_as_train_test(self):
        pass