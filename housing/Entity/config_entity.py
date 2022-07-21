from collections import namedtuple

## Download url
## download folder (this a compressed file)
## extract folder (the folder is decompressed and file is extracted from it)
## train dataset folder
## test dataset folder 


TrainingPipelineConfig = namedtuple(typename="TrainingPipelineConfig",field_names=["artifact_dir"]) 


DataIngestionConfig = namedtuple(typename = "DataIngestionConfig",field_names=["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])




DataValidationConfig = namedtuple(typename="DataValidationConfig",field_names=["schema_file_path","report_file_path","report_page_file_path"])



DataTransformationConfig = namedtuple(typename="DataTransformationConfig",
field_names=["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])





ModelTrainerConfig = namedtuple(typename = "DataTrainerConfig", field_names = ["trained_model_file_path","base_accuracy","model_config_file_path"])




ModelEvaluationConfig = namedtuple(typename = "DataEvaluationConfig", field_names = ["model_evaluation_file_path","time_stamp"])




ModelPusherConfig = namedtuple(typename = "DataPusherConfig", field_names = ["export_dir_path"])


TrainingPipelineConfig = namedtuple(typename = "TrainingPipelineConfig", field_names = ["artifact_dir"])
