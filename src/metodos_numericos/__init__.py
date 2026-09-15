"""
Pacote com implementações próprias de métodos numéricos
para determinação de raízes de equações não lineares.
"""

from .ponto_fixo import ponto_fixo
from .newton_raphson import newton_raphson
from .bissecao import bissecao
from .falsa_posicao import falsa_posicao
from .secante import secante

__all__ = ["ponto_fixo", "newton_raphson", "bissecao", "falsa_posicao", "secante"]
