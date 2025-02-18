from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation


def main():
    try:
        # +++++++++get_model_trainer_config() Check++++++++++
        model_traine_config = Configuration().get_model_trainer_config()
        print(model_traine_config)
        # +++++++++get_model_trainer_config() Done++++++++++

        # +++++++++get_data_transformation_config() Check++++++++++
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
        # +++++++++get_data_transformation_config() Done++++++++++

        # +++++++++get_data_validation_config() Check++++++++++
        #data_validation_config = Configuration().get_data_validation_config()
        #print(data_validation_config)
        # +++++++++get_data_validation_config() Done++++++++++

        # +++++++++get_data_ingestion_config() Check++++++++++
        #data_ingestion_config = Configuration().get_data_ingestion_config()
        #print(data_ingestion_config)
        # +++++++++get_data_ingestion_config() Done++++++++++



        
        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path
        #)
        #print(df.columns)
        #print(df.dtypes)
        

        # +++++++++ CHECK ANY COMPONENT ++++++++++

        #pipeline = Pipeline()
        #pipeline.run_pipeline()

        # +++++++++CHECK ANY COMPONENT DONE++++++++++



    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()