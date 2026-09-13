# ORIENTAÇÃO DE RETORNO - MÉTODO DA BISSEÇÃO
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
# "erro_intervalo":
#     Erro associado ao tamanho do intervalo utilizado
#     pelo método.
#
# "historico":
#     Lista com os dados de todas as iterações.
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
#     "erro_intervalo": ...,
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