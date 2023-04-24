# DS-composites
# Прогнозирование конечных свойств новых композитных материалов
Выпускная квалификационная работа по курсу «Data Science» 

в Образовательном Центре МГТУ им. Н.Э. Баумана по теме: 

"Прогнозирование конечных свойств композитных материалов".

Целью данной работы является разработка пользовательского приложения для прогнозирования характеристики конечных свойств новых композиционных материалов.

1)	По ходу исследования изучены теоретические основы работы по направлению DataScience, краткая теория о композитных материалах, способы решения задачи, а именно: 
Прогнозировать на основании имеющихся входных параметров конечных свойств получаемых композиционных материалов при следующих используемых признаках: 

    •	Соотношение матрица-наполнитель
    •	Плотность, кг/м3
    •	Модуль упругости, ГПа
    •	Количество отвердителя, м.%
    •	Содержание эпоксидных групп,%_2
    •	Температура вспышки, С_2
    •	Поверхностная плотность, г/м2
    •	Потребление смолы, г/м2
    •	Прочность при растяжении, МПа
    •	Потребление смолы, г/м2
    •	Угол нашивки, град
    •	Шаг нашивки
    •	Плотность нашивки

2)	Проведен разведочный анализ, подготовлена визуализация входных данных в виде гистограммы распределения каждой из переменной, диаграмм ящика с усами, попарные графики рассеяния точек. В таблице представлены для каждой колонки среднее, медианное значение. Выполнено исследование на наличие выбросов и определен метод работы с ними, проверена выборка на наличие пропусков.

3)	Проведена предобработка данных.

4)	Обучено нескольких моделей для прогноза модуля упругости при растяжении и прочности при растяжении. При построении модели было 30% данных оставлено на тестирование модели, на остальных происходило обучение моделей:

* методом опорных векторов

* методом случайного леса

* методом линейной регрессии

* методом градиентного бустинга

* методом К ближайших соседей

* методом деревья решений

* методом стохастического градиентного спуска

* методом многослойного перцептрона

* методом лассо регрессии


5)	Написана нейронная сеть, которые рекомендует соотношение "матрица-наполнитель".

6)	Разработано пользовательское приложение на Flask, выдаваемое прогноз (Выходные данные (прогнозируемы) - Соотношение "матрица - наполнитель").

7)	Оценена точность модели на тренировочном и тестовом датасете.

8)	Создан репозиторий в GitHub и размещен код исследования.

9) Оформлен данный файл README

Входные и выходные данные представлены в нормализованном виде. 
В ходе исследования было предположено, что существует неочивидная взаимосвязь между переменными, через производные параметры не использованные в датасете. Доказать/опровергнуть данную гипотезу возможно только при наличии расширенного датасета.

Структура репозитория:

Research - папка содержит:
- 2 входными файлами - датасетами X_bp.xlsx, X_nup.xlsx;
- Файла Requirements.txt с актуальными версиями использованных библиотек;
- Файл The code.ipynb содержащий в себе непосредственно выполненное исследование.

App - папка с файлами для работы пользовательского приложения + само приложение

Инструкция по работе с приложением:

Приложение позволяет решать задачу прогнозирования "Соотношение матрица наполнитель". 
Для получения прогноза необходимо 

1. запустить app.py. Рекомедую запускать в приложении VSCode.

2. Совершить запуск без отладки.

3. Пройти в браузере по адресу http://127.0.0.1:5000/.

4. Заполнить значения параметров в соответствии с подписями ячеек и нажать "Спрогнозировать".

5. Внизу таблицы будет выведен результат работы модели в виде числового значения с плавающей точкой. 


Автор: Пестерев Михаил Андреевич

Выпускная квалификационная работа по программе повышения квалификации «Data Science» в обучающем центре МГТУ им. Н. Э. Баумана
2023 г. 
