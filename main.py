## entire training pipeline will be create over here

from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1 import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2 import DataTransformationTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info("initate pipeline stage 1{STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info("stage completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data trabsformation stage"

try:
    logger.info("initate pipeline stage 1{STAGE_NAME}")
    data_ingestion_pipeline = DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info("stage completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e