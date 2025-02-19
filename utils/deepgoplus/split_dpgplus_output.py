deepgoplus_output = "utils\deepgoplus\deepgoplus_output_example.tsv"

# Abrir o arquivo para leitura
dicionario = {}

with open(deepgoplus_output, 'r') as file:
    for line in file:
        
        # Dividir a linha em colunas usando espaço ou outro delimitador
        partes = line.strip().split()
        
        ## o item da primeira coluna é a chave do dicionário. Os itens das demais colunas são os valores.
        if partes:
            dicionario[partes[0]] = partes[1:]

count = 0
for protein, gos_scores in dicionario.items():
    for go_score in gos_scores:
        if "|" in go_score:
            go_id, score = go_score.split("|", 1)
            print(protein, score, go_id, sep="\t")
            count += 1

print("Number of lines ", count)