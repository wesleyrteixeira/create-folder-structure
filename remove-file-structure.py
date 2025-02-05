import os

base_dir = r"C:"  # Insira o caminho do diretório principal

# Nome do arquivo que será removido
arquivo_alvo = "Contabilidade"

# Percorre todas as subpastas dentro do diretório principal
for subpasta in os.listdir(base_dir):
    subpasta_path = os.path.join(base_dir, subpasta)
    pasta_2025 = os.path.join(subpasta_path, "2024")

    # Verifica se a pasta "2025" existe dentro da subpasta
    if os.path.isdir(pasta_2025):
        # Lista apenas arquivos diretamente dentro da pasta "2025"
        for file in os.listdir(pasta_2025):
            file_path = os.path.join(pasta_2025, file)
            
            # Verifica se é um arquivo e se corresponde ao alvo
            if os.path.isfile(file_path) and file == arquivo_alvo:
                os.remove(file_path)
                print(f"❌ Arquivo removido: {file_path}")

print("\n✅ Todos os arquivos 'Contabilidade' foram removidos apenas das pastas '2024'!")
