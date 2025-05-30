# **Resultados obtidos com o modelo 2**    
- Visualização da matriz de confusão (treino)     
![image](https://github.com/user-attachments/assets/a5b34a80-7aea-4e6c-9c6a-b28a908a92c9)  
Treino: 0.7041 -> O modelo acerta aproximadamente 70.4%.     

- Visualização da matriz de confusão (teste)    
![image](https://github.com/user-attachments/assets/f98e1406-5ac5-4569-b22f-7523051cd9a3)   
Teste: 0.6712 -> O modelo acerta aproximadamente 67.1%.     

# **Precisão treino**       

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.80      | 0.62   | 0.70     | 591     |
| Pleno   | 0.60      | 0.69   | 0.64     | 801     |
| Sênior  | 0.76      | 0.79   | 0.77     | 788     |    

**Acurácia geral:** 0.70 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.72      | 0.70   | 0.71     | 2180    |
| Weighted Avg| 0.71      | 0.70   | 0.71     | 2180    |

# **Precisão teste**  

| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Júnior  | 0.75      | 0.60   | 0.67     | 171     |
| Pleno   | 0.58      | 0.64   | 0.61     | 280     |
| Sênior  | 0.73      | 0.75   | 0.74     | 276     |  

**Acurácia geral:** 0.67 

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Macro Avg   | 0.69      | 0.66   | 0.67     | 727     |
| Weighted Avg| 0.68      | 0.66   | 0.67     | 727     | 

# **Random Forest Finalizada**    
![download](https://github.com/user-attachments/assets/d465ef4f-0032-43c9-951d-6b78dc1b915a)    

- O modelo de teste apresentou uma queda na Acurácia, principalmente devido a classe Pleno.  
