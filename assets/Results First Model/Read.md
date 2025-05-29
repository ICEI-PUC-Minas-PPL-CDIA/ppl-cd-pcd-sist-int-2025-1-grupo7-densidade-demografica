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
