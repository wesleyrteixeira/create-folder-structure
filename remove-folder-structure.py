import os
import shutil

base_dir = r"C:"  # Insira o caminho do diretório principal

# Nome da pasta que será removida
pasta_alvo = "2025"

# Percorre todas as subpastas dentro do diretório principal
for subpasta in os.listdir(base_dir):
    subpasta_path = os.path.join(base_dir, subpasta)
    pasta_2025 = os.path.join(subpasta_path, pasta_alvo)

    # Verifica se a pasta "2025" existe dentro da subpasta
    if os.path.isdir(pasta_2025):
        shutil.rmtree(pasta_2025)  # Remove a pasta e todo o seu conteúdo
        print(f"❌ Pasta removida: {pasta_2025}")
    else:
        print(f"⚠️ Pasta não encontrada: {pasta_2025}")

print("\n✅ Todas as pastas '2025' foram removidas com sucesso!")
