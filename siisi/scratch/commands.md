# Docker Compose commands eg.:

#  Check the Odoo Version
docker-compose exec gestion_local odoo --version

# Start only the gestion_local service
docker-compose up -d gestion_local

# Stop only the gestion_local service
docker-compose stop gestion_local

# Restart only the gestion_local service
docker-compose restart gestion_local

# View logs for the gestion_local service (follow mode)
docker-compose logs -f gestion_local

# Alternatively, view logs for a container by its Docker name
docker logs gestion-web-local

# If databases already exist but have ownership issues, drop and recreate them
docker exec -it odoo-db-local psql -U odoo -d postgres -c "DROP DATABASE gestion_local;"
docker exec -it odoo-db-local psql -U odoo -d postgres -c "CREATE DATABASE gestion_local OWNER odoo;"

# Connect to PostgreSQL
docker exec -it odoo-db-local psql -U odoo -d postgres

# Run an interactive shell in the gestion_local container
docker-compose exec gestion_local /bin/bash

# Run an Odoo command inside the gestion_local container (for example, to update a module)
docker-compose exec gestion_local odoo -d gestion_local -u copro_manager --stop-after-init
# To update every installed module in your database
docker-compose exec gestion_local odoo -d gestion_local -i base --stop-after-init
docker-compose exec gestion_local odoo -d gestion_local -u all --stop-after-init
docker-compose exec odoo16_local odoo -d odoo16_local -i base --stop-after-init
docker-compose exec odoo16_local odoo -d odoo16_local -u all --stop-after-init

# Remove a specific Docker volume (if not in use)
docker volume rm gestion-web-data-local

# List Docker networks
docker network ls

# Stop & Remove the Stuck Container
docker stop odoo-db-local
docker rm odoo-db-local
# Remove the Volume & Network
docker volume rm scratch_odoo-db-data-local
docker network rm scratch_odoo-network-local

docker network create scratch_odoo-network-local
docker-compose up -d --build gestion_local
docker-compose up -d --force-recreate gestion_local

# Connect to the database
docker-compose exec db psql -U odoo -d gestion_local

# Create Module using scaffold method
docker-compose exec gestion_local odoo scaffold copro_manager /mnt/custom-addons/

# Create all Odoo Modules for 'gestion_local' Database
docker-compose down && docker-compose up -d gestion_local
docker-compose run --rm gestion_local -d gestion_local -i base --stop-after-init

# Stop and remove existing containers, networks, and volumes
docker-compose down --volumes --remove-orphans
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
# Remove All Images
docker rmi -f $(docker images -aq)
# Remove Docker System Data (Optional)
docker system prune -a --volumes -f

# Optionally prune unused volumes and networks
docker volume prune -f
docker network prune -f
docker system prune -a --volumes

# Start containers in detached mode
docker-compose up -d

# (In a separate terminal) Update Odoo modules in the container
docker-compose exec gestion_local odoo -c /etc/odoo/odoo.conf -u all --stop-after-init
