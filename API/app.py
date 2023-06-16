#Import Library
from PIL import Image
import numpy as np
import tensorflow as tf
import base64

#Import Flask
from flask import Flask, request, render_template, jsonify

#Load Flask
app = Flask(__name__)

#Load model
model = tf.keras.models.load_model("FinalModel_V1.h5")

#Define classes list
class_list = ['Ayam', 'Bawang Merah', 'Bawang Putih', 'Kambing', 'Lele', 'Sapi', 'Tahu',
              'Telur', 'Tempe', 'Udang']

#Preprocess the image before predicting
def preprocessing(image):
    image = image.resize((256, 256))
    arr = np.array(image)
    arr = (arr - arr.min()) / (arr.max() - arr.min())
    arr = np.expand_dims(arr, axis=0)
    return arr

#Checking if the application is running
@app.route("/")
def main():
    return """
    Application is Running
    """

#The index page (You can change this if you want)
@app.route("/index")
def postsPage():
    return render_template("index.html")

#The result page (You can change this if you want)
@app.route("/result", methods=["POST"])
def predict():
    image = request.files["pic"]
    image = Image.open(image)
    image = preprocessing(image)
    predicted = model.predict(image)
    class_name = class_list[np.argmax(predicted)]

    #The prediction result will be shown as class name
    return jsonify({"result" : class_name})

@app.route("/result2", methods=["POST"])
def predict():
    image_data = request.form.get("image_data")
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    image = preprocessing(image)
    predicted = model.predict(image)
    class_name = class_list[np.argmax(predicted)]

    return jsonify({"prediction": class_name})


if __name__ == '__main__':
    try:
        app.run(port=5000, debug=True)
    except:
        print("Server is exited unexpectedly. Please contact server admin.")
