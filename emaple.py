# import flast module
from flask import Flask ,request
from api.src import service
from api.src.routes import blueprint
# instance of flask application
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello"
@app.route("/verify", methods=["POST"])
def verify():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img1_path = input_args.get("img1") or input_args.get("img1_path")
    img2_path = input_args.get("img2") or input_args.get("img2_path")

    # print(img1_path+"fdffsdf")

    if img1_path is None:
        return {"message": "you must pass img1_path input"}

    if img2_path is None:
        return {"message": "you must pass img2_path input"}



    verification = service.verify(img1_path, img2_path)



    return verification




if __name__ == '__main__':
    app.run()