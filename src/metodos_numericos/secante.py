def secante(f, x0, x1, tolerancia=1e-6, max_iteracoes=100):
    """
    Método da secante para encontrar raízes de f(x) = 0.

    Parâmetros:
        f: função cuja raiz será buscada
        x0, x1: estimativas iniciais
        tolerancia: critério de parada para o erro entre aproximações
        max_iteracoes: número máximo de iterações permitidas

    Retorna um dicionário com:
        raiz, convergiu, iteracoes, erro, residuo, historico
    """
    historico = []
    convergiu = False
    erro = float('inf')
    x_atual = x1

    for i in range(1, max_iteracoes + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-15:
            # não é possível continuar: denominador ~ 0
            break

        x_atual = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        erro = abs(x_atual - x1)
        residuo_it = abs(f(x_atual))

        historico.append({
            "iteracao": i,
            "x_anterior": x1,
            "x_atual": x_atual,
            "erro": erro,
            "residuo": residuo_it
        })

        x0, x1 = x1, x_atual

        if erro < tolerancia:
            convergiu = True
            break

    resultado = {
        "raiz": x_atual,
        "convergiu": convergiu,
        "iteracoes": len(historico),
        "erro": erro,
        "residuo": abs(f(x_atual)),
        "historico": historico
    }

    return resultado
# ORIENTAÇÃO - MÉTODO DA SECANTE
#
# A implementação do método fica a critério do responsável.
# O importante é manter a função compatível com o notebook.
#
#
# ASSINATURA OBRIGATÓRIA DA FUNÇÃO
#
# A função deve possuir a seguinte assinatura:
#
# def secante(
#     f,
#     x0,
#     x1,
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
# representar a nova aproximação obtida naquela iteração.
#
# A chave "x_anterior" deve representar a aproximação
# imediatamente anterior a "x_atual", de forma que o
# histórico seja compatível com o cálculo e a apresentação
# do erro entre aproximações consecutivas.
#
#
# IMPORTAÇÃO NO PACOTE
#
# Após implementar a função secante(), também é
# necessário importá-la no arquivo:
#
# src/metodos_numericos/__init__.py
#
# Adicionar ao __init__.py:
#
# from .secante import secante
#
# Isso é necessário para permitir que o notebook faça:
#
# from metodos_numericos import secante
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
# intervalo [1, 2] ou valores iniciais específicos
# utilizados na aplicação.
#
# A função secante() deve apenas receber f, x0 e x1
# pelos parâmetros definidos em sua assinatura.
#
# A função f(H) e os valores de x0 e x1 utilizados na
# aplicação são definidos no notebook e fornecidos no
# momento da chamada do método.
#
# Essas informações pertencem à aplicação do problema
# e devem permanecer no notebook.