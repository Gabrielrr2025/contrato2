#!/bin/bash
set -e
echo "🚀 Iniciando deploy..."
pip install --no-cache-dir -r requirements.txt
mkdir -p templates contratos_gerados uploads
python -c "from db import init_db; init_db()"
echo "✅ Deploy concluído!"
