from housing.config.configuration import Configuration
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact

from housing.exception import HosingException
import os,sys
import pandas as pd
import json

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
# with the help of these 2 evidently models we can generate json report
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
# with this modules we see evidently.dashboard.tabs import DataDriftTab

class DataValidation:
    

    def __init__(self,data_validation_config:DataValidationConfig,
                      data_ingestion_artifact:DataIngestionArtifact):
        self.data_validation_config  = data_validation_config
        self.data_ingestion_artifact = data_ingestion_artifact
        try:
            pass
        except Exception as e:
            raise HosingException(e,sys) from e
        
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df,test_df
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
        
    
    def get_and_save_data_drift_report(self):
        try:
            # profile object for we wanted to check the data drift 
            # so that we created "object" of Profile(sections=[DataDriftProfileSection()])
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df) # -> generates datadrift report as json format
                                                # profile.json() # -> datadrift report as json format
            report = json.loads(profile.json()) # -> we get kind of dictionary format

            report_file_path = self.data_validation_config.report_file_path
            # making report_dir folder
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            # loading report json into report_dir(report.json) folder
            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)
            return report
        except Exception as e:
            raise HosingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path=self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise HosingException(e,sys) from e
        
    # for datadrift check  
    def is_data_drift_found(self)->bool:
        try:
            self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise HosingException(e,sys) from e
    
    def initiate_data_validaton(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
            schema_file_path = self.data_validation_config.schema_file_path,
            report_file_path = self.data_validation_config.report_file_path,
            report_page_file_path = self.data_validation_config.report_page_file_path,
            is_validated=True,
            message=f"Data Validation perform Successfully. "

        )
            logging.info(f"Data Validation Artifact: [{data_validation_artifact}]")
            return data_validation_artifact
        except Exception as e:
            raise HosingException(e,sys) from e
    