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


Com o aumento da competição por forca de trabalho vem se vendo uma maior dificuldade para a obtenção de trabalhadores qualificados, em que as empresas tentam entrar em certo local para começar mas sem a quantidade necessária ocorrem diversos problemas e a empresa perde possiveis lucros.

###    Problema


Um problema que pode apresentar-se ao criar uma empresa que necessita de cientistas de dados é a falta de profissionais qualificados. Uma empresa sem esses profissionais pode perder muito de seu lucro por falta de pesquisas que avaliem como a empresa deve agir. 

> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)


###    Objetivo geral

Desenvolver um sistema inteligente para mostrar geograficamente a densidade de cientistas de dados por municipio e indicar quais municipios estão saturados para que empresas tenham uma maior facilidade de contratar cientistas de dados ao abrirem suas empresas.

####    Objetivos específicos

- Analisar os dados e por meio deles obter informações sobre a demanda do curso Ciência de dados nos estados do Brasil, sendo esse importante para o planejamento do local em que as novas empresas dessa área serão melhor alocadas.

- Analisar os dados e por meio deles obter informações sobre o número de faculdades que atendem a Ciência de Dados nos estados do Brasil, de tal forma a ser importante para a implementação de tal nas regiões que ainda não se efetivou o curso em suas faculdades.

> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)


###    Justificativas  

A crescente demanda por profissionais de Ciência de Dados tem impulsionado empresas a buscarem maneiras mais eficientes de localizar esses especialistas e compreender suas qualificações. Entretanto, a falta de informações geográficas consolidadas sobre a distribuição desses profissionais dificulta o planejamento estratégico das organizações que desejam contratar ou expandir suas operações.  

Diante desse cenário, este projeto se justifica pela necessidade de um sistema inteligente que permita visualizar a densidade de cientistas de dados por município, identificando regiões com maior ou menor oferta desses profissionais. Além disso, compreender a relação entre a presença de cursos de Ciência de Dados e a disponibilidade de especialistas qualificados pode auxiliar tanto na alocação de empresas quanto no incentivo à criação de novos cursos em regiões menos atendidas.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)



##    Público alvo
Os CEOS e chefes de empresas novas na área de Ciencia de Dados, de tal forma a auxiliar essas novas empresas a iniciarem sua trajetória procurando profissionais qualificados e um município propenso para tal atividade.
> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)


## Análise exploratórida dos dados

###    Dicionário de dados

| Data                                                                                                                      | Description                                                                                   | Data Type                                             |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Id                                                                                                                        | O numerio da identidade de cada pessoa que respondeu a pesquisa                               | Dados qualitativos (polinomial não ordinal)           |
| Idade                                                                                                                     | Idade da pessoa que respondeu a pesquisa                                                      | Dados quantitativos discretos                         |
| Faixa idade                                                                                                               | A qual faixa de idade a pessoa pertence, sendo que cada faixa possui 4 anos entre uma e outra | Dados qualitativos ( polinomiais ordinais)            |
| Gênero                                                                                                                    | Gênerio da pessoa que respondeu a pesquisa                                                    | Dados qualitativos (Binomial simetrico)               |
| Cor/raça/etnia                                                                                                            | Cor de pele/raça/etnia da pessoa que respondeu a pesquisa                                     | Dados qualitativos (polinomial não ordinal)           |
| PCD                                                                                                                       | Se a pessoa que respondeu a pesquisa possui alguma deficiência                                | Dados qualitativos (Binomial simetrico)               |
| Vive no Brasil                                                                                                            | Se a pessoa que respondeu a pesquisa mora no Brasil ou não                                    | Dados qualitativos (Binomial assimetrico)             |
| Estado onde mora                                                                                                          | Qual estado nacional a pessoa que respondeu a pesquisa mora                                   | Dados qualitativos (polinomial não ordinal)           |
| UF onde mora                                                                                                              | Sigla do estado de onde a pessoa mora                                                         | Dados qualitativos (polinomial não ordinal)           |
| Região onde Mora                                                                                                          | Qual das 5 regiões do Brasil a pessoa mora. (Norte, Nordeste, Centro-Oeste, Sudeste e Sul)    | Dados qualitativos (polinomial não ordinal)           |
| Nível de Ensino                                                                                                           | Qual o nível de ensino superior da pessoa                                                     | Dados qualitativos (polinomiais ordinais)             |
| Área de Formação                                                                                                          | Qual das areas disponiveis na base de dados a pessoa se formou.                               | Dados qualitativos (polinomiais ordinais)             |
| Qual sua situação atual de trabalho?                                                                                      | Se a pessoa está trabalhando, procurando emprego ou desempregado                              | Dados qualitativos (polinomiais ordinais)             |
| Setor                                                                                                                     | Em qual area do setor trabalhial a pessoa trabalha na empresa.                                | Dados qualitativos ( polinomiais ordinais)            |
| Numero de Funcionários                                                                                                    | Quantos funcionários tem na empresa em que a pessoa trabalha                                  | Dados quantitativos discretos                         |
| Cargo Atual                                                                                                               | Qual o cargo a pessoa trabalha, dentro da area de ciência de dados                            | Dados qualitativos (polinomiais ordinais)             |
| Nível                                                                                                                     | A quanto tempo a pessoa está trabalhando no seu setor                                         | Dados qualitativos ( polinomiais ordinais)            |
| Faixa salarial                                                                                                            | Qual o salário medio mensal da pessoa                                                         | Dados qualitativos (polinomiais ordinais)             |
| Quanto tempo de experiência na área de dados você tem?                                                                    | Quanto tempo a pessoa trabalha na area de ciencia de dados.                                   | Tipos de dados polinomiais ordinais                   |
| Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados? | Quanto tempo a pessoa tem em outras areas que podem ajudar com o manejamento de dados.        | Dados qualitativos (polinomial não ordinal)           |
| Qual o número aproximado de pessoas que atuam com dados na sua empresa hoje?                                              | Número bruto de funcionários que trablham na area de dados na empresa                         | Dados quantitativos discretos                         |
| Cientista de Dados/Data Scientist                                                                                         | Se a pessoa é ou não cientista de dados                                                       | Tipos de dados qualitativos (binominais assimétricos) |

Este projeto deve utilizar pelo menos duas fontes de dados. Uma fonte principal e 
uma fonte para enriquecimentos dos dados principais.


###    Descrição de dados

Utilize a análise descritiva baseada em estatística de primeira ordem para descrever os dados.
Como descrever dados numéricos: média, desvio padrão, mínimo, máximo, quartis, histograma, etc.
Como descrever dados qualitativos (categóricos): moda (valor mais frequente), quantidade de valores distintos (categorias), distribuição das categorias (histograma), etc.


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.


## Indução de modelos

### Modelo 1: Algoritmo

Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


## Resultados

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




