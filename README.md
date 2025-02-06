# 📌 Automation for Managing Folders and Files in "Documents" | Automação para Gerenciamento de Pastas e Arquivos no "Documentos"

This repository contains three Python scripts to manage the creation and removal of folders and files within the **"Documents"** directory.  
Este repositório contém três scripts Python para gerenciar a criação e remoção de pastas e arquivos dentro do diretório **"Documentos"**.

---

## 📂 Scripts Structure | Estrutura dos Scripts
1. **`criar_pastas.py`** → Creates the "2025" folder structure inside all subdirectories of the main directory.  
   **Cria a estrutura de pastas "2025" dentro de todas as subpastas do diretório principal.**

2. **`remover_pastas.py`** → Completely removes the "2025" folder and all its contents within the subdirectories of the main directory.  
   **Remove completamente a pasta "2025" e todo o seu conteúdo dentro das subpastas do diretório principal.**

3. **`remover_arquivo_2025.py`** → Deletes a specific file **only inside the "2025" folder** (does not affect files inside the "Contabilidade", "Financeiro", and "Fiscal" subfolders).  
   **Apaga um arquivo específico **apenas dentro da pasta "2025"** (não afeta arquivos dentro das subpastas "Contabilidade", "Financeiro" e "Fiscal").**

---

## 📜 Scripts

### 1️⃣ Create the `2025` Folder Structure | Criar a estrutura de pastas `2025`
**File | Arquivo:** `criar_pastas.py`  
**Description | Descrição:**  
Creates the **"2025"** folder inside each subdirectory of the main directory. Inside it, creates month folders and organized subfolders.  
**Cria a pasta "2025" dentro de cada subpasta do diretório principal. Dentro dela, cria pastas de meses e subpastas organizadas.**

📌 **Structure created by the script | Estrutura criada pelo script:**
📂 Documents 
| Documentos 
├── 📂 ENTERPRISE | EMPREENDIMENTO │ 
├── 📂 2025 
│ │ ├── 📂 01 - January | Janeiro 
│ │ │ ├── 📂 Accounting | Contabilidade 
│ │ │ ├── 📂 Finance | Financeiro 
│ │ │ ├── 📂 Tax | Fiscal 
│ │ ├── 📂 02 - February | Fevereiro 
│ │ │ ├── 📂 Accounting | Contabilidade 
│ │ │ ├── 📂 Finance | Financeiro 
│ │ │ ├── 📂 Tax | Fiscal 
│ │ ├── 📂 03 - March | Março 
│ │ │ ├── 📂 Accounting | Contabilidade 
│ │ │ ├── 📂 Finance | Financeiro 
│ │ │ ├── 📂 Tax | Fiscal 
│ │ ├── 📂 ... (up to December | até Dezembro)

✅ **How to run | Como executar:**
```sh
python criar_pastas.py

### 2️⃣ Remove the 2025 Folder | Remover a pasta 2025
**File | Arquivo:** remover_pastas.py
**Description | Descrição:**
Completely removes the "2025" folder and all its contents within each subdirectory of the main directory.
**Remove completamente a pasta "2025" e todo o seu conteúdo dentro de cada subpasta do diretório principal.**

⚠️ Warning | Atenção: This action is irreversible. Double-check before running.
Essa ação é irreversível. Verifique antes de executar.

✅ How to run | Como executar:
python remover_pastas.py

3️⃣ Remove a Specific File Inside 2025 | Remover um arquivo específico dentro da pasta 2025
File | Arquivo: remover_arquivo_2025.py
Description | Descrição:
Deletes a specific file inside the "2025" folder, without affecting files in subfolders.
Apaga um arquivo específico dentro da pasta "2025", sem afetar arquivos nas subpastas.

📌 What it does | O que ele faz:

Checks all subdirectories inside "Documents".
Verifica todas as subpastas dentro de "Documentos".
If it finds the "2025" folder, it checks if the file "X" is there.
Se encontrar a pasta "2025", verifica se o arquivo "X" está nela.
If the file exists, it will be deleted.
Se o arquivo existir, ele será excluído.
⚠️ This script does not remove files inside the "Contabilidade", "Financeiro", and "Fiscal" subfolders.
Esse script não remove arquivos dentro das subpastas "Contabilidade", "Financeiro" e "Fiscal".

✅ How to run | Como executar:
python remover_arquivo_2025.py

🛠 Requirements | Requisitos
Python 3.x
Write permissions in the target directory
Permissões de escrita no diretório alvo
Python standard libraries (os, shutil)
Biblioteca padrão do Python (os, shutil)

📌 Notes | Observações
Make sure to update the directory paths in the code according to your real structure.
Certifique-se de atualizar os caminhos dos diretórios no código conforme sua estrutura real.
If you need confirmation before deleting files, the scripts can be adjusted.
Se precisar de confirmação antes de excluir arquivos, os scripts podem ser ajustados.

🚀 If you need adjustments or new features, contribute or get in touch! 😊
Caso precise de ajustes ou novas funcionalidades, contribua ou entre em contato! 😊
