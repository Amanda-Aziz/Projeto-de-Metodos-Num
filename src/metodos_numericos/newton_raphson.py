# ORIENTAÇÃO - MÉTODO DE NEWTON-RAPHSON
#
# A implementação do método fica a critério do responsável.
# O importante é manter a função compatível com o notebook.
#
#
# ASSINATURA OBRIGATÓRIA DA FUNÇÃO
#
# A função deve possuir a seguinte assinatura:
#
# def newton_raphson(
#     f,
#     df,
#     x0,
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
#     "x_anterior": ...,
#     "x_atual": ...,
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
# Após implementar a função newton_raphson(), também é
# necessário importá-la no arquivo:
#
# src/metodos_numericos/__init__.py
#
# Adicionar ao __init__.py:
#
# from .newton_raphson import newton_raphson
#
# Isso é necessário para permitir que o notebook faça:
#
# from metodos_numericos import newton_raphson
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
# A função newton_raphson() deve apenas receber f, df e x0
# pelos parâmetros definidos em sua assinatura.
#
# A função f(H), a derivada_f(H) e o valor de H0 utilizados
# na aplicação são definidos no notebook e fornecidos no
# momento da chamada do método.
#
# Essas informações pertencem à aplicação do problema
# e devem permanecer no notebook.