# Изменение рамера изображения 

Скрипт принимает на вход изображение и кладёт изображение с новым размером куда скажет пользователь или рядом с исходным. У него есть обязательный аргумент – путь до исходной картинки. И несколько необязательных: width - ширина результирующей картинки, height - её высота, scale - во сколько раз увеличить изображение (может быть меньше 1), output - куда класть результирующий файл. Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. И наоборот. – Если указана и ширина и высота – создается именно такое изображение.

# Пример 
```
(venv) user:~$ python3 image_resize.py --scale 2 test.jpeg 
(venv) user:~$ python3 image_resize.py test.jpeg -h 20 -w 300 
Warning: the picture may be disproportionate
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

