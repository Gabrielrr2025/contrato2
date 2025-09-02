import os, shutil
from datetime import datetime

def backup_sqlite(db_path: str, backup_dir: str):
    if not os.path.exists(db_path):
        print(f"❌ Banco não encontrado: {db_path}")
        return False
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"contratos_backup_{timestamp}.db")
    shutil.copy2(db_path, backup_path)
    print(f"✅ Backup criado: {backup_path}")
    return True

if __name__ == "__main__":
    backup_sqlite("contratos.db", "backups")
