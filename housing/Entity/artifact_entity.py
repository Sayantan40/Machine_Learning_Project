from collections import namedtuple

DataIngestionArtifact = namedtuple(typename="DataIngestionArtifact",field_names=["train_file_path","test_file_path","is_ingested","message"])
## the "is_ingested" clarifies whether the data has ingested on the pipeline or not.


DataValidationArtifact = namedtuple(typename="DataValidationArtifact",field_names=["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])



DataTransformationArtifact = namedtuple(typename="DataTransformationArtifact",field_names=["is_transformed", "message", "transformed_train_file_path","transformed_test_file_path","preprocessed_object_file_path"])



ModelTrainerArtifact = namedtuple(typename="ModelTrainerArtifact",field_names= ["is_trained", "message", "trained_model_file_path","train_rmse","test_rmse","train_accuracy","test_accuracy","model_accuracy"])



ModelEvaluationArtifact = namedtuple(typename="ModelEvaluationArtifact", field_names=["is_model_accepted", "evaluated_model_path"])



ModelPusherArtifact = namedtuple(typename="ModelPusherArtifact",field_names= ["is_model_pusher", "export_model_file_path"])