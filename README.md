# Algoritmos Combinatorios: Teclado Numérico y Problema de las N-Reinas

Este repositorio contiene dos ejercicios principales que abordan problemas combinatorios utilizando programación orientada a objetos (POO) y algoritmos eficientes. Ambos ejercicios están diseñados para explorar diferentes enfoques de resolución y optimización.

---

## Ejercicio 1: Cálculo de Posibilidades Válidas en un Teclado Numérico 3x3

### Descripción
El objetivo de este ejercicio es calcular las posibilidades válidas de movimientos en un teclado numérico 3x3, donde cada número tiene restricciones de movimiento. Este problema simula un teclado donde solo ciertos números pueden ser alcanzados desde otros.

### Componentes
- **`MovementRules`**: Define las reglas de movimiento válidas para cada número.
- **`PossibilityCalculator`**: Calcula las posibilidades válidas basándose en las reglas de movimiento.
- **`TableGenerator`**: Genera una tabla de resultados para un rango de valores (`max_n`), mostrando las posibilidades válidas para cada cantidad de movimientos.

### Ejemplo de Código
```python
valid_moves = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
    4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
    7: [4, 8], 8: [5, 7, 9], 9: [6, 8]
}

movement_rules = MovementRules(valid_moves)
calculator = PossibilityCalculator(movement_rules)
table_generator = TableGenerator(calculator)

max_n = 32
results = table_generator.generate_table(max_n)

print("Cantidad de movimientos (n) | Posibilidades válidas (Total)")
for n, total in results:
    print(f"{n:<26} | {total}")
```

### Resultados
```markdown
Cantidad de movimientos (n) | Posibilidades válidas (Total)
1                          | 10
2                          | 36
3                          | 116
...
32                         | 844424930131968
```

---

## Ejercicio 2: Problema de las N-Reinas

### Descripción
El objetivo de este ejercicio es resolver el problema de las N-Reinas, donde se deben colocar N reinas en un tablero de NxN de manera que ninguna reina pueda atacar a otra.

### Componentes
- **`SolucionadorNReinas`**: Resuelve el problema de las N-Reinas utilizando un algoritmo de backtracking.
- **`Visualizador`**: Muestra las soluciones encontradas en un formato visual.

### Ejemplo de Código
```python
n = 8  # Tamaño del tablero
solucionador = SolucionadorNReinas(n)
soluciones = solucionador.resolver()

print(f"Se encontraron {len(soluciones)} soluciones para un tablero de {n}x{n}.")
Visualizador.mostrar_soluciones(soluciones)
```

### Resultados
```markdown
Se encontraron 92 soluciones para un tablero de 8x8.
Solución 1:
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q
. . Q . . . . .
Q . . . . . . .
. . . . Q . . .
. . . . . . Q .

Solución 2:
. . Q . . . . .
Q . . . . . . .
. . . . Q . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q
...
```

---

## Estructura del Proyecto

```markdown
/workspaces/algoritmos-1/
├── [main.py](http://_vscodecontentref_/1)                  # Archivo principal que ejecuta ambos ejercicios
├── [MovementRules.py](http://_vscodecontentref_/2)         # Reglas de movimiento para el teclado numérico
├── [PossibilityCalculator.py](http://_vscodecontentref_/3) # Calculador de posibilidades válidas
├── [TableGenerator.py](http://_vscodecontentref_/4)        # Generador de tablas de resultados
├── [SolucionadorNReinas.py](http://_vscodecontentref_/5)   # Algoritmo de backtracking para N-Reinas
├── [Visualizador.py](http://_vscodecontentref_/6)          # Visualizador de soluciones para N-Reinas
└── [README.md](http://_vscodecontentref_/7)                # Documentación del proyecto
```


Link del repositorio