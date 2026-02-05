# Progetto Docker Compose per n8n

Questo progetto contiene una configurazione Docker Compose per eseguire n8n, un tool di automazione dei workflow.

## Contenuti

- `docker-compose.yml`: definisce i servizi necessari per avviare n8n.
- `Dockerfile.runners`: Dockerfile personalizzato per i runner di n8n.
- `run.sh`: script di avvio per facilitare il lancio del progetto.
- `./tutorial`: cartella che contiene alcuni forkflow e programmi di supporto in python.

**ATTENZIONE:** i file del tutorial contengono configurazione che si trova dentro le variabili d'ambiente. Copiare il file `.env.example` nel file `.env` inserendo i propri parametri.


## Come usare

1. Assicurati di avere Docker e Docker Compose installati.
2. Avvia i container con il comando:

   ```bash
   docker-compose up -d
   ```


