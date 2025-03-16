# Docker Compose commands eg.:

#  Check the Odoo Version
docker-compose exec odoo_latest_local odoo --version

# Start only the odoo_latest service
docker-compose up -d odoo_latest_local

# Stop only the odoo_latest service
docker-compose stop odoo_latest_local

# Restart only the odoo_latest service
docker-compose restart odoo_latest_local

# View logs for the odoo_latest service (follow mode)
docker-compose logs -f odoo_latest_local

# Alternatively, view logs for a container by its Docker name
docker logs odoo-latest-web-local

# Connect to PostgreSQL
docker exec -it odoo-db-local psql -U odoo -d postgres

# Run an interactive shell in the odoo_latest container
docker-compose exec odoo_latest_local /bin/bash

# Run an Odoo command inside the odoo_latest container (for example, to update a module)
docker-compose exec odoo_latest odoo -d odoo_latest_local -u copro_manager --stop-after-init
docker-compose exec odoo_latest odoo -d odoo_latest_local -i base,web --stop-after-init
# To update every installed module in your database
docker-compose exec odoo_latest odoo -d odoo_latest_local -u all --stop-after-init
docker-compose exec odoo_latest odoo -d odoo_latest_local -i base --stop-after-init

# Remove a specific Docker volume (if not in use)
docker volume rm odoo-latest-web-data-local

# List Docker networks
docker network ls

# Stop & Remove the Stuck Container
docker stop odoo-db-local
docker rm odoo-db-local
# Remove the Volume & Network
docker volume rm scratch_odoo-db-data-local
docker network rm scratch_odoo-network-local

docker network create scratch_odoo-network-local
docker-compose up -d --build odoo_latest_local
docker-compose up -d --force-recreate odoo_latest_local

# Connect to the database
docker-compose exec db psql -U odoo -d odoo_latest_local

# Create Module using scaffold method
docker-compose exec odoo_latest odoo scaffold copro_manager /mnt/extra-addons/

# Create all Odoo Modules for 'odoo_the' Database
docker-compose run --rm odoo_the -d odoo_the -i base --stop-after-init

docker-compose down && docker-compose up -d odoo_gestion
