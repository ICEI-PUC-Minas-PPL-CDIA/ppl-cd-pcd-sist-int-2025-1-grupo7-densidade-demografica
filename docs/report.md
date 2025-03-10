# Análise de transferência de emprego por enforcamento do trabalho presencial na área de ciencia de dados


**Ian Vinicius Marinho Malta, ian.malta@sga.pucminas.br**

**João Gabriel de Melo Neves, jgmneves@sga.pucminas.br**

**Beatriz Azevedo dos Santos, beatriz.santos.1595043@sga.pucminas.br**

**Thales Ribeiro Melo, thales.melo@sga.pucminas.br**

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

Nos últimos anos, especialmente com a pandemia de 2020, a dinâmica do trabalho passou e continua passando por mudanças significativas. Devido à necessidade de isolamento social, muitas empresas adotaram o trabalho remoto como solução. No entanto, com o retorno à normalidade, surge o questionamento: é mais vantajoso para as organizações manter o trabalho remoto ou voltar completamente ao modelo presencial? 

###    Contextualização

Após o periodo da pandemia de 2020, muitas empresas tem duvidas se o trabalho remoto ainda é vantajoso para elas ou se elas devem voltar 100% presencial.

###    Problema

Possível grande número de saída de funcionários por causa da mudança do modo de trabalho remoto/híbrido para 100% presencial.


> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)


###    Objetivo geral

O objetivo desse projeto é analisar uma serie de dados relacionados aos funcionarios de uma empresa para obter os pros e contras de mudar o sistema de trabalho dos funcionarios de trabalho remoto para o presencial.
####    Objetivos específicos

- Analisar os dados e por meio deles obter os benefícios de fazer os funcionários voltarem a trabalhar 100% presencialmente com a intenção de se obter maior lucro, sendo esses dados calculados pela produtividade individual e em grupo

- Analisar os dados e por meio deles obter as desvantagens de realizar essa mudança como a mudança de certos funcionários para outros trabalhos pela distancia ou só pela falta desse beneficio e o custo do passe transporrte

> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)


###    Justificativas

Mostre também as **justificativas** para o  desenvolvimento do seu trabalho e, caso deseje, 
destaque alguma contribuição do trabalho.

A justific ativa deve descrever a importância ou a motivação para o desenvolvimento do 
sistema inteligente escolhido. Indique as razões pelas quais você escolheu seus objetivos 
específicos ou as razões para aprofundar em certos aspectos do software.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)



##    Público alvo
Os CEOS e chefes de empresas que possuam departamento de informática e desejam misturar home office com trabalho presencial ou queiram optar apenas por um dos dois. 

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)


## Análise exploratórida dos dados

###    Dicionário de dados

Apresente uma descrição das bases de dados a serem utilizadas. 
Dicionários de dados devem conter as bases de dados, os nomes dos atributos 
com seu significado, seu tipo (inteiro, real, textual, categórico, etc).

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




