# Análise de densidade demografica de cientista de dados


**Ian Vinicius Marinho Malta, ian.malta@sga.pucminas.br**

**João Gabriel de Melo Neves, jgmneves@sga.pucminas.br**

**Thiago Couto Ferreira, thiago.couto@sga.pucminas.br**

**Thales Ribeiro Melo, thales.melo@sga.pucminas.br**

**Arthur Gabriel Marques Coelho Mourão, agmcmourao@sga.pucminas.br**

---

**Prof. Hugo Bastos de Paula**

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução



Com o crescimento e procura da área de Ciência de Dados surge uma necessidade das empresas de localizar onde estão esses profissionais e quais são suas qualificações. Portanto, nossa empresa visa justamente isso: que o empregador saiba onde localizá-los e quais lugares têm a melhor qualificação.

###    Contextualização


-Nos últimos anos, a Ciência de Dados tornou-se uma das áreas mais promissoras no mercado de tecnologia, impulsionada pelo crescimento do volume de dados e pela necessidade de extração de informações estratégicas para tomada de decisões. Empresas de diversos setores passaram a investir na contratação de Cientistas de Dados para aprimorar seus processos, otimizar operações e obter insights valiosos a partir da análise de grandes conjuntos de dados.  

-No entanto, apesar da alta demanda por esses profissionais, a distribuição geográfica de Cientistas de Dados no Brasil não é homogênea. Alguns municípios apresentam uma concentração elevada de especialistas, enquanto outros enfrentam escassez de mão de obra qualificada. Essa desigualdade dificulta a tomada de decisão por parte de novas empresas que desejam ingressar nesse setor, pois nem sempre há informações acessíveis sobre onde estão localizados os profissionais mais capacitados e quais regiões oferecem melhores oportunidades de crescimento.  

-Diante desse cenário, a nossa empresa desenvolve um sistema inteligente capaz de mapear a densidade de Cientistas de Dados por município, facilitando a identificação de regiões saturadas ou carentes desses profissionais. Além disso, o sistema permite uma análise aprofundada das qualificações exigidas pelo mercado, auxiliando empresas a encontrarem especialistas adequados para suas necessidades. Dessa forma, contribuímos para um melhor planejamento estratégico tanto do setor empresarial quanto do setor educacional, promovendo um equilíbrio mais eficiente entre oferta e demanda no mercado de Ciência de Dados.

###    Problema


O avanço da tecnologia e da inteligência artificial tem impulsionado a demanda por profissionais qualificados na área de Ciência de Dados. No entanto, a distribuição desses profissionais pelo território brasileiro ainda não é homogênea, dificultando tanto a alocação estratégica de novas empresas quanto a oferta educacional adequada para formar especialistas nessa área.

###    Objetivo geral

Desenvolver um sistema inteligente para mostrar geograficamente a densidade de cientistas de dados por municipio e indicar quais municipios estão saturados para que empresas tenham uma maior facilidade de contratar cientistas de dados ao abrirem suas empresas.

####    Objetivos específicos

- Analisar os dados e por meio deles obter informações sobre a demanda do curso Ciência de dados nos estados do Brasil, sendo esse importante para o planejamento do local em que as novas empresas dessa área serão melhor alocadas.

- Analisar os dados e por meio deles obter informações sobre o número de faculdades que atendem a Ciência de Dados nos estados do Brasil, de tal forma a ser importante para a implementação de tal nas regiões que ainda não se efetivou o curso em suas faculdades.

- Produzir um sistema eficiente, capaz de gerar dados que possibilitam expor os municípios que apresentam maiores quantidades de Cientista de Dados qualificados.

- Criar um sistema eficiente, o qual proporciona uma análise mais profunda sobre as qualidades necessárias para que um Cientista de Dados possa ser considerado especializado ( a partir de uma descrição de dados com variáveis).

###    Justificativas  

-O avanço da tecnologia e da inteligência artificial tem impulsionado a demanda por profissionais qualificados na área de Ciência de Dados. No entanto, a distribuição desses profissionais pelo território brasileiro ainda não é homogênea, dificultando tanto a alocação estratégica de novas empresas quanto a oferta educacional adequada para formar especialistas nessa área. Nesse contexto, torna-se essencial o desenvolvimento de um sistema inteligente que mapeie geograficamente a densidade de Cientistas de Dados por município, permitindo uma análise aprofundada sobre regiões saturadas ou deficitárias desses profissionais.  

-Empresas que buscam expandir seus negócios para novas localidades enfrentam dificuldades para encontrar mão de obra qualificada, especialmente em municípios onde a oferta de Cientistas de Dados é escassa. O sistema proposto facilitará esse processo ao fornecer informações detalhadas sobre a concentração desses profissionais e os municípios com maior ou menor disponibilidade de talentos, possibilitando uma tomada de decisão mais assertiva na escolha de onde estabelecer suas operações.  

-Além do impacto direto na alocação empresarial, o sistema também contribuirá para o setor educacional. A identificação da demanda por cursos de Ciência de Dados permitirá que universidades e instituições de ensino superior ajustem sua oferta acadêmica, promovendo a expansão do curso para regiões com carência de formação na área. Esse fator é crucial para equilibrar a oferta e a demanda de profissionais no mercado, evitando tanto a saturação quanto a escassez de Cientistas de Dados em determinadas localidades.  

-Por fim, ao integrar variáveis que qualificam um Cientista de Dados especializado, o sistema também possibilitará uma análise mais refinada das competências exigidas no mercado, auxiliando empresas na busca por profissionais com habilidades específicas. Dessa forma, o projeto se justifica não apenas pela inovação tecnológica envolvida, mas também pelo seu potencial impacto no desenvolvimento econômico e educacional do Brasil, promovendo um equilíbrio mais eficiente entre formação acadêmica, demanda do mercado e crescimento empresarial.

##    Público alvo
Os CEOs e chefes de empresas novas na área de Ciencia de Dados, de tal forma a auxiliar essas novas empresas a iniciarem sua trajetória procurando profissionais qualificados e um município propenso para tal atividade.

## Análise exploratórida dos dados

###    Dicionário de dados
**Main Data Base**

| Data                                                                                                                      | Description                                                                                   | Data Type                                             |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Id                                                                                                                        | O número da identidade de cada pessoa que respondeu à pesquisa                                | Dados qualitativos (polinomial não ordinal)           |
| Idade                                                                                                                     | Idade da pessoa que respondeu à pesquisa                                                      | Dados quantitativos (discretos)                       |
| Faixa idade                                                                                                               | A qual faixa de idade a pessoa pertence, sendo que cada faixa possui 4 anos entre uma e outra | Dados qualitativos (polinomial ordinal)               |
| Gênero                                                                                                                    | Gênero da pessoa que respondeu à pesquisa                                                     | Dados qualitativos (binomial simétrico)               |
| Cor/raça/etnia                                                                                                            | Cor de pele/raça/etnia da pessoa que respondeu à pesquisa                                     | Dados qualitativos (polinomial não ordinal)           |
| PCD                                                                                                                       | Se a pessoa que respondeu à pesquisa possui alguma deficiência                                | Dados qualitativos (binomial simétrico)               |
| Vive no Brasil                                                                                                            | Se a pessoa que respondeu à pesquisa mora no Brasil ou não                                    | Dados qualitativos (binomial assimétrico)             |
| Estado onde mora                                                                                                          | Qual estado nacional a pessoa que respondeu à pesquisa mora                                   | Dados qualitativos (polinomial não ordinal)           |
| UF onde mora                                                                                                              | Sigla do estado de onde a pessoa mora                                                         | Dados qualitativos (polinomial não ordinal)           |
| Região onde Mora                                                                                                          | Qual das 5 regiões do Brasil a pessoa mora (Norte, Nordeste, Centro-Oeste, Sudeste e Sul)     | Dados qualitativos (polinomial não ordinal)           |
| Nível de Ensino                                                                                                           | Qual o nível de ensino superior da pessoa                                                     | Dados qualitativos (polinomial ordinal)               |
| Área de Formação                                                                                                          | Qual das áreas disponíveis na base de dados a pessoa se formou                                | Dados qualitativos (polinomial ordinal)               |
| Qual sua situação atual de trabalho?                                                                                      | Se a pessoa está trabalhando, procurando emprego ou desempregada                              | Dados qualitativos (polinomial ordinal)               |
| Setor                                                                                                                     | Em qual área do setor de trabalho a pessoa atua na empresa                                    | Dados qualitativos (polinomial ordinal)               |
| Número de Funcionários                                                                                                    | Quantos funcionários tem na empresa em que a pessoa trabalha                                  | Dados quantitativos (discretos)                       |
| Cargo Atual                                                                                                               | Qual o cargo da pessoa dentro da área de ciência de dados                                     | Dados qualitativos (polinomial ordinal)               |
| Nível                                                                                                                     | Há quanto tempo a pessoa está trabalhando no seu setor                                        | Dados qualitativos (polinomial ordinal)               |
| Faixa salarial                                                                                                            | Qual o salário médio mensal da pessoa                                                         | Dados qualitativos (polinomial ordinal)               |
| Quanto tempo de experiência na área de dados você tem?                                                                    | Quanto tempo a pessoa trabalha na área de ciência de dados                                    | Dados qualitativos (polinomial ordinal)               |
| Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados? | Quanto tempo a pessoa tem em outras áreas que contribuem para a atuação com dados             | Dados qualitativos (polinomial não ordinal)           |
| Qual o número aproximado de pessoas que atuam com dados na sua empresa hoje?                                              | Número de funcionários que trabalham com dados na empresa                                     | Dados quantitativos (discretos)                       |
| Cientista de Dados/Data Scientist                                                                                         | Se a pessoa é ou não cientista de dados                                                       | Dados qualitativos (binomial assimétrico)             |
| Quantidade de Cursos no estado onde mora                                                                                  | A quantidade de cursos de ciência de dados que tem na UF da pessoa                            | Dados quantitativos (discretos)                       |

**Auxiliary Data Base**

| Data               | Description                                                                                   | Data Type                                       |
|--------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| CO_CURSO           | Código identificador do curso                                                                 | Dados qualitativos (polinomial não ordinal)     |
| UF                 | Nome da UF onde a pessoa mora                                                                 | Dados qualitativos (polinomial não ordinal)     |
| NO_CURSO           | Nome do curso                                                                                 | Dados qualitativos (polinomial não ordinal)     |
| TP_GRAU_ACADEMICO  | Identifica o grau acadêmico do curso (ex.: Bacharelado, Licenciatura, Tecnológico), com base em um código numérico. | Dados qualitativos (polinomial ordinal)         |
| CO_CINE_ROTULO     | Código que representa a área de conhecimento do curso segundo a Classificação Internacional da Educação (CINE/ISCED). | Dados qualitativos (polinomial não ordinal)     |
| TP_NIVEL_ACADEMICO | Representa o nível de formação acadêmica do curso (ex.: Graduação, Mestrado, Doutorado), codificado numericamente. | Dados qualitativos (polinomial ordinal)         |


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

## Preparação dos dados
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



## Indução de modelos  

### Modelo 1: Árvore de Decisão 

- **Perguntada Orientada a Dados:**
  
Em qual região existem profissionais mais qualificados? (junior, pleno, senior)
- **Justificativa da escolha do modelo:**

  
O modelo Árvore de Decisão foi escolhido porque é fácil de entender e utilizar. Ele mostra de forma clara como as decisões são tomadas com base nos dados. Precisa de pouco tratamento dos dados antes de usar e consegue identificar quais informações são mais importantes para o resultado. Também é útil porque lida bem com situações complexas e pode ser ajustado para evitar erros por excesso de aprendizado.

- **Processo de amostragem de dados:**               
Foi dividido o dataset em conjuntos de treino e teste usando a função
`train_test_split` do scikit-learn, uma quantidade de dados para treino de 75% e 25% vão para teste`(test_size=0.25)`. 

- **Parâmetros utilizados:**            
Foi definido test_size=0.25, ou seja, uma quantidade de dados para treino de 75% e 25% vão para teste

- **Exemplo de saida:**    
- Idade: 
- faixa salarial: 
- area da formação: 
- idade: 
- UF onde mora:
- Cor/ raça / etnia
- Nivel

Trechos do código comentados:

# Divisão do dataset em treino e teste
`X_treino, X_teste, y_treino, y_teste = train_test_split(df.drop(columns=['Nível']), df['Nível'], test_size=0.25, random_state=42)`       
- Aqui, garantimos que 75% dos dados vão para treino e 25% para teste, com uma semente fixa para reprodutibilidade.

# Grafico de acerto
0 = Junior
1 = Pleno
2 = Senior

`cm = ConfusionMatrix(modelo)`
`cm.fit(X_treino, y_treino)`
`cm.score(X_teste, y_teste)`

- Aqui é feito o gráfico para mostrar os acertos e erros do programa

![17467887836121283290005492835812](https://github.com/user-attachments/assets/168dea1b-6386-4e51-93c9-714ce6851708)


### Modelo 2: Random Forest

- **Perguntada Orientada a Dados: Quais atributos aparecem mais frequente em cada regiao quando a pessoa trabalha com dados? **

  Em qual região existem profissionais mais qualificados? (junior, pleno, senior)
- **Justificativa da escolha do modelo:**

O modelo Random Forest foi escolhido porque ele possue características que o tornam uma das técnicas mais robustas e eficazes em problemas de classificação por: "Alta capacidade preditiva" em que o modelo combina múltiplas árvores de decisão, o que reduz significativamente a variância do modelo e melhora a generalização, evitando problemas de overfitting comuns; "Robustez a ruídos e outliers" onde devido ao processo de agregação (bagging), o modelo é menos sensível a dados ruidosos e a outliers, garantindo previsões mais estáveis e confiáveis; "Facil implementação no modelo de arvore de decição" que para fazer o modelo arvore de decição para random forest é bem facil.
- **Processo de amostragem de dados:**
  
Foi dividido o dataset em conjuntos de treino e teste usando a função `train_test_split` do scikit-learn, uma quantidade de dados para treino de 71% e 29% vão para teste`(test_size=0.29)` e com um random_state de 69. 
- **Parâmetros Utilizados:**

test_size=0.29, n_estimators=100, max_depth=10, random_state=69, 
- **Trechos de Código Comentados:**

# **Resultados Modelo 1**   

- Visualização da matriz de confusão (treino)     
![image](https://github.com/user-attachments/assets/eec412cf-1a4d-4c7e-9a07-6bdb414b5bc5)   
Treino: 0.7289 -> O modelo acerta aproximadamente 72.9%.     

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/bed24ec5-8515-4859-ae8f-c1ca84aa801b)    
Teste: 0.6795 -> O modelo acerta aproximadamente 67.9%.    

# **Precisão treino**       

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.71      | 0.84   | 0.77     | 591     |
| Pleno   | 0.66      | 0.61   | 0.63     | 801     |
| Sênior  | 0.82      | 0.77   | 0.79     | 788     |    

**Acurácia geral:** 0.73

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.73      | 0.74   | 0.73     | 2180    |
| Weighted Avg| 0.73      | 0.73   | 0.73     | 2180    |

# **Precisão teste**  

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.66      | 0.84   | 0.74     | 171     |
| Pleno   | 0.62      | 0.55   | 0.58     | 280     |
| Sênior  | 0.76      | 0.71   | 0.73     | 276     |  

**Acurácia geral:** 0.68

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.68      | 0.70   | 0.68     | 727     |
| Weighted Avg| 0.68      | 0.68   | 0.68     | 727     |    

- O modelo de teste apresentou uma queda na Acurácia, principalmente devido a classe Pleno.

# **Árvore de decisão finalizada**    
![image](https://github.com/user-attachments/assets/7f53abc8-3d15-4df8-8a27-e8d4e15c86d4)    

   
# **Interpretação do modelo 1**      
- O modelo utilizado foi o `DecisionTreeClassifier` para a árvore de decisão.
- Os parâmetros principais `max_depth=5`, `test_size=0.25`. (Para o ajuste da profundidade da árvore e a separação de 25% dos dados para o conjunto de teste e 75% dos dados para o conjunto de treino).  
- O modelo primeiramente faz uma limpeza de dados (dropando atributos) para que os atributos irrelevantes não influenciem na tomada de decisão.
- Em segundo lugar, os dados relevantes foram transformados em numéricos, para a execução da árvore de decisão.
- O atributo nível profissional e de ensino é transformado em númerico crescente, enquanto o de gênero é transformado em númerico binário (0 = Júnior, 1 = Pleno e 2 = Sênior) (0 = Masculino e 1 = Feminino). 
- O atributo que mais influenciou na tomada de decisão do modelo, foi a Faixa Salarial.
- A partir, da ánalise da precisão de treinos e testes, é possível observar que o modelo é mais adequado para identificar Juniores e Seniores do que Plenos. Essa ánalise se deve a precisão e o desempenho que os níveis obtiveram.   
- O modelo apresenta overfitting, devido ao fato do treino possuir acurácia maior que o teste, porém pela diferença entre treino e teste não ser alta (aproximadamente 5%), ele apresenta somente um pequeno overfitting.   
- Pleno por apresentar um baixo recall, se torna mais díficil de identificar, fator que leva o modelo a confundir Pleno com as outras classes algumas vezes.   
- O modelo em sí apresenta 68% de acerto nas classificações de níveis.  

**Possíveis Melhoras:**  
- Ajustes hiperparâmetros (ajudar a diferenciação entre Júnior, Pleno e Sênior).  
- Observar quais atributos foram mais importantes para escolha dos níveis.
- Balancear os dados.

**Conclusão:**   
O modelo é razoável, porém pode ser melhorado. Ele apresenta diversas falhas, principalmente na classificação dos níveis, as quais diminuem a porcentagem de acertos. O modelo também apresenta acerto maiores no treino do que nos testes, sendo estes aproximados, indicando um leve overfitting . Logo, com certos ajustes e melhorias, o modelo tende a se tornar equilibrado.


# **Resultados obtidos com o modelo 2.**    
- Visualização da matriz de confusão (treino)     
![image](https://github.com/user-attachments/assets/2d330b06-3f4d-4af6-a995-6426a42155ba)     
Treino: 0.8914 -> O modelo acerta aproximadamente 89.1%.     

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/96a9cd2c-d187-484e-b5e4-9cf0f1ce6597)    
Teste: 0.7120 -> O modelo acerta aproximadamente 71.2%.     

# **Precisão treino**       

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.95      | 0.86   | 0.90     | 534     |
| Pleno   | 0.83      | 0.90   | 0.86     | 769     |
| Sênior  | 0.92      | 0.91   | 0.92     | 760     |    

**Acurácia geral:** 0.89 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.90      | 0.89   | 0.89     | 2063    |
| Weighted Avg| 0.89      | 0.89   | 0.89     | 2063    |

# **Precisão teste**  

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.77      | 0.68   | 0.72     | 228     |
| Pleno   | 0.61      | 0.67   | 0.64     | 312     |
| Sênior  | 0.80      | 0.78   | 0.79     | 304     |  

**Acurácia geral:** 0.71 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.72      | 0.71   | 0.72     | 844     |
| Weighted Avg| 0.72      | 0.71   | 0.71     | 844     |    

- O modelo de teste apresentou uma queda na Acurácia, principalmente devido a classe Pleno.  

# **Random Forest finalizada**    
![download](https://github.com/user-attachments/assets/2bc3dbe9-56b2-4457-8451-12da9e1b2177)  

# **Interpretação do modelo 2**   

- O modelo utilizado foi o `RandomForestClassifier` para a Floresta aleatória.
- O principal objetivo é a classificação dos níveis (Júnior, Pleno, Sênior), com base em atributos do perfil do indivíduo.   
- Os parâmetros principais `n_estimators=100`, `max_depth=10`, `test_size=0.29` (Para o número de árvores, ajuste da profundidade da árvore e a separação de 29% dos dados para o conjunto de teste e 71% dos dados para o conjunto de treino).
- O modelo primeiramente faz uma limpeza de dados (dropando atributos) para que os atributos irrelevantes não influenciem na tomada de decisão.
- Em segundo lugar, ele define os níveis profissionais e de ensino em números crescentes e define o gênero para número binários (0 = Júnior, 1 = Pleno e 2 = Sênior) (0 = Masculino e 1 = Feminino).   
- O modelo apresenta uma divisão de dados aleatória para cada árvore de decisão formada, em que cada nó um conjunto aleatório de atributos é testado.    
- O modelo possui como atributo mais influente para a tomada de decisão, a Idade e o setor no qual o indivíduo trabalha.    
- O modelo de Random Forest apresenta overfitting, já que a diferença entre treino e teste é alta (aproximadamente 18%).   
- Pleno apresenta uma queda na precisão, demonstrando que o modelo possui dificuldade em acertar e identificar a classe Pleno.   
- O modelo em sí apresenta 71% de acerto nas classificações de níveis.   

**Possíveis Melhoras:**  
- Ajustes hiperparâmetros (ajudar a diferenciação entre Júnior, Pleno e Sênior).  
- Remover mais atributos que sejam irrelevantes.  
- Reduzir a complexidade do modelo (diminuindo a profundidade de cada árvore)   
- Balancear os dados.  

**Conclusão:**   
O modelo é razoável porém precisa ser melhorado, ele continua tendo dificuldade na identificação de classes, fator o qual diminui a acurácia geral e compromete no resultado final do modelo. Um dos principais fatores que levam ao desequilibrio do modelo, se deve a quantidade de atributos utilizados. O modelo possui baixa precisão na classe Pleno, fator que precisa ser melhorado. Logo com certas melhorias o modelo tende a se tornar equilibrado para a classificação dos níveis profissionais.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS

Como um projeto de sistema inteligente não requer revisão bibliográfica, 
a inclusão das referências não é obrigatória. No entanto, caso você 
tenha utilizado referências na introdução ou deseje 
incluir referências relacionadas às tecnologias, padrões, ou metodologias 
que serão usadas no seu trabalho, relacione-as de acordo com a ABNT.

Verifique no link abaixo como devem ser as referências no padrão ABNT:

http://www.pucminas.br/imagedb/documento/DOC\_DSC\_NOME\_ARQUI20160217102425.pdf

Por exemplo:

**[1]** - DATA HACKERS. State of Data - Brasil 2023. Kaggle, 2023. Disponível em: https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023. Acesso em: 2 de abril 2025.


**[2]** - MONITORIA DE SISTEMAS INTELIGENTES. Arquivo utilizado na aula de plantão PUC de Sistemas Inteligentes, realizada no prédio do PIC, em 6 de maio de 2025. Arquivo disponibilizado no grupo do Microsoft Teams.

**[3]** - 

**[4]** - 

**[5]** - 


# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




