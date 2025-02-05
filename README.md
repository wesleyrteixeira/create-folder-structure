# 📌 Automação para Gerenciamento de Pastas e Arquivos no "Documentos"

Este repositório contém três scripts Python para gerenciar a criação e remoção de pastas e arquivos dentro do diretório **"Documentos"**.

## 📂 Estrutura dos Scripts
1. **`criar_pastas.py`** → Cria a estrutura de pastas "2025" dentro de todas as subpastas do diretório principal.
2. **`remover_pastas.py`** → Remove completamente a pasta "2025" e todo o seu conteúdo dentro das subpastas do diretório principal.
3. **`remover_arquivo_2025.py`** → Apaga um arquivo específico **apenas dentro da pasta "2025"** (não afeta arquivos dentro das subpastas "Contabilidade", "Financeiro" e "Fiscal").

---

## 📜 Scripts

### 1️⃣ Criar a estrutura de pastas `2025`
**Arquivo:** `criar_pastas.py`  
**Descrição:** Cria a pasta **"2025"** dentro de cada subpasta do diretório principal. Dentro dela, cria pastas de meses e subpastas organizadas.

📌 **Estrutura criada pelo script:**

📂 Documentos 
├── 📂 EMPREENDIMENTO 
│ ├── 📂 2025 
│ │ ├── 📂 01 - Janeiro 
│ │ │ ├── 📂 Contabilidade 
│ │ │ ├── 📂 Financeiro 
│ │ │ ├── 📂 Fiscal 
│ │ ├── 📂 02 - Fevereiro 
│ │ │ ├── 📂 Contabilidade 
│ │ │ ├── 📂 Financeiro 
│ │ │ ├── 📂 Fiscal 
│ │ ├── 📂 03 - Março
│ │ │ ├── 📂 Contabilidade 
│ │ │ ├── 📂 Financeiro 
│ │ │ ├── 📂 Fiscal  
│ │ ├── 📂 ... (até Dezembro) 

✅ **Como executar:**
```sh
python criar_pastas.py

2️⃣ Remover a pasta 2025
Arquivo: remover_pastas.py
Descrição: Remove completamente a pasta "2025" e todo o seu conteúdo dentro de cada subpasta do diretório principal.
⚠️ Atenção: Essa ação é irreversível. Verifique antes de executar.
✅ Como executar:
python remover_pastas.py

3️⃣ Remover um arquivo específico dentro da pasta 2025
Arquivo: remover_arquivo_2025.py
Descrição: Apaga um arquivo específico dentro da pasta "2025", sem afetar arquivos nas subpastas.

📌 O que ele faz:

Verifica todas as subpastas dentro de "PRESTAÇÃO DE CONTAS BACKOFFICE - Documentos".
Se encontrar a pasta "2025", verifica se o arquivo "X" está nela.
Se o arquivo existir, ele será excluído.
⚠️ Esse script não remove arquivos dentro das subpastas "Contabilidade", "Financeiro" e "Fiscal".

✅ Como executar:
python remover_arquivo_2025.py

---
🛠 Requisitos
Python 3.x
Permissões de escrita no diretório alvo
Biblioteca padrão do Python (os, shutil)

📌 Observações
Certifique-se de atualizar os caminhos dos diretórios no código conforme sua estrutura real.
Se precisar de confirmação antes de excluir arquivos, os scripts podem ser ajustados.