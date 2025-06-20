# Análise de nível profissional das pessoas que trabalham com dados


**Ian Vinicius Marinho Malta, ian.malta@sga.pucminas.br**

**João Gabriel de Melo Neves, jgmneves@sga.pucminas.br**

**Thiago Couto Ferreira, thiago.couto@sga.pucminas.br**

**Thales Ribeiro Melo, thales.melo@sga.pucminas.br**


---

**Prof. Hugo Bastos de Paula**

**Prof. Hayala Nepomuceno Curto**

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**: Este projeto tem como objetivo identificar quais atributos mais qualificam um indivíduo que trabalha com dados, por meio de uma análise aprofundada do nível profissional, buscando determinar se ele é qualificado ou não na área. O projeto surgiu devido ao fato de a área de dados ser nova no mercado e estar em constante movimentação, sempre necessitando de novos profissionais. Assim, com este estudo, empresas do setor poderão contar com um ponto de apoio para a escolha de seus colaboradores. Foram escolhidos dois modelos (Decision Tree e Random Forest). Esses modelos buscam identificar o nível do profissional na empresa a partir de certos atributos. Embora apresentem algumas falhas — a principal delas sendo a dificuldade em identificar a classe pleno —, com determinados ajustes, os modelos tendem a se tornar equilibrados._

---

## Índice

- [Introdução](#introdução)

- [Contextualização](#contextualização)

- [Problema](#problema)

- [Objetivo geral](#Objetivo-geral)

- [Justificativas](#Justificativas)

- [Público alvo](#Público-alvo)

- [Análise exploratórida dos dados](#Análise-exploratórida-dos-dados)

- [Descrição de dados](#Descrição-de-dados)

- [Modelo 1: Árvore de Decisão](#Modelo-1-Árvore-de-Decisão)

- [Modelo 2: Random Forest](#Modelo-2-Random-Forest)

- [Modelo Extra associação](#Modelo-Extra-associação)

- [Análise comparativa dos modelos](#Análise-comparativa-dos-modelos)

- [Conclusão](#8-Conclusão)



## Introdução


Com a crescente importância da área de dados na tomada de decisões estratégicas, torna-se fundamental que os profissionais que atuam nesse setor sejam altamente qualificados. Nesse cenário, é essencial que os líderes das organizações — como CEOs e diretores — tenham visibilidade sobre a senioridade da equipe de dados, a fim de identificar lacunas e planejar contratações com mais assertividade. Pensando nisso, nossa empresa propõe uma solução que permite identificar, de forma precisa, o nível de experiência dos profissionais (como Júnior, Pleno ou Sênior), oferecendo um suporte confiável para decisões relacionadas à gestão de talentos e estruturação de times.

###    Contextualização


-Nos últimos anos, a Ciência de Dados consolidou-se como uma das áreas mais promissoras dentro do setor de tecnologia, impulsionada pelo aumento exponencial no volume de dados e pela necessidade de transformá-los em insights estratégicos. Empresas de diferentes segmentos passaram a investir fortemente em profissionais de dados — como cientistas, engenheiros e analistas — para aprimorar seus processos, otimizar resultados e sustentar decisões mais embasadas. 

-Apesar da alta demanda, muitas organizações enfrentam um desafio recorrente: o desequilíbrio na composição de suas equipes, seja pela concentração de profissionais próximos à aposentadoria, sem sucessores preparados, ou pela predominância de perfis júnior, ainda em fase de desenvolvimento técnico.

-Diante desse contexto, nossa empresa desenvolveu um sistema inteligente que analisa e apresenta, de forma quantitativa, a distribuição de profissionais por nível de senioridade (Júnior, Pleno e Sênior). O objetivo é oferecer uma ferramenta estratégica para que as empresas possam manter uma equipe equilibrada em termos de experiência, prevenindo riscos futuros, como a escassez de mão de obra qualificada ou a perda de conhecimento institucional.

###    Problema


Desenvolver um sistema inteligente capaz de identificar o nível de senioridade predominante entre os profissionais de dados dentro das empresas. O objetivo é fornecer uma ferramenta analítica que permita às organizações avaliar com precisão o grau de capacitação de suas equipes, auxiliando em decisões mais fundamentadas relacionadas à contratação, promoção, definição salarial e planejamento de sucessão.

Por meio da análise de dados como tempo de experiência, cargos anteriores e histórico profissional, o sistema será capaz de demonstrar o nível de preparo dos colaboradores que atuam com dados na empresa. Essa análise não apenas contribui para decisões mais lógicas e assertivas, mas também oferece uma visão estratégica sobre a maturidade e equilíbrio da equipe como um todo — elementos fundamentais para a sustentabilidade da área de dados a longo prazo.

###    Objetivo

Desenvolver um sistema capaz de identificar o nível de qualificação de profissionais da área de dados por meio da análise de atributos específicos, utilizando modelos de aprendizado de máquina, com o intuito de auxiliar empresas na composição de equipes mais equilibradas e estrategicamente estruturadas.

###    Justificativas  

-O avanço da tecnologia e da inteligência artificial tem impulsionado a demanda por profissionais qualificados na área de Ciência de Dados. No entanto, a distribuição desses profissionais pelo território brasileiro ainda não é homogênea, dificultando tanto a alocação estratégica de novas empresas quanto a oferta educacional adequada para formar especialistas nessa área. Nesse contexto, torna-se essencial o desenvolvimento de um sistema inteligente que mapeie geograficamente a densidade de Cientistas de Dados por município, permitindo uma análise aprofundada sobre regiões saturadas ou deficitárias desses profissionais.  

-Empresas que buscam expandir seus negócios para novas localidades enfrentam dificuldades para encontrar mão de obra qualificada, especialmente em municípios onde a oferta de Cientistas de Dados é escassa. O sistema proposto facilitará esse processo ao fornecer informações detalhadas sobre a concentração desses profissionais e os municípios com maior ou menor disponibilidade de talentos, possibilitando uma tomada de decisão mais assertiva na escolha de onde estabelecer suas operações.  

-Além do impacto direto na alocação empresarial, o sistema também contribuirá para o setor educacional. A identificação da demanda por cursos de Ciência de Dados permitirá que universidades e instituições de ensino superior ajustem sua oferta acadêmica, promovendo a expansão do curso para regiões com carência de formação na área. Esse fator é crucial para equilibrar a oferta e a demanda de profissionais no mercado, evitando tanto a saturação quanto a escassez de Cientistas de Dados em determinadas localidades.  

-Por fim, ao integrar variáveis que qualificam um Cientista de Dados especializado, o sistema também possibilitará uma análise mais refinada das competências exigidas no mercado, auxiliando empresas na busca por profissionais com habilidades específicas. Dessa forma, o projeto se justifica não apenas pela inovação tecnológica envolvida, mas também pelo seu potencial impacto no desenvolvimento econômico e educacional do Brasil, promovendo um equilíbrio mais eficiente entre formação acadêmica, demanda do mercado e crescimento empresarial.

##    Público alvo

Gestores e tomadores de decisão de empresas que atuam na área de tecnologia e dados, como:

 - Diretores e gerentes de Recursos Humanos

 - Gestores de equipes de tecnologia e ciência de dados

 - Líderes de inovação ou transformação digital

 - Executivos de empresas que utilizam dados como ativos estratégicos

Esse público tem interesse direto em estratégias de gestão de talentos, estruturação de equipes e planejamento de sucessão, especialmente em contextos onde a maturidade técnica e o equilíbrio entre níveis de senioridade são fundamentais para a sustentabilidade da operação.

## Análise exploratórida dos dados

###    [Dicionário de dados](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo7-densidade-demografica/blob/5ba290a5ebeca9e754fb0cf9e0033de5c9994786/assets/Data%20Dictionary/Readme.md)


###    Descrição de dados

Main Data Base
**Dados Quantitativos:**

 • Idade
 
 • Número de Funcionários
 
 • Qual o número aproximado de pessoas que atuam com dados na sua empresa hoje?
 
 • Quantidade de Cursos no estado onde mora
 
**Dados Qualitativos:**

 • Id
 
 • Faixa idade
 
 • Gênero
 
 • Cor/raça/etnia
 
 • PCD
 
 • Vive no Brasil
 
 • Estado onde mora
 
 • UF onde mora
 
 • Região onde Mora
 
 • Nível de Ensino
 
 • Área de Formação
 
 • Qual sua situação atual de trabalho?
 
 • Setor
 
 • Cargo Atual
 
 • Nível
 
 • Faixa salarial
 
 • Quanto tempo de experiência na área de dados você tem?
 
 • Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados?
 
 • Cientista de Dados/Data Scientist

**Número de pessoas que responderam (IDs)**

- 5173

Main Data Base
**Dados Qualitativos:**

 • CO_CURSO (Código identificador do curso)
 
 • UF (Nome da UF onde a pessoa mora)
 
 • NO_CURSO (Nome do curso)
 
 • TP_GRAU_ACADEMICO (Identifica o grau acadêmico do curso)
 • CO_CINE_ROTULO (Código que representa a área de conhecimento do curso segundo a Classificação Internacional da Educação (CINE/ISCED).)
 
 • TP_NIVEL_ACADEMICO (Representa o nível de formação acadêmica do curso)

**Graficos**

[Acesse os graficos aqui](/assets/Grafico/graficos.md)     
[Acesse os código dos graficos aqui](/src/Update_graphics.ipynb)     

## Preparação dos dados
Levando em conta a pergunta orientada a dados (Qual o nível predominante dos profissionais que trabalham com dados? (junior, pleno, senior)), as hipóteses levantadas foram:   
- **Hipótese 1: Qual o nível de trabalho que se permaneceu predominante?**    
De acordo com as expectativas da empresa, era se esperado que o nível de trabalho predominante fosse o Júnior em relação aos outros, fator o qual de fato se sucedeu durante a análise do modelo.
- **Hipótese 2: Qual o estado em que há mais Cientistas de Dados qualificados?**    
A empresa acreditava que o estado em que ocorreria a maior densidade de Cientista de Dados qualificados seria em São Paulo (SP), elemento que, de fato, ocorreu durante a análise do modelo.
- **Hipótese 3: Qual o atributo que é mais relevante para a qualificação do nível de trabalho de um Cientista de Dados?**    
Já na questão de qual atributo seria mais relevante para a qualificação do nível de trabalho de um Cientista de Dados, o grupo empresarial errou em sua hipótese ao acreditar que a Faixa Salarial seria tal atributo, o qual está errado, uma vez que o atributo mais importante na tomada de decisão do modelo foi o Quanto tempo de experiência na área de dados você tem?. 

Primeiramente, foi utilizada a base principal obtida no Kaggle. Nela, selecionamos manualmente os atributos considerados relevantes para o tema do trabalho, que é a densidade demográfica de cientistas de dados. Na tabela abaixo, justificamos os motivos pelos quais esses atributos foram escolhidos.

Em seguida, encontramos uma base auxiliar do INEP que informava quais regiões possuem faculdades com o curso de Ciência de Dados. Essa base incluía dados como latitude, longitude, código do curso, nome do curso (co_cine_rotulo), grau acadêmico, modalidade de ensino, presença de material tátil, recursos de comunicação, recursos de informática, entre outros. Dentre esses, os atributos que nos interessavam eram: código do curso, latitude, longitude, nome do curso, co_cine_rotulo, grau acadêmico e nível acadêmico. A justificativa para a escolha desses atributos, com exceção da latitude e longitude, está descrita na tabela abaixo.

Quanto à latitude e longitude, com o auxílio do ChatGPT, foi possível converter essas coordenadas em Unidades da Federação (UF), permitindo assim a associação desses dados à base principal.

Além disso, a base auxiliar apresentava códigos de cursos repetidos, uma vez que abrangia dados de diferentes anos. Esses códigos duplicados foram removidos manualmente para manter apenas entradas únicas.

Por fim, utilizamos a base auxiliar para criar um novo atributo na base principal: quantidade de cursos no estado de residência. Com a ajuda do ChatGPT, comparamos a UF informada no registro da pessoa com a quantidade de cursos disponíveis na mesma UF (informação proveniente da base auxiliar). Dessa forma, foi possível preencher esse novo atributo com base na localização geográfica do participante.

Depois disso, nós utilizamos o Python para remover alguns atributos que não são relevantes da base filtrada para responder à pergunta do primeiro modelo. Além disso, nós removemos as colunas vazias. Utilizamos a moda para substituir a pequena porcentagem de respostas no campo gênero que não indicaram "homem" ou "mulher", para que pudéssemos transformá-lo em binário. Além disso, transformamos todos os dados para int, para que, assim, o modelo induzido de árvore de decisão pudesse ser aplicado.

Na nossa análise da densidade demográfica de Cientistas de Dados, optamos por selecionar certos atributos que se mostraram particularmente relevantes para entender melhor esse cenário. Esses atributos foram escolhidos com base em sua capacidade de fornecer insights significativos sobre a distribuição e as características dessa profissão em diferentes regiões.

- `State_of_data_BR_2023_Kaggle - df_survey_2023.csv`

| Atributos                  | Motivos                                                                                     | Tipo de Dado               |
|----------------------------|---------------------------------------------------------------------------------------------|----------------------------|
| `Gênero`                   | Identificação de gênero dos cientistas de dados, importante para análises de diversidade      | Categórico   (nominal)    |
| `Faixa Etária`             | Classificação etária dos cientistas, útil para entender a distribuição etária na profissão   |  Categórico (ordinal)     |
| `Faixa Salarial`           | Níveis de renda dos cientistas, relevante para análises socioeconômicas da profissão         |  Categórico (ordinal)     |
| `Nível de experiência`     | Avaliação do nível de experiência dos cientistas, importante para entender a qualificação da força de trabalho | Categórico (ordinal)       |
| `Cientista por Estado`     | Quantidade de cientistas de dados em cada estado, essencial para mapear a distribuição geográfica     | Numérico         |
| `Raça/Etnia/Cor`           | Informações sobre a diversidade racial e étnica dos cientistas, importante para análises de inclusão  | Categórico (nominal)       |
| `Cientistas por Região`    | Distribuição de cientistas de dados por região, útil para identificar áreas com maior concentração    | Numérico         |
| `Nível de Ensino`          | Níveis educacionais dos cientistas, relevante para entender a formação acadêmica na área              | Categórico (ordinal)       |
| `Situação Empresarial`     | Status de emprego dos cientistas, importante para análises de mercado de trabalho                     | Categórico (nominal)       |
| `Cargo`                    | Títulos de trabalho ocupados pelos cientistas, útil para entender a hierarquia e funções na área      | Categórico (nominal)       
| `Área de Formação`         | Campos de estudo dos cientistas, importante para analisar a diversidade de formações na profissão     | Categórico (nominal)       |
 
- `Auxiliary_data_courses`   
     
| Atributo              | Motivos                                                                        |  Tipo de Dado  |
|-----------------------|--------------------------------------------------------------------------------|----------------|
| `CO_CURSO`              | Importante para identificar a formação acadêmica dos profissionais na área   |  Numérico |
| `CO_MUNICIPIO`         | Relevante para analisar a concentração de Cientistas de Dados em diferentes regiões        |  Numérico |
| `NO_CURSO`              | Identificar as formações mais comuns entre os Cientistas de Dados            | Categórico (nominal) |
| `CO_CINE_ROTULO`        | Categorizar dados em análises mais complexas                                 | Numérico |
| `TP_GRAU_ACADEMICO`    | Analisar nível de formação dos profissionais na área                          | Categórico (ordinal) |
| `TP_NIVEL_ACADEMICO`   | Avaliar a qualificação e especialização dos Cientistas de Dados               | Categórico (ordinal) |   

Por outro lado, identificamos que os demais atributos não contribuíram de maneira eficaz para a nossa análise. Isso nos permitiu focar em dados que realmente fazem a diferença, garantindo que nossas conclusões sejam precisas e úteis. Ao concentrar nossos esforços nos atributos mais relevantes, conseguimos obter uma visão mais clara e informada sobre a demografia dos Cientistas de Dados, facilitando a tomada de decisões e o planejamento estratégico.

---

# Indução de modelos  

---

# Modelo 1: Árvore de Decisão 

- **Perguntada Orientada a Dados:**
  Qual o nível predominante dos profissionais que trabalham com dados? (junior, pleno, senior)

- **Justificativa da escolha do modelo:**

  
O modelo Árvore de Decisão foi escolhido porque é fácil de entender e utilizar. Ele mostra de forma clara como as decisões são tomadas com base nos dados. Precisa de pouco tratamento dos dados antes de usar e consegue identificar quais informações são mais importantes para o resultado. Também é útil porque lida bem com situações complexas e pode ser ajustado para evitar erros por excesso de aprendizado.

- **Processo de amostragem de dados:**               
Foi dividido o dataset em conjuntos de treino e teste usando a função
`train_test_split` do scikit-learn, uma quantidade de dados para treino de 75% e 25% vão para teste`(test_size=0.25)`.  

- **Parâmetros utilizados:**            
Foi definido `test_size=0.25` -> uma quantidade de dados para treino de 75% e 25% vão para teste.    
`modelo.feature_importances_` -> para a avaliação dos atributos de mais importância na tomada de decisão do modelo.  
`'min_samples_split': [2, 5, 10]` -> mínimo de amostras para dividir um nó interno da árvore.   
`'max_depth': [None, 5, 10, 15]` -> para identificar qual é a melhor profundidade para a árvore.   

- **Trechos do Código:**  
```python
`X_treino, X_teste, y_treino, y_teste = train_test_split(df.drop(columns=['Nível']), df['Nível'], test_size=0.25, random_state=42)

# Define o classificador base e a grade de parâmetros
clf = DecisionTreeClassifier(random_state=42)

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
}

# Cria e executa o Grid Search
grid_search = GridSearchCV(estimator=clf,
                           param_grid=param_grid,
                           scoring='accuracy',
                           cv=5)

grid_search.fit(X_treino, y_treino)

# Usa o melhor modelo encontrado
modelo_otimizado = grid_search.best_estimator_`
```

```python
`# Obtemos a importância das features
importancias = modelo_otimizado.feature_importances_

# Associamos aos nomes das colunas
df_importancia = pd.DataFrame({
    'Feature': X_treino.columns,
    'Importância': importancias
})

# Ordenamos do mais importante para o menos
df_importancia = df_importancia.sort_values(by='Importância', ascending=False)

# Exibimos
print(df_importancia)`  
```  

```python
`accuracy_score(y_teste, previsoesTeste)
accuracy_score(y_treino, previsoesTreino)

cm = ConfusionMatrix(modelo)
cm.fit(X_treino, y_treino)
cm.score(X_treino, y_treino)

cm = ConfusionMatrix(modelo)
cm.fit(X_treino, y_treino)
cm.score(X_teste, y_teste)`
```    
- Mostra a acurácia e as matrizes de confusão de teste e treino.   
 
[Código modelo 1](/src/DecisionTreeModel.ipynb)   
[Resultados modelo 1](/assets/Results%20First%20Model/Read.md)  


## **Interpretação do modelo 1**      
- O modelo utilizado foi o `DecisionTreeClassifier` para a árvore de decisão.
- O modelo utilizou o `GridSearchCV` para a escolha dos melhores hiperparâmetros.   
- Os parâmetros principais `max_depth`, `test_size=0.25`. (Para o ajuste da profundidade da árvore e a separação de 25% dos dados para o conjunto de teste e 75% dos dados para o conjunto de treino).  
- O modelo primeiramente faz uma limpeza de dados (dropando atributos) para que os atributos irrelevantes não influenciem na tomada de decisão.
- Em segundo lugar, os dados relevantes foram transformados em numéricos, para a execução da árvore de decisão.
- O atributo nível profissional e de ensino é transformado em númerico crescente, enquanto o de gênero é transformado em númerico binário (0 = Júnior, 1 = Pleno e 2 = Sênior) (0 = Masculino e 1 = Feminino). 
- O atributo que mais influenciou na tomada de decisão do modelo, foi o Quanto tempo de experiência na área de dados e a Faixa Salarial.
- Os atributos que mais influenciaram, fizeram com que o modelo não utilizasse outros atributos, já que a partir desses atributos o modelo já tomava a decisão das classes.
- A partir, da ánalise da precisão de treinos e testes, é possível observar que o modelo é mais adequado para identificar Juniores e Seniores do que Plenos. Essa ánalise se deve a precisão e o desempenho que os níveis obtiveram.   
- O modelo apresenta um leve overfitting, devido ao fato do treino possuir acurácia maior que o teste, porém pela diferença entre treino e teste não ser alta (aproximadamente 5%), ele apresenta somente um leve overfitting.   
- Pleno por apresentar um baixo recall, se torna mais díficil de identificar, fator que leva o modelo a confundir Pleno com as outras classes algumas vezes.   
- O modelo em sí apresenta 68% de acerto nas classificações de níveis.
 
## **Conjunto de Dados utilizados (Ordem decrescente de importância aproximada)**   
- Quanto tempo de experiência na área de dados você tem? (59%)  
- Faixa Salarial (32%)  
- Idade (4%)   
- Cargo Atual (2%)     
- Nível de Ensino (1%)  
- Área de Formação (0.8%)  
- Cor/raca/etnia (0.7%)  
- UF onde mora (0.3%)
- Setor (0.3%)       
- Faixa idade (0.1%)             
- Gênero (0%)
- Vive no Brasil (0%)           
- PCD (0%)         
- Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados? (0%)
- Existe faculdade no Estado (0%)
![image](https://github.com/user-attachments/assets/06102fbf-0915-4615-a115-1838cce33ae2)    
 

**Possíveis Melhoras:**  
- Ajustes hiperparâmetros (ajudar a diferenciação entre Júnior, Pleno e Sênior).  
- Observar quais atributos foram mais importantes para escolha dos níveis.
- Balancear os dados.

## **Conclusão:**   
O modelo é razoável, porém pode ser melhorado. Ele apresenta diversas falhas, principalmente na classificação dos níveis, as quais diminuem a porcentagem de acertos. O modelo também apresenta acerto maiores no treino do que nos testes, sendo estes aproximados, indicando um leve overfitting. Logo, com certos ajustes e melhorias, o modelo tende a se tornar equilibrado.

---

# Modelo 2: Random Forest

- **Perguntada Orientada a Dados:**
  Qual o nível predominante dos profissionais que trabalham com dados? (junior, pleno, senior)
- **Justificativa da escolha do modelo:**

O modelo Random Forest foi escolhido porque ele possue características que o tornam uma das técnicas mais robustas e eficazes em problemas de classificação por: "Alta capacidade preditiva" em que o modelo combina múltiplas árvores de decisão, o que reduz significativamente a variância do modelo e melhora a generalização, evitando problemas de overfitting comuns; "Robustez a ruídos e outliers" onde devido ao processo de agregação (bagging), o modelo é menos sensível a dados ruidosos e a outliers, garantindo previsões mais estáveis e confiáveis; "Facil implementação no modelo de arvore de decição" que para fazer o modelo arvore de decição para random forest é bem facil.
- **Processo de amostragem de dados:**
 
Foi dividido o dataset em conjuntos de treino e teste usando a função `train_test_split` do scikit-learn, uma quantidade de dados para treino de 75% e 25% vão para teste`(test_size=0.25)` e com um random_state de 42.  

- **Parâmetros utilizados:**            
Foi definido `test_size=0.25` -> uma quantidade de dados para treino de 75% e 25% vão para teste.    
`modelo.feature_importances_` -> para a avaliação dos atributos de mais importância na tomada de decisão do modelo.  
`'ccp_alpha': [0.0, 0.01]` -> controle de overfitting.  
`'max_depth': [None, 5, 20]` -> para a profundidade da árvore.  
`'n_estimators': [10, 20, 50]` -> para o número de árvores criadas.   
`'min_impurity_decrease'` -> controle crescimento da árvore.  

- **Trechos do Código:**  
```python
`# Separação em X e Y
X_treino, X_teste, y_treino, y_teste = train_test_split(
    df.drop(columns=['Nível']), df['Nível'], test_size=0.25, random_state=42)

# Grade de hiperparâmetros
param_grid = {
    'n_estimators': [10, 20, 50],
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 5, 20],
    'min_impurity_decrease': [0.0, 0.001],
    'ccp_alpha': [0.0, 0.01]
}

# Modelo base
clf = RandomForestClassifier(random_state=42)

# Grid Search com validação cruzada
grid_search = GridSearchCV(estimator=clf,
                           param_grid=param_grid,
                           scoring='accuracy',
                           cv=5,
                           n_jobs=-1)

# Treinamento com Grid Search
grid_search.fit(X_treino, y_treino)

# Melhor modelo encontrado
melhor_modelo = grid_search.best_estimator_`
```

```python
`# Importância das features
importancias = melhor_modelo.feature_importances_
df_importancia = pd.DataFrame({
    'Feature': X_treino.columns,
    'Importância': importancias
}).sort_values(by='Importância', ascending=False)

print("\nImportância das Features:")
print(df_importancia)`
```

```python
`accuracy_score(y_teste, previsoesTeste)
accuracy_score(y_treino, previsoesTreino)

cm = ConfusionMatrix(modelo)
cm.fit(X_treino, y_treino)
cm.score(X_treino, y_treino)

cm = ConfusionMatrix(modelo)
cm.fit(X_treino, y_treino)
cm.score(X_teste, y_teste)`
```    
- Mostra a acurácia e as matrizes de confusão de teste e treino.      

[Código modelo 2](/src/RandomForestModel(1)(1).ipynb)   
[Resultados modelo 2](/assets/Results%20Second%20Model/read.md) 
  
## **Interpretação do modelo 2**   

- O modelo utilizado foi o `RandomForestClassifier` para a Floresta aleatória.
- O modelo utilizou o `GridSearchCV` para a escolha dos melhores hiperparâmetros.
- O principal objetivo é a classificação dos níveis (Júnior, Pleno, Sênior), com base em atributos do perfil do indivíduo.   
- Os parâmetros principais `n_estimators`, `max_depth`, `test_size=0.25`, `ccp_alpha` (Para o número de árvores, ajuste da profundidade da árvore, a separação de 25% dos dados para o conjunto de teste e 75% dos dados para o conjunto de treino, e para o controle do overfitting do modelo).  
- O modelo primeiramente faz uma limpeza de dados (dropando atributos) para que os atributos irrelevantes não influenciem na tomada de decisão.  
- Em segundo lugar, ele define os níveis profissionais e de ensino em números crescentes e define o gênero para número binários (0 = Júnior, 1 = Pleno e 2 = Sênior) (0 = Masculino e 1 = Feminino).   
- O modelo apresenta uma divisão de dados aleatória para cada árvore de decisão formada, em que cada nó um conjunto aleatório de atributos é testado.    
- O modelo possui como atributo mais influente para a tomada de decisão, o Quanto tempo de experiência na área de dados e a Faixa Salarial.    
- O modelo apresenta uma diferença de 22% entre treino e teste, fator que indica que o modelo apresenta overfitting.   
- Pleno apresenta uma queda na precisão e recall, demonstrando que o modelo possui dificuldade em acertar e identificar a classe Pleno.   
- O modelo em sí apresenta 70% de acerto nas classificações de níveis.   

## **Conjunto de Dados utilizados (Ordem decrescente de importância aproximada)** 
- Quanto tempo de experiência na área de dados você tem? (25%)  
- Faixa Salrial (20%)  
- Idade (10%)   
- Setor (6%)       
- Nível de Ensino (6%)  
- Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados? (6%)   
- Faixa idade (6%)    
- Cargo Atual (5%)        
- UF onde mora (5%)    
- Área de Formação (4%)   
- Cor/raca/etnia (3%)   
- Existe faculdade no Estado (2%)   
- Gênero (1%)    
- PCD (0.05%)         
- Vive no Brasil (0%)   
![image](https://github.com/user-attachments/assets/661fe0e8-5db3-405f-b309-5245f005092b)     
  
**Possíveis Melhorias:**  
- Ajustes hiperparâmetros (ajudar a diferenciação entre Júnior, Pleno e Sênior).  
- Remover mais atributos que sejam irrelevantes.    
- Balancear os dados.  

## **Conclusão:**   
O modelo tem uma boa acurácia porém precisa ser melhorado, já que possui overfitting, ele continua tendo dificuldade na identificação de classes, fator o qual diminui a acurácia geral e compromete no resultado final do modelo. Um dos principais fatores que levam ao desequilibrio do modelo, se deve a quantidade de atributos utilizados. O modelo possui baixa precisão na classe Pleno, fator que precisa ser melhorado. Logo com certas melhorias e com o controle do overfitting o modelo tende a se tornar equilibrado para a classificação dos níveis profissionais.

---

# Modelo Extra associação
Modelo foi criado para responder a pergunta: quais os top 10 atributos aparecem mais frequente divididos por regiao quando a pessoa trabalha com dados?

- [Código](assets/Google Colab/AssociationModel.ipynb)

Resultados: 
Região: Sudeste
  - Qual sua situação atual de trabalho?_Empregado (CLT): apareceu em 806 regras
  - Existe faculdade no Estado: apareceu em 733 regras
  - Gênero_Masculino: apareceu em 623 regras
  - Cor/raca/etnia_Branca: apareceu em 293 regras
  - Numero de Funcionários_Acima de 3.000: apareceu em 22 regras

• Região: Nordeste
  - Gênero_Masculino: apareceu em 2 regras
  - Qual sua situação atual de trabalho?_Empregado (CLT): apareceu em 2 regras

• Região: Sul
  - Qual sua situação atual de trabalho?_Empregado (CLT): apareceu em 33 regras
  - Cor/raca/etnia_Branca: apareceu em 31 regras
  - Gênero_Masculino: apareceu em 26 regras

Interpretação
Não foram criadas regras da região Norte e Centro Sul, possivelmente poissivelmente pois não há muitos cientistas de dados nessas regiões e por isso nenhuma regra ou poucas foram criadas para essas regiões.

# Análise comparativa dos modelos

O modelo decision tree and random forest não estão muito separados um do outro, sendo que o random forest utiliza diversas decisões trees.
A decision tree pega todos os atributos disponíveis e faz um treinamento usando parte dos dados (geralmente entre 70) mas como utiliza de todos os atributos isso pode causar um over fitting mas conseguindo uma acuracy boa, enquanto isso a random forest pega todos os atributos e os separa em diferentes decision trees (onde pode ser colocado até o mesmo atributos várias vezes numa árvore de decisão) e usando disso ele pega dicas de cada árvore e no final cria um modelo no qual e geralmente melhor que a árvore de decisão e tem menos chance de ocorrer over fitting e obtendo uma acuracy mais consistente melhor mas sendo mais pesada


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresentação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS

**[1]** - DATA HACKERS. State of Data - Brasil 2023. Kaggle, 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 2 de abril 2025.


**[2]** - MONITORIA DE SISTEMAS INTELIGENTES. Arquivo utilizado na aula de plantão PUC de Sistemas Inteligentes, realizada no prédio do PIC, em 6 de maio de 2025. Arquivo disponibilizado no grupo do Microsoft Teams.

**[3]** - INEP. Censo da Educação Superior. [S.l.]: Power BI, [s.d.]. Disponível em: https://app.powerbi.com/view?r=eyJrIjoiMGJiMmNiNTAtOTY1OC00ZjUzLTg2OGUtMjAzYzNiYTA5YjliIiwidCI6IjI2ZjczODk3LWM4YWMtNGIxZS05NzhmLWVhNGMwNzc0MzRiZiJ9&pageName=ReportSection4036c90b8a27b5f58f5. Acesso em: 10 de março. 2025.


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado no repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




