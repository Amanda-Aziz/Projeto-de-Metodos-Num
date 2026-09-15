def secante(
    f,
    x0,
    x1,
    tolerancia_x=1e-6,
    tolerancia_f=1e-6,
    max_iter=100
):
    """
    Método da Secante para encontrar raízes de f(x) = 0.

    Parâmetros:
        f: função cuja raiz será buscada
        x0, x1: estimativas iniciais
        tolerancia_x: critério de parada para o erro
                      entre aproximações consecutivas
        tolerancia_f: critério de parada para o resíduo
        max_iter: número máximo de iterações permitidas

    Retorna um dicionário com:
        raiz, convergiu, iteracoes, erro, residuo, historico
    """

    historico = []

    convergiu = False

    erro = float('inf')

    x_atual = x1

    for i in range(1, max_iter + 1):

        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-15:
            # não é possível continuar: denominador ~ 0
            break

        x_atual = (
            x1
            - f_x1 * (x1 - x0)
            / (f_x1 - f_x0)
        )

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

        if (
            erro < tolerancia_x
            and
            residuo_it < tolerancia_f
        ):
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