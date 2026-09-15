# ORIENTAÇÃO - MÉTODO DA FALSA POSIÇÃO
#
# ASSINATURA OBRIGATÓRIA DA FUNÇÃO
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



def falsa_posicao(
    f,
    a,
    b,
    tolerancia_x=1e-6,
    tolerancia_f=1e-6,
    max_iter=100
):
    
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError(
            "f(a) e f(b) devem ter sinais opostos: "
            f"f(a)={fa}, f(b)={fb}"
        )

    historico = []
    x_anterior = a
    x_atual = None
    f_x = None
    erro = None
    convergiu = False
    iteracao = 0

    while iteracao < max_iter:
        iteracao += 1

        x_atual = a - fa * (b - a) / (fb - fa)
        f_x = f(x_atual)
        erro = abs(x_atual - x_anterior)
        residuo = abs(f_x)

        historico.append({
            "iteracao": iteracao,
            "a": a,
            "b": b,
            "x_atual": x_atual,
            "f_x": f_x,
            "erro": erro,
            "residuo": residuo,
        })

        if residuo < tolerancia_f and erro < tolerancia_x:
            convergiu = True
            break

        if fa * f_x < 0:
            b = x_atual
            fb = f_x
        else:
            a = x_atual
            fa = f_x

        x_anterior = x_atual

    return {
        "raiz": x_atual,
        "convergiu": convergiu,
        "iteracoes": iteracao,
        "erro": erro,
        "residuo": abs(f_x),
        "historico": historico,
    }