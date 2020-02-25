# beep_himno_andalucia

Aplicación python3 desarrollada para conmemorar el Día de Andalucía (28 de febrero), que usando la utilidad de línea de comandos `beep` toca el himno de Andalucia por el altavoz del ordenador.

## Pasos previos

Debes instalar la utilidad `beep`, como superusuario:

    apt install beep

## Ejecución de la partitura

Para tocar el himno de Andalucía, ejecutamos como superusuario:

    # python3 andalucia.py

Disfruta de nuestro himno!!!

## Tocando otras melodías

Modificando el programa puedes guardar en la variable `musica` cualquier melodía. La variable `musica` es una cadena de caracteres donde se indica cada nota separada por un espacio. Cada nota se indica con una cadena donde se pone el tipo de nota (indicada con un número) y la nota que tenemos que tocar.

Los tipos de notas son:

* 0: semicorchea
* 1: corchea
* 2: negra con puntilla
* 3: negra
* 4: blanca
* 5: blanca con puntillo
* 6: redonda

Si ponemos una nota `--` estamos indicando un silencio.