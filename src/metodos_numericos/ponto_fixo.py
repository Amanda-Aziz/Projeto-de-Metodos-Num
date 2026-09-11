def ponto_fixo(
    phi,
    f,
    x0,
    tolerancia_x=1e-6,
    tolerancia_f=1e-6,
    max_iter=100
):
    """
    Método do Ponto Fixo para determinação de raízes
    de equações não lineares.

    Parâmetros:
        phi:
            Função de iteração x = phi(x).

        f:
            Função original f(x) = 0.

        x0:
            Aproximação inicial.

        tolerancia_x:
            Tolerância para a diferença entre
            aproximações consecutivas.

        tolerancia_f:
            Tolerância para o resíduo |f(x)|.

        max_iter:
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

        x_proximo = phi(x_atual)

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