#!/bin/sh
set -e

echo "🚀 Avvio del progetto n8n con Docker Compose..."

docker-compose up -d

echo "⏳ Verifico che n8n sia avviato correttamente..."

# Controlla se il container n8n è in esecuzione
if docker-compose ps | grep -q 'n8n.*Up'; then
  echo "✅ Container n8n è in esecuzione."
else
  echo "❌ Errore: il container n8n non è partito correttamente."
  exit 1
fi

# Verifica che n8n risponda sulla porta 5678 (timeout 10 secondi)
timeout=10
success=0
while [ $timeout -gt 0 ]; do
  if curl -s http://localhost:5678 > /dev/null; then
    success=1
    break
  else
    echo "⌛ Attendo che n8n risponda..."
    sleep 1
    timeout=$((timeout - 1))
  fi
done

if [ $success -eq 1 ]; then
  echo "✅ n8n è disponibile su http://localhost:5678"
else
  echo "❌ Errore: n8n non risponde sulla porta 5678."
  exit 1
fi
