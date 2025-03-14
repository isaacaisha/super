# Commands for Odoo

<!-- Installation -->
sudo apt update
sudo apt upgrade -y
sudo apt install -y docker.io docker-compose

<!-- Docker -->
docker --version
docker-compose --version

sudo systemctl restart docker
sudo systemctl status docker

<!-- Start Odoo -->
docker-compose up -d
<!-- Stop Odoo Docker -->
docker-compose down

<!-- Check if all containers are running -->
docker ps

<!-- Check logs -->
docker-compose logs -f db      # PostgreSQL logs
docker-compose logs -f odoo16  # Odoo 16 logs
docker-compose logs -f odoo17  # Odoo 17 logs
docker-compose logs -f odoo18  # Odoo 18 logs

<!-- Run Odoo into Docker bash -->
docker exec -it odoo-web-1 odoo -i base -r odoo -w odoo

# Stop and remove containers, networks, and volumes
docker-compose down --remove-orphans --volumes
# Remove any lingering Docker resources
docker system prune -a --volumes
# Remove the old network (if it exists)
docker network rm super-network

# Create a fresh network
docker network create super-network

<!-- Grant permissions to the PostgreSQL user -->
docker exec -it odoo-db-super psql -U odoo -d postgres -c "ALTER USER odoo WITH SUPERUSER;"
# Check if the odoo user has the correct privileges
docker exec -it odoo-db-super psql -U odoo -d postgres -c "\du odoo"
# Apply the changes
docker-compose restart odoo16 odoo17 odoo18
# Check if the odoo17 Database Exists
docker exec -it odoo-db-super psql -U odoo -d postgres -c "\l"
# If databases already exist but have ownership issues, drop and recreate them
docker exec -it odoo-db-super psql -U odoo -d postgres -c "DROP DATABASE odoo16;"
docker exec -it odoo-db-super psql -U odoo -d postgres -c "CREATE DATABASE odoo16 OWNER odoo;"

# Connect to PostgreSQL
docker exec -it odoo-db-super psql -U odoo -d postgres
# Run these SQL commands inside PostgreSQL:
GRANT ALL PRIVILEGES ON DATABASE odoo16 TO odoo;
GRANT ALL PRIVILEGES ON DATABASE odoo17 TO odoo;
GRANT ALL PRIVILEGES ON DATABASE odoo18 TO odoo;
# Make the user the owner of the databases (critical for Odoo)
ALTER DATABASE odoo16 OWNER TO odoo;
ALTER DATABASE odoo17 OWNER TO odoo;
ALTER DATABASE odoo18 OWNER TO odoo;
# Exit PostgreSQL
\q

# Delete Old Database Volumes
docker volume rm odoo-db-data-super odoo16-web-data odoo17-web-data odoo18-web-data
# First start ONLY the PostgreSQL container
docker-compose up -d db
# Wait 20 seconds for PostgreSQL to initialize
sleep 20
# Start Odoo containers (they'll auto-create databases)
docker-compose up -d odoo16 odoo17 odoo18

echo "odoo" > odoo_pg_pass

<!-- Super Password odoo18 -->
itra-emub-73eb
<!-- Super Password odoo17 -->
34s5-5ajz-sjin
<!-- Super Password odoo16 -->

sudo nano /etc/nginx/nginx.conf

docker-compose logs nginx-proxy
docker-compose logs nginx-letsencrypt

# Run an Odoo command inside the odoo_gestion container (for example, to update a module)
docker-compose exec odoo_gestion odoo -d odoo_gestion -u copro_manager --stop-after-init
docker-compose exec odoo_gestion odoo -d odoo_gestion -i base,web --stop-after-init
docker-compose down odoo_gestion
docker-compose up -d odoo_gestion
