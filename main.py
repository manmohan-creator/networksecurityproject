from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging

import sys
if __name__=="__main__":
    try:
        trainingpipelineconfig= TrainingPipelineConfig()
        dataingestionconfig =DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("initiate data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation complete")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)