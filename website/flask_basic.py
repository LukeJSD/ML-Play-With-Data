"""A simple example flask application
"""
from flask import Flask, jsonify, request, render_template
import numpy as np
import joblib
import cv2
import traceback
import utils

# clear_session()
app = Flask(__name__)
iris_model = None
mnist_model = None
all_american_model = None


# def load_iris_model():
#     global iris_model
#     # Step 1: Determine file location
#     model_file = 'models/sk-model.joblib'
#     # Step 2: Load model
#     iris_model = joblib.load(model_file)

# def load_mnist_model():
#     global mnist_model
#     model_file = 'models/keras-mnist.h5'
#     mnist_model = load_model(model_file)

def load_all_american_model():
    global all_american_model
    model_file = 'models/all-american-model-2.joblib'
    all_american_model = joblib.load(model_file)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json")
def json_endpoint():
    return jsonify({
        "message": "Hello World!"
    })


@app.route("/variables/<variable>")
def example_variable(variable):
    return jsonify({
        "message": f"The variable you entered is {variable}"
    })

@app.route("/request-args")
def example_request_args():
    try:
        a = request.args["a"]
        b = request.args["b"]
        c = request.args["c"]
        return jsonify({
            "message": f"You entered a = {a}, b= {b} and c= {c}."
        })
    except:
        return jsonify({
            "message": f"You did not provide one of a, b, or c."
        })

# @app.route("/iris")
# def predict_iris():
#     # To predict the iris species we need:
#     # sepal length in cm - sepal_length
#     # sepal width in cm - sepal_width
#     # petal length in cm - petal_length
#     # petal width in cm - petal_width
#     try:
#         sl = request.args["sepal_length"]
#         sw = request.args["sepal_width"]
#         pl = request.args["petal_length"]
#         pw = request.args["petal_width"]
#     except:
#         return jsonify({
#             "message": f"You did not provide one of sepal_length, sepal_width, petal_length, or petal_width."
#         })
#     vector = np.array([sl, sw, pl, pw])
#     pred = iris_model.predict([vector])
#     classes = ["Setosa","Versicolour","Virginica"]
#     species = classes[pred[0]]
#     return jsonify({
#         "message": f"The predicted species for the observations you entered is {species} ",
#         "species": species
#     })


# @app.route("/iris-ui")
# def iris_ui():
#     return render_template("iris.html")
    

# @app.route("/mnist", methods=["POST"])
# def mnist_predict():
#     try:
#         image =  request.files['file'].read()
#         print("Got image")
#         # https://stackoverflow.com/a/27537664/818687
#         arr = cv2.imdecode(np.fromstring(image, np.uint8), cv2.IMREAD_UNCHANGED)
#         print("CV2 read image")
#         my_image = arr / 255.0
#         my_images = my_image.reshape(1, 28, 28, 1)
#         print("Got here")

#         pred = mnist_model.predict(my_images)
#         n = int(np.argmax(pred))
#         print(n)
#         return jsonify({
#             "message": f"The predicted number for the uploaded image is {n} ",
#             "number": n
#         })
#     except Exception as e:
#         print(traceback.format_exc())
#         return jsonify({
#             "message": f"An error occurred. {e}"
#         })

# @app.route("/mnist-ui")
# def mnist_ui():
#     return render_template("mnist.html")


@app.route("/all_american")
def all_american_predict(): 
    # To predict an all american  we need:
    # Pr's in events: 10k, 8k, 5k, 3k, mile, 1500
    # Championship wins 
    # Time since PR: years 
    # idk stuff
    try:
        distance = request.args["distance"]
        time = request.args["time"]
        champs = request.args["championships"]
        season = request.args["season"]
        time_since_pr = request.args["time_since_pr"]
    except:
        return jsonify({
            "message": f"You did not provide one of Distance, Time, Time_since_pr, Season, Championships."
        })
    # Fix time 
    h,m,s = time.split(':')
    time = int(h) * 3600 + int(m) * 60 + int(s)
    # Fix distance
    if distance == '1500':
        distance = 1500
    elif distance == 'Mile':
        distance = 1609 
    elif distance == '3k':
        distance = 3000
    elif distance == '5k':
        distance = 5000
    elif distance == '8k':
        distance = 8000
    else:
        distance = 10000
    # Fix season 
    if season == 'XC':
        season = 0
    elif season == 'Indoor Track':
        season = 1
    else:
        season = 2
    vector = np.array([[distance, season, time, time_since_pr, champs]])
    vector = vector.astype(np.float64)
    pred = all_american_model.predict(vector)
    return jsonify({
        "message": f"Your chance at being an all american are {pred[0]} ",
        "pred": pred[0]
    })

@app.route("/all-american-ui")
def all_american_ui():
    return render_template("all_american.html")

if __name__ == '__main__':
    # load_iris_model()
    # load_mnist_model()
    load_all_american_model()
    app.run(debug=True)