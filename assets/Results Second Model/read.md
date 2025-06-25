# **Resultados obtidos com o modelo 2**    
- Visualização da matriz de confusão (treino)     
![image](https://github.com/user-attachments/assets/8d24d3b9-b520-4d34-815c-019d6c8f0984)   
Treino: 0.9211 -> O modelo acerta aproximadamente 92.1%.     

| Código | Classe  |
|--------|---------|
| 0      | Júnior  |
| 1      | Pleno   |
| 2      | Sênior  |

- A imagem é uma matriz de confusão de teste utilizada para classificar o nível de desempenho das classes no modelo. Cada linha representa a classe real dos dados e as colunas a classe prevista.

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/207b447f-371c-4741-9a57-0f777c19451c)    
Teste: 0.6960 -> O modelo acerta aproximadamente 69.6%.

| Código | Classe  |
|--------|---------|
| 0      | Júnior  |
| 1      | Pleno   |
| 2      | Sênior  |

- A imagem é uma matriz de confusão de teste utilizada para classificar o nível de desempenho das classes no modelo a partir de previsões corretas ou incorretas. Cada linha representa a classe real dos dados e as colunas a classe prevista.

# **Precisão treino**       

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.94      | 0.93   | 0.93     | 591     |
| Pleno   | 0.90      | 0.88   | 0.89     | 801     |
| Sênior  | 0.92      | 0.95   | 0.94     | 788     |    

**Acurácia geral:** 0.92 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.92      | 0.92   | 0.92     | 2180    |
| Weighted Avg| 0.92      | 0.92   | 0.92     | 2180    |

# **Precisão teste**  

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.74      | 0.73   | 0.73     | 171     |
| Pleno   | 0.61      | 0.62   | 0.62     | 280     |
| Sênior  | 0.75      | 0.76   | 0.75     | 276     |  

**Acurácia geral:** 0.70 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.70      | 0.70   | 0.70     | 727     |
| Weighted Avg| 0.70      | 0.70   | 0.70     | 727     | 

# **Random Forest Finalizada**    
![download](https://github.com/user-attachments/assets/3450692c-f66e-4fac-b857-16d45e43d9b9)   

- O modelo de teste apresentou uma queda na Acurácia, principalmente devido a classe Pleno.   
- O modelo possui overfitting.  
