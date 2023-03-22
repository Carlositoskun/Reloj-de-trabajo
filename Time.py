import time

Tiempo_actual = time.localtime().tm_hour

if Tiempo_actual>= 16:
    print("Ya es hora de ir a casa perro!!!", Tiempo_actual)
else:
        Hora_salida=16
        Minutos_faltantes = 60- time.localtime().tm_min
        Segundos_faltantes= 60- time.localtime().tm_sec
        Tiempo_faltante =(Hora_salida - Tiempo_actual)
        print(f"Te quedan por trabajar {Tiempo_faltante} horas con {Minutos_faltantes} minutos y {Segundos_faltantes} segundos perro")
        print("ponle ganas")
     


