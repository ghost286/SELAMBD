import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pymongo

# Define a function to preprocess the images
def preprocess_image(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

# Define a function to extract features
def extract_features(image):
    return [cv2.contourArea(cnt) for cnt in cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]]

# Define a function to load images from a database
def load_images_from_database():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mammograms"]
    collection = db["images"]
    images = [cv2.imdecode(np.fromstring(image['data'], np.uint8), cv2.IMREAD_GRAYSCALE) for image in collection.find()]
    return images

# Define a function to split the dataset
def split_dataset(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == '__main__':
    # Load the mammograms from a database
    mammograms = load_images_from_database()

    # Preprocess the images and extract features
    X = []
    y = []
    for mammogram in mammograms:
        preprocessed_image = preprocess_image(mammogram)
        features = extract_features(preprocessed_image)
        X.append(features)
        if 'cancerous' in mammogram['tags']:
            y.append(1)
        else:
            y.append(0)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Train the model
    model = Pipeline([
        ('preprocessing', preprocess_image),
        ('classification', LogisticRegression())
    ])
    model.fit(X_train, y_train)

    # Test the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)

    # Calculate probability for a new mammogram
    new_mammogram = cv2.imread('new_mammogram.jpg', 0)
    preprocessed_new_mammogram = preprocess_image(new_mammogram)
    features_new_mammogram = extract_features(preprocessed_new_mammogram)
    probability = model.predict_proba(np.array([features_new_mammogram]).T)[0][1]

    # Display results
    print('Probability of cancer:', probability)