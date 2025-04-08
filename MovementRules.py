class MovementRules:
    """Clase que define las reglas de movimiento para un teclado numérico."""
    def __init__(self, valid_moves):
        self.valid_moves = valid_moves

    def get_valid_moves(self, position):
        """Devuelve los movimientos válidos desde una posición dada."""
        return self.valid_moves.get(position, [])