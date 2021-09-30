import numpy as np
from PIL import Image
from keras.models import load_model
import os
# model_path = os.path.join(os.getcwd(),'')
model = load_model('mnist.h5')

def pre_pic(picName):
    # Сначала откройте входящее исходное изображение
    img = Image.open(picName)
         # Используйте метод сглаживания, чтобы изменить размер изображения
    reIm = img.resize((28,28),Image.ANTIALIAS)
         # Стать изображением в оттенках серого, преобразовать в матрицу
    im_arr = np.array(reIm.convert("L"))
    return im_arr


def process_image(picName):
    image = pre_pic(picName)
    
    image = image.reshape((1,28,28,1))
    image = image.astype('float32')/255
    
    predict = model.predict(image)[0].argmax()
    return predict