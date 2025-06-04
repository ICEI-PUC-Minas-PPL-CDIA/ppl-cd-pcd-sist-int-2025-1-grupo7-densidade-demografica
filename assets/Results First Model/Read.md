# **Resultados Modelo 1**   

- Visualização da matriz de confusão (treino)     
![image](https://github.com/user-attachments/assets/f19ac1fc-0185-4ab2-b81e-66386512d32b)   
Treino: 0.7069 -> O modelo acerta aproximadamente 70.7%.     

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/65fad542-c615-48e4-9a7f-afba329395a5)    
Teste: 0.6781 -> O modelo acerta aproximadamente 67.8%.    

# **Precisão treino**       

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.71      | 0.78   | 0.74     | 591     |
| Pleno   | 0.61      | 0.64   | 0.63     | 801     |
| Sênior  | 0.81      | 0.72   | 0.76     | 788     |    

**Acurácia geral:** 0.71

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.71      | 0.71   | 0.71     | 2180    |
| Weighted Avg| 0.71      | 0.71   | 0.71     | 2180    |

# **Precisão teste**  

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.66      | 0.82   | 0.73     | 171     |
| Pleno   | 0.60      | 0.60   | 0.60     | 280     |
| Sênior  | 0.78      | 0.67   | 0.72     | 276     |  

**Acurácia geral:** 0.68
|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.68      | 0.70   | 0.68     | 727     |
| Weighted Avg| 0.69      | 0.68   | 0.68     | 727     |    

- O modelo de teste apresentou uma queda na Acurácia, principalmente devido a classe Pleno.

# **Árvore de decisão finalizada**    
![image](https://github.com/user-attachments/assets/9eb8cefa-9846-41b0-827b-67c7d6c287be)

