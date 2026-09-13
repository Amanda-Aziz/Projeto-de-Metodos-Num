# ORIENTAÇÃO DE RETORNO - MÉTODO DE NEWTON-RAPHSON
#
# A implementação do método fica a critério do responsável.
# O importante é manter o retorno compatível com o notebook.
#
# O método deve retornar um dicionário contendo:
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
# Importante: os arquivos em src/metodos_numericos/ 
# devem implementar somente os algoritmos genéricos. 
# Não colocar neles g, L, t, v_alvo, f(H), phi(H), 
# derivada_f(H), [1,2] ou H0=1.5, 
# porque essas informações pertencem à aplicação do problema e ficam no notebook.