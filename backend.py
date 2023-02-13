from PIL import Image
import numpy as np
import cv2 
import matplotlib.pyplot as plt
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
from tensorflow import keras

"""Carga de documentos"""
# load and prepare the image
def cargarImagen(filename):
  # load the image
  img = load_img(filename, target_size=(224, 224))
  # convert to array
  img = img_to_array(img)
  # reshape into a single sample with 3 channels
  img = img.reshape(1, 224, 224, 3)
  # center pixel data
  #img = img.astype('float32')
  #img = img - [123.68, 116.779, 103.939]
  
  return img

class FixedDropout(keras.layers.Dropout):
    def call(self, inputs, training=None):
        return super().call(inputs, training=True)

custom_objects = {
    "FixedDropout": FixedDropout,
}


  # load an image and predict the class
def run_example(filemane):
 # load the image
  img = cargarImagen(filemane)
 # load model
  with keras.utils.custom_object_scope(custom_objects):
    model = keras.models.load_model("model_tf.h5")
 # predict the class
  result = model.predict(img)
  result = np.round(result)
  result = [columna for fila in result for columna in fila]
  r = get_category(result)
  if(r=="Pan" or r=="Postres" or r=="Comida rapida" or r=="Sopa"):
    res = "Comida no saludable ha sido clasificado como: "+r
  else:
    res = "Comida saludable ha sido clasificado como: "+r
  print(result)
  return res


categories = ["Pan", "Productos diarios", "Postres", "Huevos", "Comida rapida","Carne","Pasta","Arroz","Mariscos","Sopa","Vegetales-frutas"]

def get_category(vector):
    try:
        index = vector.index(1)
        return categories[index]
    except ValueError:
        return "Categoría no encontrada"
