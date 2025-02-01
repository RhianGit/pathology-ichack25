from flask import *
import json
import requests as rq
from PIL import Image
import cv2 as cv
import numpy as np
from io import BytesIO
from model import process
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/transform")
def transform():
    url = request.args.get("url")
    print(url)
    rsp = rq.get(url)
    image = Image.open(BytesIO(rsp.content))

    out = process(image)

    enc = cv.imencode(".png", out)[1].tobytes()
    rsp = make_response(enc)
    rsp.headers.set('Content-Type', 'image/png')
    rsp.headers.set(
        'Content-Disposition', 'attachment', filename='frame.png')
    return rsp
