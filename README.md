# Regressao-Linear-Brasil
Neste repositório, disponibilizo um pacote em português para desenvolvimento de modelos de regressão linear. O pacote contém as principais métricas de validação como métodos da classe `RegressaoLinearBRC`, as quais são MAE, MSE, RMSE, R² e R² Ajustado.

Além do pacote, disponibilizo o arquivo .ipynb que demonstra o sucesso da classe `RegressaoLinearBRC` e seus métodos e a base usada para a validação.

## Obtendo o pacote
Cole o seguinte código em uma célula do Jupyter Lab ou Google Colab:

`!wget https://raw.githubusercontent.com/bruno-rodrigues-carloto/Regressao-Linear-Brasil/refs/heads/main/regressao-linear-brasil/modelo_regressao_linear_brasil.py`

## Importando a classe
`**from** modelo_regressao_linear_brasil **import** RegressaoLinearBRC`

Para uso da classe, segue-se o mesmo padrão do `LinearRegression` do **scikit-learn**.

**Exemplo:**
```
# Instanciando modelo BRC
modelo_brc = RegressaoLinearBRC()

# Realizando ajuste do modelo BRC
modelo_brc.ajuste(X_treinamento, y_treinamento)

# Predição
y_pred = modelo_brc.predizer(X_teste)
```

## Sobre o pacote
O pacote é composto pela classe **RegressaoLinearBRC** - *BRC referente a Bruno Rodrigues Carloto* - que contém os seguintes métodos:

1. **ajuste( ):**

Recebe os dados de treinamento, tanto as variáveis dependentes X quanto a variável dependente y, para cálculo matricial e ajuste do modelo.
Respectivamente recebe as variáveis independentes X e a variável dependente y.

2. **predizer( ):**

Recebe somente as variáveis independentes X de teste ou os dados de predição após implementação/aplicação do modelo.

3. **equacao( ):**

O objetivo desse método é apenas evidenciar a equação da regressão.
Não se fornece qualquer parâmetro para o método.

4. **erro_absoluto_medio( ):**

Esse método calcula o erro absoluto médio.
Para usá-lo, basta passar os valores reais da variável dependente/resposta.

5. **erro_quadrado_medio( ):**

Esse método calcula o erro quadrado médio.
Para usá-lo, basta passar os valores reais da variável dependente/resposta.

6. **raiz_quadrada_erro_quadrado_medio( ):**

Esse método calcula a raiz do erro quadrado médio.
Para usá-lo, basta passar os valores reais da variável dependente/resposta.

7. **r_quadrado( ):**

Esse método é o coeficiente determinante. Ele calcula o quanto as variáveis independentes X explicam a variabilidade da variável dependente y.

Quanto mais próximo de 1, mais X explica a variabilidade de y.

Sua desvantagem é que quanto mais variável independente há, mais seu valor é maior. 
Nesses casos, o coeficiente determinante ajustado é mais indicado.

8. **r_quadrado_ajustado( ):**

Esse método é o coeficiente determinante ajustado. Ele calcula o quanto as variáveis independentes X explicam a variabilidade da variável dependente y.

Sua vantagem é não permitir que o excesso de variáveis independentes irrelevantes aumentem seu valor.
Quanto mais próximo de 1, mais X explica a variabilidade de y.
