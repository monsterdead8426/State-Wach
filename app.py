import time
import random

# Simulamos los nodos con estados cambiantes
nodos = {
    "nodo_1": "activo",
    "nodo_2": "inactivo",
    "nodo_3": "activo",
}

def mostrar_estado():
    for nodo, estado in nodos.items():
        print(f"{nodo}: {estado}")

def cambiar_estado():
    nodo = random.choice(list(nodos.keys()))
    estado = random.choice(["activo", "inactivo"])
    nodos[nodo] = estado
    print(f"El estado de {nodo} ha cambiado a {estado}")

if __name__ == "__main__":
    while True:
        mostrar_estado()
        cambiar_estado()
        time.sleep(3)  # Actualiza el estado cada 3 segundos
