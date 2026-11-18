# Notável: previsão de nota com Machine Learning

Projeto de Machine Learning feito na disciplina **RMC** do 1º semestre de Engenharia de Software (PUCPR), como TDE 3. O programa usa **regressão linear** para prever a nota de um aluno a partir da média, horas extras, frequência, tarefas e atividades extras, e diz se ele deve ser aprovado.

## Estrutura

| Arquivo | O que é |
|---|---|
| `TDE3.py` | Programa principal: treina o modelo, pede os dados de um aluno e mostra a nota prevista e se ele foi aprovado |
| `prototipos/teste.py` | Protótipo do TDE 3 que também mostra o R² do modelo |
| `prototipos/teste_tde.py` | Outra versão de teste do TDE 3, feita na pasta dos TDEs |
| `prototipos/teste2.py` | Rascunho da regra de aprovação, separando reprovação por nota e por frequência |
| `aula/aulasklr.ipynb` | Notebook da aula de scikit-learn: regressão linear que estima o preço de um imóvel |

## Como o `TDE3.py` funciona

O programa usa Machine Learning (regressão linear) para prever a nota de um aluno a partir dos seus atributos acadêmicos e, com isso, indicar se ele foi aprovado ou não.

### Bibliotecas usadas

- `scikit-learn`: modelo de regressão linear
- `numpy`: manipulação de arrays

Se o scikit-learn não carregar (por exemplo, bloqueado pelo Windows), o código usa uma regressão linear própria feita com `numpy` (mínimos quadrados), que dá o mesmo resultado.

### Parte 1: criar e treinar o modelo

```python
modelo = LinearRegression()

X = np.array([[7.0, 2, 0.9, 8, 2], ...])
y = np.array([6.5, 8.2, 3.6, 1.3, 9.7, 6.0, 2.8, 4.0, 8.5, 10.0])

modelo.fit(X, y)
```

`modelo` é um objeto vazio que vai aprender com os dados. `X` tem os atributos de 10 alunos e `y` tem as notas de cada um. O `modelo.fit(X, y)` treina o modelo, ou seja, ele aprende a relação entre os atributos e as notas para conseguir fazer previsões.

**Atributos de X (nessa ordem):**

| Coluna | Atributo | Tipo | Intervalo |
|---|---|---|---|
| 1 | Média do aluno | float | 0.0 – 10.0 |
| 2 | Horas extras | int | 0 – 6 |
| 3 | Frequência | float | 0.0 – 1.0 |
| 4 | Tarefas feitas | int | 0 – 15 |
| 5 | Atividades extras | int | 0 – 6 |

### Parte 2: validação dos valores digitados

```python
def recebe_valor(mensagem: str, tipo: type, minimo: float, maximo: float) -> float | int:
    valido = False
    while not valido:
        try:
            valor = tipo(input(mensagem))
            if valor < minimo or valor > maximo:
                print(f'Valor tem que ser entre {minimo} e {maximo}')
            else:
                valido = True
        except ValueError as error:
            print(f'Certifique-se de digitar o tipo correto: {tipo}')
    return valor
```

Função reutilizada para pedir e validar cada atributo. Ela recebe a mensagem, o tipo esperado (`float` ou `int`) e os limites mínimo e máximo. Enquanto o valor for inválido (tipo errado ou fora do intervalo), ela continua pedindo. Quando o valor é válido, ela o retorna.

### Parte 3: coletar os dados e prever a nota

```python
dados_aluno_novo = np.array([[media, horas_extras, freq, tarefas_feitas, atividades_extras]])
nota_prevista = modelo.predict(dados_aluno_novo)
```

O programa pede os atributos do aluno novo no terminal. Os dados ficam em um array de duas dimensões (uma tabela de uma linha), porque o modelo exige o mesmo formato usado no treino. Depois, `modelo.predict()` aplica o que foi aprendido e calcula a nota prevista.

### Parte 4: mostrar o resultado e decidir a aprovação

```python
if freq >= 0.5 and nota_prevista[0] >= 7.0:
    print('O aluno foi aprovado')
else:
    print(f'O aluno provavelmente reprovará com a nota {nota_prevista[0]:.2f} e frequencia {freq * 100:.0f}%')
```

O aluno só é aprovado se as **duas** condições forem verdadeiras ao mesmo tempo (`and`): frequência de pelo menos 50% **e** nota prevista de pelo menos 7.0. Se uma delas falhar, o programa mostra a mensagem de reprovação com a nota e a frequência.

### Como executar

```bash
pip install scikit-learn numpy
python TDE3.py
```

Digite os atributos do aluno quando o programa pedir e veja a previsão.

---

## Protótipos (`prototipos/`)

Versões feitas durante o desenvolvimento, antes do `TDE3.py` final:

- **`teste.py`**: o mesmo programa do TDE 3, com o cálculo do **R²** (`modelo.score(X, y)`), que mostra o quanto o modelo se ajusta aos dados de treino. Quanto mais perto de 1, melhor.
- **`teste_tde.py`**: versão de teste muito parecida, feita junto com os arquivos do TDE.
- **`teste2.py`**: trecho com a regra de aprovação separada em duas variáveis (`aprovado_por_frequencia` e `aprovado_por_nota`), para mostrar o motivo da reprovação. É só um rascunho: ele usa `freq` e `nota_prevista` sem defini-las, então não roda sozinho.

## Notebook da aula (`aula/aulasklr.ipynb`)

Exercício da aula de scikit-learn que serviu de base para o TDE. O modelo é treinado com 6 imóveis, cada um descrito por 10 características numéricas, e os preços deles. Depois, `modelo.predict()` estima o preço de um imóvel novo. A ideia é a mesma do TDE 3, só que com outro tipo de dado.

```bash
pip install notebook scikit-learn numpy
jupyter notebook aula/aulasklr.ipynb
```

---

Os TDEs de RMC também estão no repositório [TDEs_RMC](https://github.com/franpietrobelli-creator/TDEs_RMC).
