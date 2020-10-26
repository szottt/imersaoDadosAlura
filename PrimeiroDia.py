import pandas as pd

# fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

fonte2 = r"C:\Users\Igor Szot\Documents\Cursos2020\CursoImersaoAluraDados\imersao-dados-2-2020\MICRODADOS_ENEM_2019_SAMPLE_43278.csv"

dados = pd.read_csv(fonte2)

colunas = ['SG_UF_RESIDENCIA', 'Q020'] #listas para pegar varias colunas


# print(dados.head(5)) ## primeiros 5
# print(dados.shape)    ## total
#print(dados['NO_MUNICIPIO_RESIDENCIA'])
# print(dados.columns.values)
# print(dados[colunas])
# print(dados['SG_UF_RESIDENCIA'].unique()) ## Unique usamos para fazer tipo um distinct
#print(len(dados['SG_UF_RESIDENCIA'].unique())) ## len para contar quantos estados
#print(dados['SG_UF_RESIDENCIA'].value_counts()) ## value_counts() para sabermos quantos fizeram o ENEM em cada estado
# print(dados['NU_IDADE'].value_counts()) ## Para descobrir as idades
print(dados['NU_IDADE'].value_counts().sort_index())