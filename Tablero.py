class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = [-1] * n  # Representa las posiciones de las reinas en cada columna

    def es_seguro(self, fila, col):
        """
        Verifica si es seguro colocar una reina en la fila y columna dadas.
        """
        for c in range(col):
            if self.tablero[c] == fila or abs(self.tablero[c] - fila) == abs(c - col):
                return False
        return True

    def colocar_reina(self, col, fila):
        """
        Coloca una reina en la columna y fila dadas.
        """
        self.tablero[col] = fila

    def quitar_reina(self, col):
        """
        Quita la reina de la columna dada.
        """
        self.tablero[col] = -1

    def obtener_solucion(self):
        """
        Devuelve una copia del tablero actual como solución.
        """
        return self.tablero.copy()