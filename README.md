# OilSpillDetection

A detecção de manchas de óleo no mar é crucial para proteger o ambiente e responder a desastres ecológicos, prevenindo danos à vida marinha e aos ecossistemas costeiros. Este projeto tem como objetivo desenvolver um algoritmo em Python para auxiliar na detecção de manchas de óleo na superfície dos oceanos, identificando áreas afetadas com base em imagens de satélite.

## Funcionalidades

- Solicitação do tamanho dos quadrados da grade em metros quadrados.
- Entrada de dados pelo usuário para cada quadrado da grade, identificando água ('A') ou óleo ('O').
- Armazenamento dos dados inseridos pelo usuário em uma lista.
- Análise dos dados para detectar a presença de manchas de óleo.
- Impressão dos dados analisados, indicando a presença de óleo e suas posições na lista.
- Cálculo da área total das manchas de óleo com base nos dados inseridos.

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/OilSpillDetection.git
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

O projeto consiste em várias funções para obter entradas do usuário, processar dados e gerar saídas:

- `obter_tamanho_quadrado()`: Solicita e retorna o tamanho dos quadrados em metros quadrados.
- `obter_numero_de_quadrados()`: Solicita e retorna o número de quadrados que o usuário deseja analisar.
- `capturar_valores_quadrados(total_quadrados)`: Captura os valores de cada quadrado (água ou óleo) e os armazena em uma lista.
- `mostrar_quadrados(valores)`: Imprime os valores capturados dos quadrados.
- `analisar_manchas_oleo(valores, area_quadrado)`: Analisa os dados para detectar manchas de óleo e calcula a área total das manchas.

## Exemplo de Uso

```plaintext
Digite o tamanho do quadrado em m²: 10
Digite o número de quadrados: 5
Digite o valor do quadrado 1 (A para água, O para óleo): O
Digite o valor do quadrado 2 (A para água, O para óleo): A
Digite o valor do quadrado 3 (A para água, O para óleo): O
Digite o valor do quadrado 4 (A para água, O para óleo): A
Digite o valor do quadrado 5 (A para água, O para óleo): O

Valores dos quadrados:
Quadrado 1: O
Quadrado 2: A
Quadrado 3: O
Quadrado 4: A
Quadrado 5: O

Manchas de óleo nas posições: [0, 2, 4]
Área total das manchas de óleo: 30.00 m²
