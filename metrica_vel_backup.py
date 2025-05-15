import matplotlib.pyplot as plt

dias = list(range(1, 8))

velocidad_antes = [45, 47, 46, 44, 43, 46, 45]

velocidad_despues = [110, 120, 122, 121, 118, 119, 120]

plt.figure(figsize=(12, 6))
plt.plot(dias, velocidad_antes, label='Antes (Backup completo diario)', color='red', marker='o')
plt.plot(dias, velocidad_despues, label='Después (Backup incremental)', color='green', marker='s')
plt.title('Velocidad de Backup Antes y Después de Implementar Backups Incrementales')
plt.xlabel('Día')
plt.ylabel('Velocidad de Backup (MB/s)')
plt.xticks(dias)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
