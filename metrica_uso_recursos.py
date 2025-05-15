import matplotlib.pyplot as plt

#uso en un periodo de tiempo
dias = list(range(10, 18))

uso_recursos_antes = [34, 36, 35, 34, 31, 37, 34, 35]

uso_recursos_despues = [2, 1, 3, 2, 1, 3, 2, 1]


plt.figure(figsize=(12, 6))
plt.plot(dias, uso_recursos_antes, label='Antes (Uso haciendo backup en horas pico)', color='red', marker='o')
plt.plot(dias, uso_recursos_despues, label='Después (Uso en horas pico sin backup)', color='green', marker='s')
plt.title('Porcentaje de uso de recursos del servicio de backup')
plt.xlabel('Hora')
plt.ylabel('Porcentaje de uso de recursos (%)')
plt.xticks(dias)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#uso total en un periodo de tiempo
uso_recursos_antes_2 = [100, 100, 98, 100, 97, 97, 100, 99]

uso_recursos_despues_2 = [62, 61, 63, 62, 61, 63, 62, 61]

plt.figure(figsize=(12, 6))
plt.plot(dias, uso_recursos_antes_2, label='Antes (Uso del sistema en horas pico con backup)', color='red', marker='o')
plt.plot(dias, uso_recursos_despues_2, label='Después (Uso del sistema en horas pico sin backup)', color='green', marker='s')
plt.title('Porcentaje de uso de recursos del sistema utilizando el servicio de backup')
plt.xlabel('Hora')
plt.ylabel('Porcentaje de uso de recursos (%)')
plt.xticks(dias)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#horas de bottleneck

horas = list(range(1, 8))

horas_bottleneck_antes = [8, 7, 8, 8, 8, 7, 5]

horas_bottleneck_despues = [2, 3, 2, 2, 1, 0, 0]

plt.figure(figsize=(12, 6))
plt.plot(horas, horas_bottleneck_antes, label='Antes (Haciendo backup en horarios de alta demanda)', color='red', marker='o')
plt.plot(horas, horas_bottleneck_despues, label='Después (Haciendo backup en horarios de baja demanda)', color='green', marker='s')
plt.title('Horas de bottleneck de los recursos del sistema')
plt.xlabel('Día')
plt.ylabel('Horas de bottleneck')
plt.xticks(horas)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()