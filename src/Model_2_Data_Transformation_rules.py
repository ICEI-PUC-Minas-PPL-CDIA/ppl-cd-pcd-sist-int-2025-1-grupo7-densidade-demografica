
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('State_of_data_BR_2023_Kaggle - df_survey_2023 (1).csv')


df = df.rename(columns={
    "('P1_i ', 'Estado onde mora')": "estado",
    "('P2_f ', 'Cargo Atual')": "cargo_atual",
    "('P1_f_2', 'Senioridade das vagas recebidas em relação à sua experiência')": "senioridade_percebida",
    "('P4_a ', 'Mesmo que esse não seja seu cargo formal, você considera que sua atuação no dia a dia, reflete alguma das opções listadas abaixo?')": "atuacao_percebida"
})

mask_cientistas = df["cargo_atual"].str.contains("cientista de dados", case=False, na=False) | \
                  df["atuacao_percebida"].str.contains("cientista de dados", case=False, na=False)

df_cientistas = df[mask_cientistas]

cientistas_por_estado = df_cientistas["estado"].value_counts().sort_values(ascending=False)

df_senioridade = df_cientistas[df_cientistas["senioridade_percebida"].notna()]

senioridade_por_estado = df_senioridade.groupby(["estado", "senioridade_percebida"]).size().unstack(fill_value=0)
senioridade_por_estado.columns = ["Qualificados (0.0)", "Não Qualificados (1.0)"]
senioridade_por_estado["% Qualificados"] = senioridade_por_estado["Qualificados (0.0)"] / (
    senioridade_por_estado["Qualificados (0.0)"] + senioridade_por_estado["Não Qualificados (1.0)"]
)

populacao_estimada = {
    'São Paulo (SP)': 46700000,
    'Minas Gerais (MG)': 21170000,
    'Rio de Janeiro (RJ)': 17150000,
    'Bahia (BA)': 14930000,
    'Paraná (PR)': 11520000,
    'Rio Grande do Sul (RS)': 11330000,
    'Pernambuco (PE)': 9675000,
    'Ceará (CE)': 9241000,
    'Pará (PA)': 8777000,
    'Santa Catarina (SC)': 7656000,
    'Goiás (GO)': 7196000,
    'Maranhão (MA)': 7037000,
    'Paraíba (PB)': 4039000,
    'Amazonas (AM)': 3962000,
    'Espírito Santo (ES)': 4019000,
    'Mato Grosso (MT)': 3567000,
    'Rio Grande do Norte (RN)': 3561000,
    'Piauí (PI)': 3273000,
    'Alagoas (AL)': 3322000,
    'Distrito Federal (DF)': 3055000,
    'Mato Grosso do Sul (MS)': 2839000,
    'Sergipe (SE)': 2328000,
    'Rondônia (RO)': 1803000,
    'Tocantins (TO)': 1620000,
    'Acre (AC)': 830000,
    'Amapá (AP)': 877000,
    'Roraima (RR)': 636000
}

df_densidade = cientistas_por_estado.to_frame(name="Qtd Cientistas").join(pd.Series(populacao_estimada, name="População"))
df_densidade["Densidade por 100 mil hab"] = (df_densidade["Qtd Cientistas"] / df_densidade["População"]) * 100_000

df_densidade.to_csv("densidade_cientistas_dados_estados.csv")
senioridade_por_estado.to_csv("qualificacao_cientistas_estados.csv")

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
cientistas_por_estado.head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Estados com Mais Cientistas de Dados (Total Absoluto)")
plt.ylabel("Quantidade de Cientistas de Dados")
plt.xlabel("Estado")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_qualificados = senioridade_por_estado[senioridade_por_estado["Qualificados (0.0)"] + senioridade_por_estado["Não Qualificados (1.0)"] >= 5]
plt.figure(figsize=(12, 6))
sns.barplot(data=top_qualificados.reset_index(), x="estado", y="% Qualificados", palette="viridis")
plt.title("Percentual de Profissionais Qualificados por Estado (Amostras ≥ 5)")
plt.ylabel("Percentual de Qualificados")
plt.xlabel("Estado")
plt.ylim(0, 1.1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
