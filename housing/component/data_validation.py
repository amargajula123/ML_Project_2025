from housing.config.configuration import Configuration
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.exception import HosingException
import os,sys



class DataValidation:
    

    def __init__(self,data_validation_config:DataValidationConfig,
                      data_ingestion_artifact:DataIngestionArtifact):
        self.data_validation_config  = data_validation_config
        self.data_ingestion_artifact = data_ingestion_artifact
        try:
            pass
        except Exception as e:
            raise HosingException(e,sys) from e
        
    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            
            # Assigment validate traing and testing dataset using file
            #1. Number of Colum
            #2. Check the value of ocean proximity
            #3. Check column names
            validation_status = True
            
            return validation_status
        except Exception as e:
            raise HosingException(e,sys) from e


    # checking train and test file available or not in 
    def is_train_test_file_exists(self)->bool:
        try: 
            logging.info(f"Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False
            
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
          
            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist  = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            logging.info(f"is train and test file is exist?-> {is_available}")

            if not is_available:
                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Training file:[{training_file}] and Testing file: [{testing_file}]\
                    is not prasent "
                
                raise Exception(message)
            
            return is_available

        except Exception as e:
            raise HosingException(e,sys) from e
        
    def initiate_data_validaton(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            
        except Exception as e:
            raise HosingException(e,sys) from e
    