import threading
import time
import queue
import random

trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

for documento in range(1, 26):
    trabajos.put((documento, random.randint(1, 5)))

def trabajador(nombre):
    while True:
        try:
            documento, numero = trabajos.get_nowait()
        except queue.Empty:
            break
        with lock:
            resultados[documento] = nombre
        time.sleep(0.1)
        print(f"{nombre} ha terminado el documento {documento}")

hilo_a = threading.Thread(target=trabajador, args=("Thiago",))
hilo_b = threading.Thread(target=trabajador, args=("Pepe",))
hilo_c = threading.Thread(target=trabajador, args=("Carlos",))
hilo_d = threading.Thread(target=trabajador, args=("Daniel",))
hilo_a.start()
hilo_b.start()
hilo_c.start()
hilo_d.start()
hilo_a.join()
hilo_b.join()
hilo_c.join()
hilo_d.join()

print("\nRegistro final:")
for usuario in ("Thiago", "Pepe", "Carlos", "Daniel"):
    cantidad = list(resultados.values()).count(usuario)
    print(f"{usuario}: {cantidad} documentos")
