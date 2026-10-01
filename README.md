# AI-Powered Nutrition Analyzer for Fitness Enthusiasts

Upload a photo of a fruit and get its nutrition facts. A CNN classifies the image (apple, banana, orange, pineapple, watermelon), then the app looks up calories and macros through the CalorieNinjas API.

Built as part of the IBM Nalaiya Thiran program (project IBM-Project-22536, team PNT2022TMID26372, 2022) by Keerthana VS, Maya Padhy, Madhubala R, Rasika M and Roszhan Raj MS. The model was trained with TensorFlow/Keras and deployed with IBM Watson Machine Learning.

## Structure
- `app.py`: Flask app (upload → predict with `nutrition.h5` → nutrition lookup)
- `templates/`, `Static/`: web UI
- `Sample_Images/`: test images to try
- `training/`: model-building and IBM Cloud deployment notebooks
- `docs/project-report.pdf`: final project report

## Run

```sh
pip install flask tensorflow requests
export RAPIDAPI_KEY=your-rapidapi-key        # CalorieNinjas on RapidAPI
python app.py
```

The IBM Cloud deployment notebook reads `IBM_CLOUD_API_KEY` from the environment.
