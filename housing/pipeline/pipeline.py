from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HosingException
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion




class Pipeline(self);
    def __init__(self,config: Configuration=Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HosingException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
             
            # initiate_data_ingestion() here we have download data Split data Read data we have 
            # we used download_housing_data() funtion for downoad data
            # we used extract_tgz_file() function for extract "housing file" data
            # we used split_data_as_train_test() fuction for split the data int trai and test and store at
            # ingested_train_dir and ingested_test_dir
            return data_ingestion.initiate_data_ingestion() 
        except Exception as e:
            raise HosingException(e,sys) from e
        
    def start_data_validation(self):
        pass
    
    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass
    
    def start_model_pusher(self):
        pass
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HosingException(e,sys) from e


        