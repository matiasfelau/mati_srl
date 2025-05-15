import matplotlib.pyplot as plt

dias = list(range(1, 8))

velocidad_antes = [245, 238, 268, 249, 276, 237, 256]

velocidad_despues = [184, 186, 182, 183, 185, 184, 182]

plt.figure(figsize=(12, 6))
plt.plot(dias, velocidad_antes, label='Antes (Recuperación tras intervención humana)', color='red', marker='o')
plt.plot(dias, velocidad_despues, label='Después (Recuperación tras activación automática)', color='green', marker='s')
plt.title('Velocidad de Recuperación Antes y Después de Implementar Automatización')
plt.xlabel('Día')
plt.ylabel('Velocidad de Recuperación (minutos)')
plt.xticks(dias)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
