import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Sathyarajpalle/kidney-disease-classification-deeplearning.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Sathyarajpalle"
os.environ["MLFLOW_TRACKING_PASSWORD"]="aea301ec4baa449a3878623b93dbb8d54ba0f358"

from cnnClasifier import logger
from cnnClasifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClasifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClasifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClasifier.pipeline.stage_04_model_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e