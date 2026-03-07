import os
import zipfile
from datetime import datetime
from pathlib import Path

class BackupManager:
    """
    Automatiza o processo de criação de arquivos .zip de pastas importantes,
    adicionando um timestamp ao nome do arquivo para controle de versão.
    """
    def __init__(self, pasta_origem, pasta_destino):
        self.pasta_origem = Path(pasta_origem)
        self.pasta_destino = Path(pasta_destino)
        
    def criar_backup(self):
        if not self.pasta_origem.exists():
            print(f"Erro: A pasta de origem '{self.pasta_origem}' não existe.")
            return

        # Cria a pasta de destino se não existir
        self.pasta_destino.mkdir(parents=True, exist_ok=True)

        # Gera o nome do arquivo com a data e hora atual
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo_zip = f"backup_{self.pasta_origem.name}_{timestamp}.zip"
        caminho_completo_zip = self.pasta_destino / nome_arquivo_zip

        print(f"Iniciando backup da pasta: {self.pasta_origem}")
        print("Compactando arquivos...")

        try:
            # Cria o arquivo zip
            with zipfile.ZipFile(caminho_completo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self.pasta_origem):
                    for file in files:
                        caminho_arquivo = Path(root) / file
                        # Caminho relativo para manter a estrutura de pastas dentro do zip
                        caminho_relativo = caminho_arquivo.relative_to(self.pasta_origem)
                        zipf.write(caminho_arquivo, caminho_relativo)
            
            print(f"Sucesso! Backup criado em: {caminho_completo_zip}")
            
        except Exception as e:
            print(f"Ocorreu um erro durante o backup: {e}")

if __name__ == "__main__":
    print("=== Automação de Backup ===")
    origem = input("Digite o caminho da pasta que deseja fazer backup: ")
    destino = input("Digite o caminho onde o arquivo ZIP será salvo: ")
    
    # Exemplo de uso fixo (descomente e ajuste para agendar no Windows/Linux)
    # origem = "./meus_documentos"
    # destino = "./meus_backups"
    
    if origem and destino:
        backup = BackupManager(origem, destino)
        backup.criar_backup()
