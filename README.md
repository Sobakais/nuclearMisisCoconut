## Обнаружение курения в запрещенных зонах

### Название команды: MISIScoconut

#### Участники команды:
- <a href="https://t.me/dmmmit">Дмитрий Уросов</a>
- <a href="https://t.me/mishka_gumer">Михаил Гумиров</a>
- <a href="https://t.me/cvvup">Мария Хайдукова</a>
- <a href="https://t.me/FFHKJQ">Синицын Данил</a>

#### Обзор
 Цель - обучить модель YOLOv8 для обнаружения того, курит ли человек в запрещенной зоне на скриншотах с видеокамер наблюдения. Обнаружение курения в запрещенных зонах может помочь в соблюдении политики запрета курения и улучшении соблюдения этого правила.


#### Ход работы
  Сперва мы решили взять доступные датасеты в интернете и обучить модель по ним. В датасете было около 3000 размеченных изображений, около 1000 мы разметили самостоятельно. После обучения модели по этому датасету, мы получили не очень хорошие результаты. Сигареты на представленном заказчиками датасете определялась плохо. На фоне 3 тыс изображений, 76 представленных замыливались. Из-за этого мы получали не очень хороший результат.

<p align="center">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/BigDataMetrica1.jpg" alt="Метрика-1" style="width: 48%;">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/BigDataMetrica2.jpg" alt="Метрика-2" style="width: 48%">
</p>
<p align="center">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/BigDataMetrica3.jpg" alt="Метрика-3" style="width: 48%;">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/BigDataMetrica4.jpg" alt="Метрика-4" style="width: 48%;">
</p>

- ![BigData NOTEBOOK](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/notebooks/BigData.ipynb)
- ![BigData Model](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/models/big_data_model.pt)


  В ходе работы мы решили провести исследование. В темное время суток, когда силуэт человека и сигареты тяжело зафиксировать камере видеонаблюдения, детектить сигарету можно по горящему концу. В темноте его будет видно как четко выражающийся красный объект. Для исследования мы создали свой датасет. Сфотографировались на плохо освещенной территории с подоженной сигаретой. Далее, полученные изображения мы разметили и собрали из них датасет, добавив еще одну группу изображений из открытых источников. Модель справлялась с детекцией, но по хорошему её нужно дообучать. Данную модель можно объединить с основной, и получить улучшенные метрики обнаружения сигареты у человека. 

<p align="center">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/RedLightMetrica1.jpg" alt="Метрика-1" style="width:30%;">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/RedLightMetrica2.jpg" alt="Метрика-2" style="width:30%;">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/RedLightMetrica3.jpg" alt="Метрика-3" style="width:30%;">
</p>

- ![RedLight NOTEBOOK](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/notebooks/RedLight.ipynb)
- ![RedLight Model](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/models/red_light_model.pt)

  В дополнении мы решили попробовать детекцию дыма. Будем определять дым от зажженой сигареты. Обучили модель по имеющемуся датасету. Получили хорошие метрики. Данную модель можно использовать вместе с основной, для более точного обнаружения курения.

<p align="center">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/SmokeDetectMetrica1.jpg" alt="Метрика-1" style="width:45%;">
  <img src="https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/metrics/SmokeDetectMetrica2.jpg" alt="Метрика-2" style="width:45%;">
</p>

- ![SmokeDetect NOTEBOOK](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/notebooks/SmokeDetect.ipynb)
- ![SmokeDetect Model](https://github.com/Sobakais/nuclearMisisCoconut/blob/main/source/models/smoke_model.pt)

  Окончательная модель обучена на размеченных фотографий заказчиком плюс подобные фотографии с камер наблюдения где есть как курящие, так и не курящие люди. Получили такие метрики:
Скрин метрик:
Kaggle:

Для удобной работы с основной моделью мы собрали Telegram бота, который принимает изображение, обрабатывает и отправляет полученное предсказание в процентах пользователю.
Ссылка на Telegram бота: 
<a href="https://t.me/misis_coconut_bot">Telegram Bot</a>

#### Планы по улучшению
- Точная настройка модели для лучшей производительности обнаружения.
- Включить обнаружение позы человека в модель.
- Интеграция с базой данных биометрии (Сбер, mos.ru), для определения личности и автоматического выписывания штрафов нарушителям
