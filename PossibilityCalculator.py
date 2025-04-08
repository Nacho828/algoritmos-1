class PossibilityCalculator:
    """Clase que calcula las posibilidades válidas basadas en reglas de movimiento."""
    def __init__(self, movement_rules):
        self.movement_rules = movement_rules

    def calculate_possibilities(self, n):
        """Calcula el número total de posibilidades válidas para n movimientos."""
        if n == 1:
            return 9  # Cada tecla tiene 1 posibilidad inicial

        # Inicializamos la tabla dp[t][k] para almacenar resultados intermedios
        dp = [[0] * (n + 1) for _ in range(10)]

        # Para n = 1, cada tecla tiene 1 posibilidad
        for t in range(1, 10):
            dp[t][1] = 1

        # Llenamos la tabla para n > 1
        for k in range(2, n + 1):
            for t in range(1, 10):
                dp[t][k] = sum(dp[neighbor][k - 1] for neighbor in self.movement_rules.get_valid_moves(t))

        # Sumamos las posibilidades para todas las teclas iniciales
        total_possibilities = sum(dp[t][n] for t in range(1, 10))
        return total_possibilities