def obter_tamanho_quadrado() -> float:
    while True:
        entrada = input("Digite o tamanho do quadrado em m²: ")
        try:
            tamanho = float(entrada)
            if tamanho > 0:
                return tamanho
            else:
                print("Erro: O tamanho deve ser positivo.")
        except ValueError:
            print("Erro: Entrada inválida, por favor digite um número.")

def obter_numero_de_quadrados() -> int:
    while True:
        entrada = input("Digite o número de quadrados: ")
        try:
            quantidade = int(entrada)
            if quantidade > 0:
                return quantidade
            else:
                print("Erro: A quantidade deve ser um número inteiro positivo.")
        except ValueError:
            print("Erro: Entrada inválida, por favor digite um número inteiro.")

def capturar_valores_quadrados(total_quadrados: int) -> list:
    valores = []
    for index in range(total_quadrados):
        while True:
            valor = input(f"Digite o valor do quadrado {index + 1} (A para água, O para óleo): ").upper()
            if valor in ['A', 'O']:
                valores.append(valor)
                break
            else:
                print("Erro: Valor inválido. Use 'A' para água ou 'O' para óleo.")
    return valores

def mostrar_quadrados(valores: list) -> None:
    print("\nValores dos quadrados:")
    for i, valor in enumerate(valores, start=1):
        print(f"Quadrado {i}: {valor}")

def analisar_manchas_oleo(valores: list, area_quadrado: float) -> None:
    manchas = [i for i, valor in enumerate(valores) if valor == 'O']
    if manchas:
        print(f"\nManchas de óleo nas posições: {manchas}")
        area_total = len(manchas) * area_quadrado
        print(f"Área total das manchas de óleo: {area_total:.2f} m²")
    else:
        print("\nNenhuma mancha de óleo encontrada.")

def principal() -> None:
    area_quadrado = obter_tamanho_quadrado()
    num_quadrados = obter_numero_de_quadrados()
    valores_quadrados = capturar_valores_quadrados(num_quadrados)
    mostrar_quadrados(valores_quadrados)
    analisar_manchas_oleo(valores_quadrados, area_quadrado)

if __name__ == "__main__":
    principal()