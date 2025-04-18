import numpy as np
from .generation import generation

class generation_A(generation):
    def __init__(self):
        self.members = []

    def add_member(self, mask: np.ndarray):
        if not isinstance(mask, np.ndarray):
            raise TypeError("O membro deve ser um np.ndarray")
        if mask.dtype != np.uint8:
            raise ValueError("A máscara deve ser do tipo np.uint8 (binária)")
        self.members.append(mask)
        return f"Membro adicionado com shape {mask.shape}"

    def del_member(self, idx: int):
        if 0 <= idx < len(self.members):
            self.members.pop(idx)
            return f"Membro de índice {idx} removido."
        else:
            return f"❌ Índice {idx} inválido."
