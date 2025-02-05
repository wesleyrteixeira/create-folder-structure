import os

# Caminho base onde as SPEs estão localizadas
base_dir = r"C:\Users\wesley.teixeira\Grupo Trinus Co\PRESTAÇÃO DE CONTAS BACKOFFICE - Documentos"

# Lista de meses e subpastas
meses = [
    "01 - Janeiro", "02 - Fevereiro", "03 - Março", "04 - Abril",
    "05 - Maio", "06 - Junho", "07 - Julho", "08 - Agosto",
    "09 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"
]
subpastas = ["Contabilidade", "Financeiro", "Fiscal"]

# Percorre todas as subpastas dentro do diretório principal
for subpasta in os.listdir(base_dir):
    subpasta_path = os.path.join(base_dir, subpasta)

    # Verifica se é um diretório
    if os.path.isdir(subpasta_path):
        # Criar a pasta 2025 dentro da subpasta
        path_2025 = os.path.join(subpasta_path, "2025")
        os.makedirs(path_2025, exist_ok=True)

        for mes in meses:
            mes_path = os.path.join(path_2025, mes)
            os.makedirs(mes_path, exist_ok=True)

            for sub in subpastas:
                sub_path = os.path.join(mes_path, sub)
                os.makedirs(sub_path, exist_ok=True)

        print(f"✅ Estrutura criada para: {subpasta}")

print("\n🎯 Todas as pastas foram criadas com sucesso!")
