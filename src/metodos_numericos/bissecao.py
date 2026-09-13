# ORIENTAÇÃO - MÉTODO DA BISSEÇÃO
#
# A implementação interna do método fica a critério do responsável.
# Entretanto, para garantir a compatibilidade com o notebook,
# devem ser respeitados:
#
# 1. A assinatura da função;
# 2. A estrutura do retorno;
# 3. A estrutura do histórico;
# 4. A importação da função no arquivo __init__.py.
#
#
# ASSINATURA OBRIGATÓRIA DA FUNÇÃO
#
# A função deve possuir a seguinte assinatura:
#
# def bissecao(
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
# A função deve retornar um dicionário contendo:
#
# {
#     "raiz": ...,
#     "convergiu": ...,
#     "iteracoes": ...,
#     "erro": ...,
#     "residuo": ...,
#     "erro_intervalo": ...,
#     "historico": ...
# }
#
# "raiz":
#     Aproximação final obtida para a raiz.
#
# "convergiu":
#     True se o método atender aos critérios de convergência;
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
#     Erro associado ao intervalo utilizado pela Bisseção.
#
# "historico":
#     Lista contendo os dados das iterações.
#
#
# ESTRUTURA OBRIGATÓRIA DO HISTÓRICO
#
# Cada elemento de "historico" deve conter, no mínimo:
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
# Para compatibilidade com os gráficos do notebook,
# a chave "x_atual" deve representar a aproximação
# obtida naquela iteração.
#
#
# IMPORTAÇÃO NO PACOTE
#
# Após implementar bissecao(), adicionar ao arquivo
# src/metodos_numericos/__init__.py:
#
# from .bissecao import bissecao
#
# Isso permite que o notebook utilize:
#
# from metodos_numericos import bissecao
#
#
# SEPARAÇÃO ENTRE PACOTE E APLICAÇÃO
#
# Este arquivo deve conter somente o algoritmo genérico.
#
# Não incluir informações específicas do problema, como:
# g, L, t, v_alvo, f(H), phi(H), derivada_f(H),
# intervalo [1, 2] ou H0 = 1.5.
#
# Essas informações pertencem à aplicação e permanecem
# no notebook.