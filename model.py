import numpy as np
from PIL import Image
from keras.models import load_model
from io import BytesIO
import base64

model = load_model('mnist.h5')


def pre_pic(picName):
    # Сначала откройте входящее исходное изображение
    img = Image.open(BytesIO(base64.b64decode(picName)))
    # Меняем размер изображения методом сглаживания
    reIm = img.resize((28, 28), Image.ANTIALIAS)
    # Убираем цвета, преобразуем в матрицу
    im_arr = np.array(reIm.convert("L"))
    return im_arr


def process_image(picName):
    # предобработка изображения, ресайз и преобразование в серое
    image = pre_pic(picName)
    # Меняем размерность на ту, которую принимает модель
    image = image.reshape((1, 28, 28, 1))
    # Нормализуем значения цвета 
    image = image.astype('float32')/255
    # Получаем ответ от модели
    predict = model.predict(image)[0].argmax()
    return predict