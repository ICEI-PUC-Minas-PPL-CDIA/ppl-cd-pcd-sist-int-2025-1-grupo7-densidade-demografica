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

**1- Gênero**

- Moda: Masculino(3883)

<img src=https://github.com/user-attachments/assets/41674eef-491e-49f3-894f-d0d98a24aed8 width="600"/>  

- Masculino: 75.1%  
- Feminino: 24.5%  
- preferiu não informar: 0.3%  
- outros: 0.1%  

**2- Faixa Etária**

- Moda: 25-29(1627)

<img src=https://github.com/user-attachments/assets/b1a4698c-c1e0-4fbc-9ede-555dad8b1f9f width="600"/>  

- 17-21: 3.4%  
- 22-24: 9.4%  
- 25-29: 31.5%  
- 30-34: 25.9%  
- 35-39: 14.8%   
- 40-44: 8.0%  
- 45-49: 3.5%  
- 50-54: 2.1%  
- mais que 55: 1.4%  

**3- Faixa Salarial**

- Moda: 6.001-12.000(1640)

<img src=https://github.com/user-attachments/assets/5756a64d-768c-4888-a291-3a0f3d1601e7 width="600"/>  

- 0-2.000: 14.7%  
- 2.001-6.000: 26.6%  
- 6.001-12.000: 31.7%  
- 12.001-16.000: 12.3%  
- 16.001-20.000: 6.1%  
- mais que 20.001: 8.5%  

**4- Nível de experiência**

- Moda: 1 a 2 anos(1186)

<img src=https://github.com/user-attachments/assets/173c4a9c-6b2b-4e36-9715-72018a2aa83b width="600"/>  

- menos que 1 ano: 9.0%  
- 1 a 2 anos: 22.9%  
- 3 a 4 anos: 21.2%  
- 4 a 6 anos: 15.5%  
- mais que 6 anos: 18.4%  
- não possui experiência: 13.1%  

**5- Ciêntista por Estado**

Moda: São Paulo(SP)(2073)

<img src=https://github.com/user-attachments/assets/fbf05279-b98e-4beb-8bb3-6792579e70c2 width="600"/> 

**6- Raça/Etnia/Cor**

- Moda: Branca(3331)

<img src=https://github.com/user-attachments/assets/5d53a1b2-a41d-481a-8442-32b445b20284 width="600"/>  

- Branca: 64.4%  
- Parda: 24.3%  
- Amarela: 2.8%  
- preta: 7.3%  
- preferiu não informar: 0.6%  
- outra: 0.3%  
- Indígena: 0.3%  

**7- Ciêntistas por Região**

- Moda: Sudeste(3172)

<img src=https://github.com/user-attachments/assets/9c5fa378-d068-4267-b030-18a647e4adaf width="600"/>   

- Sudeste: 61.3%  
- Sul: 18.6%  
- Nordeste: 11.8%  
- Centro-Oeste: 6.7%  
- Norte: 1.7%  

**8- Nível de Ensino**

- Moda: Graduação/Bacharelado(2442)

<img src=https://github.com/user-attachments/assets/2802abf5-f8db-4d37-a969-b571b5b13880 width="600"/>  

- Graduação/Bacharelado: 47.2%  
- Pós-Graduação: 34.5%     
- Mestrado: 12.3%   
- Doutorado: 4%  
- sem graduação: 2%  

**9- Situação Empresarial**

- Moda: Empregado(CLT)(4134)

<img src=https://github.com/user-attachments/assets/d9927137-4c2e-41e2-a553-c7ad59f6bdf7 width="600"/>  

- Empregado(CLT): 79.9%  
- Desempregado: 7.0%  
- Estagiário: 4.0%  
- Estudante: 1.9%  
- Servidor Público: 2.8%  
- outros: 4.4%  

**10- Cargo**

- Moda: Analista de dados(em geral)(1829)

<img src=https://github.com/user-attachments/assets/b2dc972a-465f-478e-bae8-c1ac21d3b873 width="600"/>  

- Analista de Dados: 35.4%  
- Engenheiro de Dados: 16.9%  
- Ciêntista de Dados: 13.0%  
- Estatístico: 0.4%  
- Data Product Manager: 1.5%  
- outros: 32.8%  

**11- Área de Formação**

- Moda: Computação/TI/ Engenharia de software(2115)

<img src=https://github.com/user-attachments/assets/7df55226-0cfb-41c0-bea9-3fcff29d37c9 width="600"/>  

- Computação/TI/ Engenharia de software: 40.9%  
- Economia: 15.4%  
- Estatística: 7.1%  
- Marketing: 2.5%  
- Ciências Biológicas: 2.2%  
- Ciências Sociais: 1.5%  
- outros: 30.3%  

Gráficos com 2 variáveis:   
- Área de Formação / Faixa Salarial   
<img src=https://github.com/user-attachments/assets/1b401f80-f989-4034-88d3-498519ba16d1 width="600"/>  

- Idade / Gênero
<img src="https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo7-2025-1/blob/main/docs/imagens/AgeGender.png?raw=true" width="600">  

- Nível de experiência / Cargo atual
<img src="https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo7-2025-1/blob/main/docs/imagens/Graph Experience level by current position.png?raw=true" width="600">

- Faixa Etária / Nível na Empresa
<img src=https://github.com/user-attachments/assets/75502139-1ac6-42b6-b2a5-89d8c36346ba width="600">

- Nível na Empresa / Salário
<img src="https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo7-2025-1/blob/main/docs/imagens/Gr%C3%A1fico.png" width="600">

- Área de formação Cientistas de Dados
<img src="https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo7-densidade-demografica/blob/main/docs/imagens/Gr%C3%A1fico%2002.png" width="850">

- **Gráfico base auxiliar**      
<img src=https://github.com/user-attachments/assets/08a5812f-1697-481a-add7-38c93b236c07 width="600">     
 
Curso de Ciência de Dados por Estado (código)       
- SP - 1521433; 1536760; 1538622; 1543013; 1545554; 1589553; 1599656; 1603036; 1618685; (9)    
- MG - 1600504; (1)    
- CE - 1127861; 1571410 (2)   
- PB - 1550460; (1)    

## Preparação dos dados
Primeiramente, foi utilizada a base principal obtida no Kaggle. Nela, selecionamos manualmente os atributos considerados relevantes para o tema do trabalho, que é a densidade demográfica de cientistas de dados. Na tabela abaixo, justificamos os motivos pelos quais esses atributos foram escolhidos.

Em seguida, encontramos uma base auxiliar do INEP que informava quais regiões possuem faculdades com o curso de Ciência de Dados. Essa base incluía dados como latitude, longitude, código do curso, nome do curso (co_cine_rotulo), grau acadêmico, modalidade de ensino, presença de material tátil, recursos de comunicação, recursos de informática, entre outros. Dentre esses, os atributos que nos interessavam eram: código do curso, latitude, longitude, nome do curso, co_cine_rotulo, grau acadêmico e nível acadêmico. A justificativa para a escolha desses atributos, com exceção da latitude e longitude, está descrita na tabela abaixo.

Quanto à latitude e longitude, com o auxílio do ChatGPT, foi possível converter essas coordenadas em Unidades da Federação (UF), permitindo assim a associação desses dados à base principal.

Além disso, a base auxiliar apresentava códigos de cursos repetidos, uma vez que abrangia dados de diferentes anos. Esses códigos duplicados foram removidos manualmente para manter apenas entradas únicas.

Por fim, utilizamos a base auxiliar para criar um novo atributo na base principal: quantidade de cursos no estado de residência. Com a ajuda do ChatGPT, comparamos a UF informada no registro da pessoa com a quantidade de cursos disponíveis na mesma UF (informação proveniente da base auxiliar). Dessa forma, foi possível preencher esse novo atributo com base na localização geográfica do participante.


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

### Modelo 1: Regra de Associação   

- **Perguntada Orientada a Dados:** Existem regiões específicas onde certos atributos demográficos como Faixa Etária e Faixa Salarial são mais comuns entre os Cientistas de Dados?       
- **Justificativa da escolha do modelo:**               
Utilizamos o modelo de Associação com algoritmo Apriori para identificar regras de correlação nos dados de densidade demográfica. Essa escolha é excelente para descobrir padrões frequentes e relações entre atributos, como região, renda e faixa de idade, especialmente quando o objetivo é entender combinações comuns ou interessantes nesses atributos. Neste caso, buscamos associações de regiões que possuem Cientistas de Dados e possíveis padrões em relação a Faixa Etária e a Faixa Salarial, com o objetivo de  entender melhor como esses profissionais estão distribuídos pelo país, considerando diferentes grupos de idade e níveis de renda. Isso permite identificar padrões, como onde há mais profissionais, quais regiões têm maior concentração de jovens ou de profissionais mais experientes, e como a remuneração varia de acordo com a localização e a idade. Essa análise ajuda a criar estratégias mais eficientes para o mercado de trabalho, educação e políticas públicas voltadas para a área. 

- **Processo de amostragem de dados:**               
Foi dividido o dataset em conjuntos de treino e teste usando a função
`train_test_split` do scikit-learn, com uma proporção de 70% para treino e 30% para teste `(test_size=0.3)`. 
Essa divisão ajuda a validar o modelo, garantindo que as regras geradas não sejam apenas específicas do conjunto de treinamento, mas também se mantenham no conjunto de teste, promovendo uma avaliação mais confiável.

- **Parâmetros utilizados:**            
Para o algoritmo Apriori, foi definido
`min_support=0.07`, ou seja, as regras devem aparecer em pelo menos 7% dos registros para serem consideradas frequentes.
Para gerar as regras de associação, utilizou-se `confidence=0.7`, o que significa que as regras só são consideradas se tiverem uma confiança de pelo menos 70%.

- **Exemplo de saida:**    
- antecedents: item ou conjunto de itens que aparecem antes na regra.
- consequents: item ou conjunto de itens que aparecem após na regra.
- support: proporção de registros que contêm ambos os itens.
- confidence: probabilidade de o consequente ocorrer dado o antecedente. 
- lift: indica quanto a regra é mais provável de ocorrer do que se fosse uma ocorrência independente.

Trechos do código comentados:

# Divisão do dataset em treino e teste
`train_df`, `test_df = train_test_split(df_demografico, test_size=0.3, random_state=42)`       
- Aqui, garantimos que 70% dos dados vão para treino e 30% para teste, com uma semente fixa para reprodutibilidade. 
# Função para processar regras de associação
def processar_regras(df_dados):         
    `dataset = df_dados.drop('Região', axis=1).values.tolist()`  # Remove a coluna Região para focar nos atributos         
    `te = TransactionEncoder()`  # Cria o encoder para transformar os dados em formato binário           
    `te_ary = te.fit(dataset).transform(dataset)`  # Aplica o encoder           
    `df_transformed = pd.DataFrame(te_ary, columns=te.columns_)`  # Cria DataFrame com os atributos binários           
    `frequent_itemsets = apriori(df_transformed, min_support=0.4, use_colnames=True)`  # Encontra conjuntos frequentes          
    `regras = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)`  # Gera regras com confiança >= 70%       
    `return regras`     
- **Fluxo de processamento gráfico:**         
Foi criado um diagrama simples que mostra as etapas do processo, desde o carregamento dos dados até a visualização dos resultados. Essa visualização ajuda a entender o fluxo de trabalho de forma clara e intuitiva (Carregar Dados, Dividir em Treino e Teste, Processar Regras com Apriori, Visualizar Resultados).

- **Gráfico informativo:**   
Para finalizar é gerado um gráfico de barras empilhadas, o qual fornece uma visão clara da distribuição demográfica, facilitando a identificação de regiões com maior ou menor concentração de profissionais em diferentes faixas.   

### Modelo 2: Transformação de dados

- **Perguntada Orientada a Dados:** Qual a densidade demográfica de cientistas de dados pelo Brasil?
Em qual região existem profissionais mais qualificados? (junior, pleno, senior)      
- **Justificativa da escolha do modelo:**  
Utilizamos um modelo de transformação de dados baseado em agregações, filtragens e enriquecimento de dados externos (população por estado via IBGE) para responder às perguntas sobre densidade demográfica e qualificação de Cientistas de Dados no Brasil. Essa abordagem é especialmente apropriada quando o objetivo é consolidar informações dispersas em um formato analítico estruturado, possibilitando comparações entre regiões e faixas de perfil profissional. Por exemplo, partimos de uma base que continha cargos, estados e percepções de senioridade, mas esses dados brutos não indicavam diretamente onde havia maior densidade ou qualificação de profissionais. Assim, aplicamos transformações como: Filtragem condicional para isolar profissionais que se identificam ou atuam como Cientistas de Dados; Classificação por senioridade percebida para separar grupos “qualificados” (pleno/sênior) dos demais; Junção com dados populacionais externos para calcular uma métrica de densidade (número de Cientistas de Dados por 100 mil habitantes), padronizando comparações entre estados de tamanhos distintos; Agregações por estado e cálculo de proporções qualificadas para derivar insights sobre a distribuição e experiência desses profissionais.

- **Processo de amostragem de dados:**
Embora o modelo utilizado não seja de aprendizado supervisionado, aplicamos um processo de amostragem filtrada e particionamento lógico com os seguintes objetivos:
	1 Filtragem Semântica:

	- Isolamos apenas os registros em que o participante se identifica como “Cientista de Dados” ou atua dessa forma.

	- Isso garante que a amostra seja coerente com o objetivo da análise: estudar a densidade e qualificação de Cientistas de Dados no Brasil.
   
	2 Particionamento por Estado e Senioridade:
	- Após o filtro, os dados foram particionados por estado de residência e por percepção de senioridade, permitindo cálculos agregados regionais.

	3 Validação por Amostragem Mínima (quasi cross-validation):
  	- Estados com menos de 5 registros foram excluídos da análise percentual de qualificação, para evitar vieses por amostra pequena — uma forma de validação implícita.
 
- **Parâmetros Utilizados:**
| Parâmetro              | Valor/Condição                                                                        |  Justificativa  |

| Parâmetro              | Valor e Condição                                                                        |  Justificativa  |
|-----------------------|--------------------------------------------------------------------------------|----------------|
| `Filtro por cargo/atuação` | str.contains("cientista de dados")   |  Garante foco em profissionais relevantes |
| `Senioridade considerada`  | "0.0" (pleno/sênior), "1.0" (júnior/iniciante)        | Baseado na codificação da base original |
| `Amostra mínima por estado`| ≥ 5 registros            | Para confiabilidade estatística |
| `População externa (IBGE)` | População por estado (2023)               | 	Necessária para cálculo de densidade demográfica |
| `Métrica de densidade`    | # profissionais / população * 100.000       | Padronização entre estados com populações diferentes |

- **Trechos de Código Comentados:**
# 1. Filtro para selecionar apenas cientistas de dados
mask_cientistas = df["cargo_atual"].str.contains("cientista de dados", case=False, na=False) | \
df["atuacao_percebida"].str.contains("cientista de dados", case=False, na=False)
df_cientistas = df[mask_cientistas]
	- Isola os profissionais que efetivamente atuam como Cientistas de Dados.

# 2. Agrupamento por estado
cientistas_por_estado = df_cientistas["estado"].value_counts()
	- Conta quantos profissionais atuam em cada estado.

# 3. Agrupamento por senioridade (pleno/sênior vs. júnior)
df_senioridade = df_cientistas[df_cientistas["senioridade_percebida"].notna()]
senioridade_por_estado = df_senioridade.groupby(["estado", "senioridade_percebida"]).size().unstack(fill_value=0)
	- Cria uma matriz com estados e contagem por tipo de senioridade.

# 4. Cálculo da densidade proporcional à população
df_densidade = cientistas_por_estado.to_frame(name="Qtd Cientistas").join(pd.Series(populacao_estimada, name="População"))
df_densidade["Densidade por 100 mil hab"] = (df_densidade["Qtd Cientistas"] / df_densidade["População"]) * 100_000
	- Normaliza a contagem de profissionais pela população, possibilitando comparação justa entre estados.
### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


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

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




