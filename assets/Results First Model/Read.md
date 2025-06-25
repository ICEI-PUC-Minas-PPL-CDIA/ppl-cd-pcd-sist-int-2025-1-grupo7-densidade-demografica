# **Resultados Modelo 1**   

- Visualização da matriz de confusão (treino)   
![image](https://github.com/user-attachments/assets/19165905-7c22-4256-8f58-4870b81af568)     
Treino: 0.7289 -> O modelo acerta aproximadamente 72.9%.     

| Código | Classe  |
|--------|---------|
| 0      | Júnior  |
| 1      | Pleno   |
| 2      | Sênior  |

- A imagem é uma matriz de confusão de teste utilizada para classificar o nível de desempenho das classes no modelo. Cada linha representa a classe real dos dados e as colunas a classe prevista.

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/92b60300-a7db-464b-a9c2-ffe6d4362a0f)       
Teste: 0.6795 -> O modelo acerta aproximadamente 67.9%.    

| Código | Classe  |
|--------|---------|
| 0      | Júnior  |
| 1      | Pleno   |
| 2      | Sênior  |

- A imagem é uma matriz de confusão de teste utilizada para classificar o nível de desempenho das classes no modelo a partir de previsões corretas ou incorretas. Cada linha representa a classe real dos dados e as colunas a classe prevista.

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
![image](https://github.com/user-attachments/assets/fe27267f-7f46-4489-9f3b-54c0106096b2)   


