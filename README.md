# 🗂️ Organizador Automático de Arquivos

Um script em Python desenvolvido para organizar automaticamente arquivos de uma pasta, classificando-os por categoria (Imagens, Documentos, Planilhas, Vídeos, etc.). Além disso, o sistema registra logs detalhados de cada movimentação, garantindo rastreabilidade e profissionalismo.

## 🚀 Funcionalidades

- 📁 Organização automática por categorias  
- 🧠 Detecção inteligente de extensões  
- 🛡️ Tratamento de erros (arquivo em uso, permissão negada, etc.)  
- 📝 Geração automática de logs diários  
- 🔄 Evita sobrescrever arquivos (cria `_copy` quando necessário)  
- 🧹 Ignora pastas automaticamente  
- ⚙️ Código simples, limpo e fácil de manter  

## 📦 Categorias Suportadas

| Categoria      | Extensões |
|----------------|-----------|
| Imagens        | jpg, jpeg, png, gif, bmp, svg |
| Documentos     | pdf, doc, docx, txt, odt |
| Planilhas      | xls, xlsx, csv |
| Vídeos         | mp4, mov, avi, mkv |
| Áudios         | mp3, wav, aac, ogg |
| Compactados    | zip, rar, 7z |
| Executáveis    | exe, msi |
| Outros         | Qualquer extensão não reconhecida |

## 📝 Logs

O script gera automaticamente um arquivo de log diário no formato:

log_2026-01-04.txt

Cada linha contém:

[15:32:10] Movido: foto.jpg → Imagens
[15:32:10] Permissão negada para mover: arquivo.xlsx

Isso permite auditoria completa de tudo que foi feito.

## ▶️ Como usar

1. Instale o Python 3.8+  
2. Baixe ou clone este repositório:

git clone https://github.com/SEU_USUARIO/organizador-de-arquivos.git

3. Execute o script:

python script.py

4. Informe o caminho da pasta que deseja organizar:

Digite o caminho da pasta que deseja organizar:
C:\Users\User\Downloads

5. Pronto! Seus arquivos serão organizados automaticamente.

## 📁 Estrutura do Projeto

organizador-de-arquivos/
│
├── script.py
├── README.md
├── log_2026-01-04.txt  (gerado automaticamente)
└── 

## 🛠️ Tecnologias Utilizadas

- Python 3  
- Módulos padrão:
  - os  
  - shutil  
  - datetime  

## 💡 Melhorias Futuras

- Interface gráfica (GUI)  
- Configurações personalizadas via arquivo `.json`  
- Suporte a mais categorias  
- Modo automático (monitoramento contínuo da pasta)  
- Versão .exe para Windows  

## 📜 Licença

Este projeto é distribuído sob a licença MIT.  
Sinta-se livre para usar, modificar e compartilhar.

## 👨‍💻 Autor

**Jonas**  
Organizador de arquivos simples, eficiente e profissional.
