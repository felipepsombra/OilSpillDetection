# Detecção de Derramamento de Óleo

Detectar derramamentos de óleo no mar é crucial para proteger o meio ambiente e responder a desastres ecológicos, evitando danos à vida marinha e aos ecossistemas costeiros. Este projeto tem como objetivo desenvolver um algoritmo em Python para auxiliar na detecção de derramamentos de óleo na superfície do oceano, identificando áreas afetadas com base em imagens de satélite.

## Funcionalidades

- Solicitar o tamanho dos quadrados da grade em metros quadrados.
- Entrada do usuário para cada quadrado da grade, identificando água ('A') ou óleo ('O').
- Armazenar os dados de entrada do usuário em uma lista.
- Analisar os dados para detectar a presença de derramamentos de óleo.
- Imprimir os dados analisados, indicando a presença de óleo e suas posições na lista.
- Calcular a área total dos derramamentos de óleo com base nos dados de entrada do usuário.

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/yourusername/OilSpillDetection.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd OilSpillDetection
    ```
3. Execute o script Python:
    ```bash
    python3 oil_spill_detection.py
    ```

## Estrutura do Código

O projeto consiste em várias funções para obter entrada do usuário, processar os dados e gerar saídas:

- `get_square_size()`: Solicita e retorna o tamanho dos quadrados em metros quadrados.
- `get_number_of_squares()`: Solicita e retorna o número de quadrados que o usuário deseja analisar.
- `capture_square_values(total_squares)`: Captura os valores de cada quadrado (água ou óleo) e os armazena em uma lista.
- `display_squares(values)`: Imprime os valores capturados dos quadrados.
- `analyze_oil_spills(values, square_area)`: Analisa os dados para detectar derramamentos de óleo e calcula a área total dos derramamentos.

## Exemplo de Uso

```plaintext
Informe o tamanho do quadrado em m²: 10
Informe o número de quadrados: 5
Informe o valor do quadrado 1 (A para água, O para óleo): O
Informe o valor do quadrado 2 (A para água, O para óleo): A
Informe o valor do quadrado 3 (A para água, O para óleo): O
Informe o valor do quadrado 4 (A para água, O para óleo): A
Informe o valor do quadrado 5 (A para água, O para óleo): O

Valores dos quadrados:
Quadrado 1: O
Quadrado 2: A
Quadrado 3: O
Quadrado 4: A
Quadrado 5: O

Derramamentos de óleo detectados nas posições: [0, 2, 4]
Área total dos derramamentos de óleo: 30,00 m²
