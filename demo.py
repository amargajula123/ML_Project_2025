from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation


def main():
    try:
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
        #data_validation_config = Configuration().get_data_validation_config()
        #print(data_validation_config)
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        #schema_file_path=r"C:\Users\gajula Amar\python_ALL_projects\ML_Project_2025\config\schema.yaml"
        #file_path=r"C:\Users\gajula Amar\python_ALL_projects\ML_Project_2025\housing\artifact\data_ingestion\2025-02-16-13-26-27\ingested_data\train\housing.csv"

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path
        #)
        #print(df.columns)
        #print(df.dtypes)

        # +++++++++data_transformation++++++++++

        pipeline = Pipeline()
        pipeline.run_pipeline()



    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()