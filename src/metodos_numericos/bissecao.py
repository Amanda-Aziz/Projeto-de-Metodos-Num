def bissecao(
    f,
    a,
    b,
    tolerancia_x=1e-6,
    tolerancia_f=1e-6,
    max_iter=100
):
    """
    Metodo da Bissecao para determinacao de raizes
    de equacoes nao lineares.

    Parametros:
        f:
            Funcao original f(x) = 0.

        a, b:
            Extremos do intervalo inicial (deve valer f(a) * f(b) < 0).

        tolerancia_x:
            Tolerancia para o erro associado ao intervalo.

        tolerancia_f:
            Tolerancia para o residuo |f(x)|.

        max_iter:
            Numero maximo de iteracoes.

    Retorna:
        Um dicionario contendo:
            raiz
            convergiu
            iteracoes
            erro
            residuo
            erro_intervalo
            historico
    """

    historico = []

    fa = f(a)
    fb = f(b)

    if fa == 0:
        return {
            "raiz": a, "convergiu": True, "iteracoes": 0,
            "erro": 0.0, "residuo": 0.0,
            "erro_intervalo": abs(b - a), "historico": historico,
        }
    if fb == 0:
        return {
            "raiz": b, "convergiu": True, "iteracoes": 0,
            "erro": 0.0, "residuo": 0.0,
            "erro_intervalo": abs(b - a), "historico": historico,
        }

    x_anterior = None

    for i in range(max_iter):

        x_atual = (a + b) / 2
        f_x = f(x_atual)

        erro_intervalo = (b - a) / 2
        erro = erro_intervalo if x_anterior is None else abs(x_atual - x_anterior)
        residuo = abs(f_x)

        historico.append({
            "iteracao": i + 1,
            "a": a,
            "b": b,
            "x_atual": x_atual,
            "f_x": f_x,
            "erro": erro,
            "erro_intervalo": erro_intervalo,
            "residuo": residuo,
        })

        if (
            erro_intervalo < tolerancia_x
            and
            residuo < tolerancia_f
        ):
            return {
                "raiz": x_atual,
                "convergiu": True,
                "iteracoes": i + 1,
                "erro": erro,
                "residuo": residuo,
                "erro_intervalo": erro_intervalo,
                "historico": historico,
            }

        if fa * f_x < 0:
            b = x_atual
            fb = f_x
        else:
            a = x_atual
            fa = f_x

        x_anterior = x_atual

    return {
        "raiz": x_atual,
        "convergiu": False,
        "iteracoes": max_iter,
        "erro": erro,
        "residuo": residuo,
        "erro_intervalo": erro_intervalo,
        "historico": historico,
    }