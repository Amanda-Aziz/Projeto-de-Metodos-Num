"""
Pacote com implementações próprias de métodos numéricos
para determinação de raízes de equações não lineares.
"""

from .ponto_fixo import ponto_fixo
from .newton_raphson import newton_raphson
from .bissecao import bissecao

__all__ = ["ponto_fixo", "newton_raphson", "bissecao"]
