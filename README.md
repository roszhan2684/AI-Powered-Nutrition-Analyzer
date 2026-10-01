<div align="center">

# AI-Powered Nutrition Analyzer

**Snap a fruit, get its nutrition facts. A deep-learning image classifier plus a live nutrition API, built for fitness enthusiasts who'd rather not look everything up.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow%20%2F%20Keras-CNN-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=flat-square&logo=flask&logoColor=white)
![IBM](https://img.shields.io/badge/IBM%20Watson-ML%20Deployment-054ADA?style=flat-square&logo=ibm&logoColor=white)

<img src="docs/screenshots/upload.jpg" width="760" alt="Upload a fruit photo to classify" />

</div>

---

## The problem

Tracking what you eat is tedious: search a database, guess the serving, copy the numbers. For whole foods like fruit, a photo should be enough.

## How it works

<img src="docs/screenshots/fruits.jpg" width="760" alt="The five fruit classes" />

1. **Upload a photo.** The web app previews it instantly.
2. **Classify.** A convolutional neural network trained on five fruit classes (apples, bananas, oranges, pineapples, watermelons) predicts what's in the picture.
3. **Get the nutrition.** The predicted food is sent to the **CalorieNinjas** API, and its nutrition record (calories, protein, carbohydrates, fat, sugar, fibre and more) is shown alongside the prediction.

## Model results

<img src="docs/screenshots/predictions.jpg" width="640" alt="Model predictions on the sample images" />

On the bundled sample images, the model gets **6 of 6 right**. Reproduce it with:

```sh
python docs/classify_samples.py
```

## Tech

| Layer | Details |
|---|---|
| Model | Keras CNN on 64×64 RGB images, trained with `ImageDataGenerator` augmentation (`training/`) |
| Serving | Flask app (`app.py`) loading `nutrition.h5`, with upload → predict → nutrition lookup |
| Nutrition data | CalorieNinjas via RapidAPI |
| Cloud | Model trained and deployed with IBM Watson Studio / Watson Machine Learning (`training/model_training_on_ibm_cloud.ipynb`) |

## Run it locally

```sh
pip install flask tensorflow pillow requests
export RAPIDAPI_KEY=your-rapidapi-key        # CalorieNinjas on RapidAPI
python app.py                                # → http://127.0.0.1:5000
```

Try it with the photos in `Sample_Images/`.

## Team

Built for the IBM Nalaiya Thiran program (project IBM-Project-22536, team PNT2022TMID26372, 2022) by **Keerthana VS, Maya Padhy, Madhubala R, Rasika M and Roszhan Raj MS**. The full write-up is in [`docs/project-report.pdf`](docs/project-report.pdf).
