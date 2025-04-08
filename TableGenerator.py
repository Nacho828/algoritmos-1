class TableGenerator:
    """Clase que genera una tabla de resultados para diferentes valores de n."""
    def __init__(self, calculator):
        self.calculator = calculator

    def generate_table(self, max_n):
        """Genera una tabla con las posibilidades válidas para n desde 1 hasta max_n."""
        table = []
        for n in range(1, max_n + 1):
            possibilities = self.calculator.calculate_possibilities(n)
            table.append((n, possibilities))
        return table