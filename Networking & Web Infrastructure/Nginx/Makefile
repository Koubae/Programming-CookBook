.PHONY: up down restart logs help nginx-terminal nginx-recreate service_a service_b

help:
	@echo "Docker Compose Commands:"
	@echo "  make up              - Start all containers (nginx, service-a, service-b)"
	@echo "  make down            - Stop and remove all containers"
	@echo "  make restart         - Restart all containers"
	@echo "  make logs            - Follow logs from all containers"
	@echo "  make nginx-terminal  - Connect to Nginx CLI terminal"
	@echo "  make nginx-recreate  - Force recreate Nginx container"
	@echo ""
	@echo "Individual Services:"
	@echo "  make service_a      - Start service-a container"
	@echo "  make service_b      - Start service-b container"
	@echo "  make help           - Show this help message"

up:
	docker-compose --env-file .env.nginx up -d nginx

down:
	docker-compose --env-file .env.nginx down nginx
down-all:
	docker-compose --env-file .env.nginx down 
restart:
	docker-compose --env-file .env.nginx restart nginx

logs:
	docker-compose --env-file .env.nginx logs -f nginx

nginx-terminal:
	docker exec -it nginx bash

nginx-recreate:
	docker-compose --env-file .env.nginx up -d --force-recreate nginx

# ----------------------------------
# Individual Services (Docker Compose)
# ----------------------------------
service_a:
	docker-compose --env-file .env.nginx up service-a

service_b:
	docker-compose --env-file .env.nginx up service-b
