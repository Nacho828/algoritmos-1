from Tablero import Tablero
  

class SolucionadorNReinas:
    def __init__(self, n):
        self.n = n
        self.tablero = Tablero(n)
        self.soluciones = []

    def resolver(self):
        """
        Inicia el proceso de resolución del problema de las n-reinas.
        """
        self._backtrack(0)
        return self.soluciones

    def _backtrack(self, col):
        """
        Algoritmo de backtracking para encontrar todas las soluciones.
        """
        if col == self.n:
            # Se encontró una solución válida
            self.soluciones.append(self.tablero.obtener_solucion())
            return

        for fila in range(self.n):
            if self.tablero.es_seguro(fila, col):
                self.tablero.colocar_reina(col, fila)
                self._backtrack(col + 1)
                self.tablero.quitar_reina(col)
