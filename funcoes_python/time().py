# Usado para trabalhar com tempo, como medir o tempo de execução de um código.

import time

start_time = time.time()

# Código a ser medido
for _ in range(1000000):
    pass

end_time = time.time()
print(f"Tempo de execução: {end_time - start_time} segundos")