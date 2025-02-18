from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HosingException
from housing.entity.artifact_entity import DataIngestionArtifact,\
DataValidationArtifact,DataTransformationArtifact,ModelTrainerArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
from housing.component.model_trainer import ModelTrainer
import os,sys





class Pipeline:
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
        
    def start_data_validation(self,
                              data_ingestion_artifact:DataIngestionArtifact
                              )->DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
            )
            return data_validation.initiate_data_validaton()
        
        except Exception as e:
            raise HosingException(e,sys) from e
    
    def start_data_transformation(self,
                                  data_ingestion_artifact:DataIngestionArtifact,
                                  data_validation_artifact:DataValidationArtifact
                                  )->DataTransformationArtifact:
        
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact= data_ingestion_artifact,
                data_validation_artifact= data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
    
        except Exception as e:
            raise HosingException(e,sys) from e

    def start_model_trainer(self,
                            data_ingestion_artifact:DataIngestionArtifact,
                            data_validation_artifact:DataValidationArtifact,
                            data_transformation_artifact:DataTransformationArtifact
                            )->ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config =self.config.get_model_trainer_config(),
                data_ingestion_artifact= data_ingestion_artifact,
                data_validation_artifact= data_validation_artifact,
                data_transformation_artifact = data_transformation_artifact
                )
            return model_trainer.initiate_model_trainer()
        except Exception as e:
            raise HosingException(e,sys) from e

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise HosingException(e,sys) from e

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise HosingException(e,sys) from e
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact= data_ingestion_artifact,
                                                                          data_validation_artifact=data_validation_artifact)
            
        except Exception as e:
            raise HosingException(e,sys) from e


        