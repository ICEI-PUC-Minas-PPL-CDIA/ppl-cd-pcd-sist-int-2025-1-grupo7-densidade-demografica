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
| CO_CURSO                | Código identificador do curso                              | dados qualitativos polinomiais não ordinais |
| LATITUDE                | Coordenada geográfica de latitude                          | Dados quantitativos contínuos               |
| LONGITUDE               | Coordenada geográfica de longitude                         | Dados quantitativos contínuos               |
| CO_MUNICIPIO            | Código identificador do município                          | Dados quantitativos discretos               |
| NO_CURSO                | Nome do curso                                              | dados qualitativos                          |
| CO_CINE_ROTULO          | Código da classificação do curso no CINE                   | dados qualitativos                          |
| TP_GRAU_ACADEMICO       | Grau acadêmico do curso (Bacharelado, Licenciatura, etc.)  | dados polinomiais ordinais                  |
| TP_MODALIDADE_ENSINO    | Modalidade do curso (Presencial, EAD, etc.)                | dados polinomiais ordinais                  |
| TP_NIVEL_ACADEMICO      | Nível acadêmico do curso (Graduação, Pós-Graduação, etc.)  | dados polinomiais ordinais                  |
| IN_MATERIAL_TATIL       | Indica se há material tátil disponível (Sim/Não)           | dados qualitativos binomiais assimétricos   |
| IN_RECURSOS_COMUNICACAO | Indica se há recursos de comunicação disponíveis (Sim/Não) | dados qualitativos binomiais simétricos     |
| IN_RECURSOS_INFORMATICA | Indica se há recursos de informática disponíveis (Sim/Não) | dados qualitativos binomiais assimétricos   |
| RELAÇÃO                 | Código identificador de relação entre registros            | dados qualitativos                          |

Este projeto deve utilizar pelo menos duas fontes de dados. Uma fonte principal e 
uma fonte para enriquecimentos dos dados principais.


###    Descrição de dados

Dados Quantitativos:
• Gênero 
• Faixa Etária
• Faixa Salarial (média que o usuário recebe por mês)
• Nível de experiência (quantos anos o usuário possui na área)
• Ciêntista por Estado
• Raça/Etnia/Cor

Dados Qualitativos:
• Ciêntistas por Região
• Nível de Ensino (o grau de ensino que os usuários possuem)
• Situação Empresarial (situação atual do usuário diante o mercado de trabalho)
• Cargo (tipo de cargo assumido)
• Área de Formação (em qual curso o usuário se formou)

1- Gênero
Moda: Masculino(3975)
![image](https://github.com/user-attachments/assets/c39e1b22-d724-44a0-8c61-640407b89423)
Masculino: 75.1%
Feminino: 24.4%
preferiu não informar: 0.3%
outros: 0.2%

2- Faixa Etária
Moda: 25-29(1654)
![image](https://github.com/user-attachments/assets/e54e0435-dbd0-4628-abf3-7c577cbf22f7)
17-21: 3.4%
22-24: 9.3%
25-29: 31.3%
30-34: 26%
35-39: 14.9%
40-44: 8.1%
45-49: 3.6%
50-54: 2.1%
mais que 55: 1.4%

3- Faixa Salarial
Moda: 6.001-12.000(1663)
![image](https://github.com/user-attachments/assets/98c6c4c9-0caf-44c5-993a-439508e01cfe)
menos que 1.000: 0.6%
1.001-2.000: 4.5%
2.001-6.000: 29.1%
6.001-12.000: 35%
12.001-16.000: 13.7%
16.001-20.000: 6.9%
mais que 20.001: 10.1%

4- Nível de experiência
Moda: 4 a 6 anos(1300)
![image](https://github.com/user-attachments/assets/ac8ce524-9839-4d83-99d3-df9c399313ac)
menos que 1 ano: 8.2%
1 a 2 anos: 20.8%
3 a 4 anos: 19.2%
4 a 6 anos: 22.5%
mais que 6 anos: 17.1%
não possui experiência: 12.1%

5- Ciêntista por Estado
Moda: São Paulo(SP)(2072)
![image](https://github.com/user-attachments/assets/d38c9611-6938-429f-9be8-64bb357318c3)

![image](https://github.com/user-attachments/assets/f31e79e1-9725-4526-8b99-c7511fb27595)

![image](https://github.com/user-attachments/assets/da214e89-25be-4d53-97d4-b496e306be1c)

6- Raça/Etnia/Cor
Moda: Branca(3414)
![image](https://github.com/user-attachments/assets/a60d2f95-f7e9-4e64-b209-b502443c9f38)
Branca: 64.5%
Parda: 24.2%
Amarela: 2.8%
preta: 7.3%
preferiu não informar: 0.6%
outra: 0.3%

7- Ciêntistas por Região
Moda: Sudeste(3172)
![image](https://github.com/user-attachments/assets/f01648ae-98bb-43b3-a57a-745877ce81f2)
Sudeste: 59.9%
Sul: 18.2%
Nordeste: 11.5%
Centro-Oeste: 6.5%
Norte: 1.6%
Vazio(não identificado): 2.3%

8- Nível de Ensino
Moda: Graduação/Bacharelado(2476)
![image](https://github.com/user-attachments/assets/1ff7373b-598c-43ad-8458-02c76287bf22)
Graduação/Bacharelado: 46.8%
Pós-Graduação: 34.3%
Mestrado: 12.8%
Doutorado: 4%
sem graduação: 2%
outros: 0.1%

9- Situação Empresarial
Moda: Empregado(CLT)(4159)
![image](https://github.com/user-attachments/assets/0c498987-8761-4c03-8225-d7f4f49229ba)
Empregado(CLT): 78.6%
Desempregado: 7%
Estagiário: 3.9%
Estudante: 2%
Servidor Público: 2.8%
outros: 5.7%

10- Cargo
Moda: Analista de dados(em geral)(1858)
![image](https://github.com/user-attachments/assets/ff494eaa-fba2-4706-a4d4-8d507542aa96)
Analista de Dados: 35.8%
Engenheiro de Dados: 14.6%
Ciêntista de Dados: 13.2%
Estatístico: 0.4%
Data Product Manager: 1.9%
outros: 34%

11- Área de Formação
Moda: Computação/TI/ Engenharia de software(2153)
![image](https://github.com/user-attachments/assets/ca57f7f1-46b1-4112-91fe-f055674ae0f5)
Computação/TI/ Engenharia de software: 40.7%
Economia: 15.4%
Estatística: 7.1%
Marketing: 2.5%
Ciências Biológicas: 2.3%
Ciências Sociais: 1.6%
outros: 30.4%



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




