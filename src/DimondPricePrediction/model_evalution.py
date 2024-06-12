import os
import sys
from sklearn.metrics  import mean_squared_error,mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.DimondPricePrediction.utils.utils import load_object

class ModelEvalutaion:
    def __init__(self):
        pass

    def eval_metrics(self,actual,pred):
        rmse= np.sqrt(mean_squared_error(actual,pred))
        mae= mean_absolute_error(actual,pred)
        r2= r2_score(actual,pred)
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_test,y_test=(
                test_array[:,:-1],
                train_array[:,-1]
            )
        

            model_path =os.path.join("artifacts","model.pkl")
            model = load_object(model_path)

            mlflow.set_registry_uri("https://dagshub.com/bhaskarmaddala/MLProjectEndtoEnd.mlflow")

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():

                predicted_qualities = model.predict(X_test)

                (rmse, mae,r2) = self.eval_metrics(y_test,predicted_qualities)

                mlflow.log_metrics("rmse",rmse)
                mlflow.log_metrics("r2",r2)
                mlflow.log_metrics("mae",mae)

                #model registry does not work with file store
                if tracking_url_type_store != "file":
                     
                     #Register the model
                     #there are other ways to use the model Registry , which depends in the use case ,
                     #please refer to the doc fot more information
                     #https://mlflow.org/docs/latest/model-registry.html#api-workflow
                     mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model,"model")
        except Exception as e:
            raise e
                