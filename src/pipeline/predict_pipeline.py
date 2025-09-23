import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: float,
                 writing_score: float):

        # Ensure all inputs are scalars
        self.gender = str(gender) if gender is not None else ""
        self.race_ethnicity = str(race_ethnicity) if race_ethnicity is not None else ""
        self.parental_level_of_education = str(parental_level_of_education) if parental_level_of_education is not None else ""
        self.lunch = str(lunch) if lunch is not None else ""
        self.test_preparation_course = str(test_preparation_course) if test_preparation_course is not None else ""
        self.reading_score = float(reading_score) if reading_score is not None else 0.0
        self.writing_score = float(writing_score) if writing_score is not None else 0.0

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
    "gender": [str(self.gender)],
    "race_ethnicity": [str(self.race_ethnicity)],
    "parental_level_of_education": [str(self.parental_level_of_education)],
    "lunch": [str(self.lunch)],
    "test_preparation_course": [str(self.test_preparation_course)],
    "reading_score": [float(self.reading_score)],
    "writing_score": [float(self.writing_score)],
}


            # Debug: confirm all values are scalars inside lists
            print("DEBUG: DataFrame input dict:", custom_data_input_dict)

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
