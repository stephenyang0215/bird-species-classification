import streamlit as st
from PIL import Image
from io import BytesIO
import tensorflow as tf
import numpy as np
import requests

st.title("475 Bird Species - Image Classification")
dataset = 'https://www.kaggle.com/datasets/gpiosenka/100-bird-species'
st.write("Kaggle Data source : [Link](%s)" % dataset)
def exec(model_path, class_path):
    with open() as f:
        lines = f.read().splitlines()
    classes = lines[0].split(',')
    with st.spinner('Wait for it...Loading ML model!'):
        model = tf.keras.models.load_model(model_path)
        st.success('Done!')
    return model, classes
model_path = 'models/'
class_path = 'bird_species.txt'
model, classes = exec(model_path, class_path)

def decode_img(image):
  image = tf.image.decode_jpeg(image, channels=3)  
  image = tf.image.resize(image,[224,224])
  image = np.expand_dims(image, axis=0)
  return image

path = st.text_input('Paste your url of the image : ',
'https://storage.googleapis.com/kagglesdsdata/datasets/534640/4957101/test/ABBOTTS%20BABBLER/1.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230210%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230210T183345Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=9a44eeea7b75adf263aa08e517b0a021e8a54ba27577abcbdee6455697eb5afa19c956636b9b3c620fcea9236733efad2fa34276f4825f754b512d0a0db9000381fd0c65ec7533406e3be8974b73aec37598e23c5a586c07c61ce4bf5585a5f6c1ea37752da685fdf0a1f7132e402c95ca53e725a957dd587dbdf974e47bd04a9c38106a0a405346bf0353b123a26910549bffb33e7123e27e57a8e439241d0bc6182c80774e53d4349e59a908d5c3d6a49d6af81c14f88094fa7e32678ef945c359343c9b1b594c7300cd3ffe0a7dfab95ff1042352450fdb352e3615841aefd2d5fd286ee3a0c8ed4df004ddcd4c509e0b4322531cff6740814d7330ae9b7e')
if path is not None:
    image_content = requests.get(path).content

    st.write("Predicted Bird Species :")
    with st.spinner('Generating output : '):
      label =np.argmax(model.predict(decode_img(image_content)),axis=1)
      st.write(classes[label[0]])    
    image = Image.open(BytesIO(image_content))
    st.image(image)

st.markdown(f"475 bird species names for image search : {classes}")
