# ORIENTAÇÃO - MÉTODO DA FALSA POSIÇÃO
#
# A implementação do método fica a critério do responsável.
# O importante é manter a função compatível com o notebook.
#
#
# ASSINATURA OBRIGATÓRIA DA FUNÇÃO
#
# A função deve possuir a seguinte assinatura:
#
# def falsa_posicao(
#     f,
#     a,
#     b,
#     tolerancia_x=1e-6,
#     tolerancia_f=1e-6,
#     max_iter=100
# ):
#
# Os nomes dos parâmetros devem ser mantidos, pois o notebook
# realiza a chamada utilizando argumentos nomeados.
#
#
# RETORNO OBRIGATÓRIO
#
# O método deve retornar um dicionário contendo:
#
# {
#     "raiz": ...,
#     "convergiu": ...,
#     "iteracoes": ...,
#     "erro": ...,
#     "residuo": ...,
#     "historico": ...
# }
#
# "raiz":
#     Aproximação final obtida para a raiz.
#
# "convergiu":
#     True se o método atender aos critérios de convergência.
#     False caso contrário.
#
# "iteracoes":
#     Quantidade de iterações realizadas.
#
# "erro":
#     Erro entre aproximações consecutivas.
#
# "residuo":
#     Valor absoluto de f(x) na aproximação final.
#
# "historico":
#     Lista com os dados de todas as iterações.
#
#
# ESTRUTURA OBRIGATÓRIA DO HISTÓRICO
#
# Cada elemento do histórico deve conter, no mínimo:
#
# {
#     "iteracao": ...,
#     "a": ...,
#     "b": ...,
#     "x_atual": ...,
#     "f_x": ...,
#     "erro": ...,
#     "residuo": ...
# }
#
# Para compatibilidade com o notebook, "x_atual" deve
# representar a aproximação obtida naquela iteração.
#
#
# IMPORTAÇÃO NO PACOTE
#
# Após implementar a função falsa_posicao(), também é
# necessário importá-la no arquivo:
#
# src/metodos_numericos/__init__.py
#
# Adicionar ao __init__.py:
#
# from .falsa_posicao import falsa_posicao
#
# Isso é necessário para permitir que o notebook faça:
#
# from metodos_numericos import falsa_posicao
#
#
# SEPARAÇÃO ENTRE PACOTE E APLICAÇÃO
#
# Os arquivos em src/metodos_numericos/ devem implementar
# somente os algoritmos genéricos.
#
# Não colocar neste arquivo informações específicas da
# aplicação, como:
#
# g, L, t, v_alvo, f(H), phi(H), derivada_f(H),
# intervalo [1, 2] ou aproximação inicial H0 = 1.5.
#
# Essas informações pertencem à aplicação do problema
# e devem permanecer no notebook.