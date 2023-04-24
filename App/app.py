# Приложение для прогнозирования "соотношения матрица-наполнитель" в рамках ВКР по курсу Data Science 2023 МГТУ им. Баумана.
# Импорт
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
from flask import Flask, request, render_template
app = Flask(__name__)

# Загружаем модель и определяем параметры функции  -  будущие входы для модели (всего 12 параметров)

def set_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12):

    model = keras.models.load_model("/ideal_model/")
    #model = pickle.dump(model, open("model1.pkl", "wb"))
    prediction = model.predict([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12])

    return prediction[0][0]
@app.route('/', methods=['POST', 'GET'])

#@app.route('/index', methods=['POST', 'GET'])

def app_calculation():
    param_lst = []
    message = ''
    if request.method == 'POST':
        
       # получим данные из наших форм и кладем их в список, который затем передадим функции set_params
        for i in range(1,13,1):
            param = request.form.get(f'param{i}')
            param_lst.append(float(param))
            
        message = set_params(*param_lst)

    # указываем шаблон и прототип сайта для вывода    
    return render_template("index.html", message=message) 

# # Запускаем приложение  
app.run()
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)