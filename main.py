from MovementRules import MovementRules
from PossibilityCalculator import PossibilityCalculator
from TableGenerator import TableGenerator

def lanzador():
    # Definimos las reglas de movimiento para un teclado numérico 3x3
    valid_moves = {
        1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
        4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
        7: [4, 8], 8: [5, 7, 9], 9: [6, 8]
    }

    # Creamos las instancias de las clases
    movement_rules = MovementRules(valid_moves)
    calculator = PossibilityCalculator(movement_rules)
    table_generator = TableGenerator(calculator)

    # Generamos y mostramos la tabla de resultados
    max_n = 32  # Cambia este valor para calcular hasta n deseado
    results = table_generator.generate_table(max_n)

    print("Cantidad de movimientos (n) | Posibilidades válidas (Total)")
    for n, total in results:
        print(f"{n:<26} | {total}")

if __name__ == "__main__":
    lanzador()