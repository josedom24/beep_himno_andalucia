#!/usr/bin/python3
import os, sys

# Frecuencias de las distintas notas para beep
notas={"Do":261.6,"Do#":277.2,"Re":293.7,"Re#":311.1,"Mi":329.6,"Fa":349.2,"Fa#":370.0,"Sol":392.0,"Sol#":415.3,"La":440.0,"La#":466.2,"Si":493.9,"Do":523.2,"--":0}

# Los tipos de notas están especificadas por un número

#0: semicorchea
#1: corchea
#2: negra con puntilla
#3: negra
#4: blanca
#5: blanca con puntillo
#6: redonda

# Guardo los tiempos de cada tipo de nota, la duración está calculada a partir de la duración de la semicorchea

# Cambiando la duración de la semicorchea cambiamos el "tempo" de la melodía.

semicorchea=87
tiempo={"0":semicorchea,"1":2*semicorchea,"2":6*semicorchea,"3":4*semicorchea,"4":8*semicorchea,"5":12*semicorchea,"6":16*semicorchea,"7":32*semicorchea}

# Guardamos la partitura en la cadena "musica", las notas están separada por un espacio. La nota "--" es un silencio. Se indica el tipo de nota (un número) y la nota

musica="3Do 3Re 5Mi 3Fa 3La 4Sol 3Fa# 4Sol 4Re 6-- 3La 3La 6La 1Si 1La 4Sol 3Fa 1Sol 1Fa 5Mi 6-- 3Do 3Re 5Mi 3Fa 3La 4Sol 3Fa# 4Sol 4Re 6-- 3La 3La 6La 1Si 1La 4Sol 3Fa 1Sol 1Fa 5Mi 7-- 6Do 6Sol 3Fa 3Sol 4Fa 6Mi 6Do 7Sol 3Fa 4La 1Sol 1Fa 4Mi"

# Programa principal

musica=musica.split(" ")
for nota in musica: 
    duracion=tiempo[nota[0]]
    dur=int(duracion)/1000
    if nota[1:]=="--":
        os.system("sleep %f" % dur)
    else:
        if len(sys.argv) == 2 and sys.argv[1] == "sox":
            os.system("play -n -c1 synth %f sine %d"%(dur,notas[nota[1:]]))
        else:
            os.system("beep -l %d -f %d"%(duracion,notas[nota[1:]]))
