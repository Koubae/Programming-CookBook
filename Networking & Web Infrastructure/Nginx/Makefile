.PHONY: nginx-up nginx-down nginx-terminal nginx-logs help

help:
	@echo "Nginx Docker Compose Commands:"
	@echo "  make nginx-up      - Start Nginx container"
	@echo "  make nginx-down    - Stop Nginx container"
	@echo "  make nginx-terminal- Connect to Nginx CLI terminal"
	@echo "  make nginx-logs    - Follow Nginx container logs"
	@echo "  make help          - Show this help message"

nginx-up:
	docker-compose up -d nginx

nginx-down:
	docker-compose stop nginx
	docker-compose rm -f nginx

nginx-terminal:
	docker exec -it nginx bash

nginx-logs:
	docker-compose logs -f nginx
