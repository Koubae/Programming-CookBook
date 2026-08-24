.PHONY: nginx-up nginx-down nginx-restart nginx-terminal nginx-logs help

help:
	@echo "Nginx Docker Compose Commands:"
	@echo "  make nginx-up       - Start Nginx container"
	@echo "  make nginx-down     - Stop Nginx container"
	@echo "  make nginx-restart  - Restart Nginx container"
	@echo "  make nginx-terminal - Connect to Nginx CLI terminal"
	@echo "  make nginx-logs     - Follow Nginx container logs"
	@echo "  make help           - Show this help message"

nginx-up:
	docker-compose --env-file .env.nginx up -d nginx

nginx-down:
	docker-compose --env-file .env.nginx down

nginx-restart:
	docker-compose --env-file .env.nginx restart nginx

nginx-terminal:
	docker exec -it nginx bash

nginx-recreate:
	docker-compose --env-file .env.nginx up -d --force-recreate nginx

nginx-logs:
	docker-compose logs -f nginx
