def newton_raphson(
    f,
    df,
    x0,
    tolerancia_x=1e-6,
    tolerancia_f=1e-6,
    max_iter=100
):

    """
    Método de Newton Raphson.

    Parâmetros:
    f:
        Função original f(x) = 0.
    
    df:
        Derivada de f, ou seja, f'(x).
    
    x0:
        Aproximação inicial.

    tolerancia_x:
        Tolerância para a diferença entre
        aproximações consecutivas.

    tolerancia_f:
        Tolerância para o resíduo |f(x)|.

    max_iter=100:
        Número máximo de iterações.

    Retorna:
        Um dicionário contendo:
            raiz
            convergiu
            iteracoes
            erro
            residuo
            historico
    """

    x_atual = x0
    historico = []

    for i in range(max_iter):

        f_atual = f(x_atual)
        df_atual = df(x_atual)

        if df_atual == 0:
            return{
                "raiz": x_atual,
                "convergiu": False,
                "iteracoes": i,
                "erro": None,
                "residuo": abs(f_atual),
                "historico": historico
            }
        
        x_proximo = x_atual - f_atual / df_atual
        erro = abs(x_proximo - x_atual)
        residuo = abs(f(x_proximo))

        historico.append({
            "iteracao": i + 1,
            "x_anterior": x_atual,
            "x_atual": x_proximo,
            "erro": erro,
            "residuo": residuo
        })

        if (
            erro < tolerancia_x
            and
            residuo < tolerancia_f
        ):
            return {
                "raiz": x_proximo,
                "convergiu": True,
                "iteracoes": i + 1,
                "erro": erro,
                "residuo": residuo,
                "historico": historico
            }

        x_atual = x_proximo


    return {
        "raiz": x_atual,
        "convergiu": False,
        "iteracoes": max_iter,
        "erro": erro,
        "residuo": residuo,
        "historico": historico
    }