import argparse
from io import BytesIO
import os
from PIL import Image

from min_dalle.generate_image import generate_image_from_text

from flask import Flask, send_file
app = Flask(__name__)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/get-image', methods=['GET','POST'])
def get_image():
    # text = request.form['text']

    image = generate_image_from_text(
      text = "Hello World!",
      # is_mega = args.mega,
      # is_torch = args.torch,
      # seed = args.seed,
      # image_token_count = args.image_token_count
    )
    
    return serve_pil_image(image)

if __name__ == '__main__':
    app.run()