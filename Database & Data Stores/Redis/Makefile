.PHONY: redis-up redis-down redis-terminal help

help:
	@echo "Redis Docker Compose Commands:"
	@echo "  make redis-up      - Start Redis container"
	@echo "  make redis-down    - Stop Redis container"
	@echo "  make redis-terminal- Connect to Redis CLI terminal"
	@echo "  make help          - Show this help message"

redis-up:
	docker-compose up -d redis

redis-down:
	docker-compose stop redis
	docker-compose rm -f redis

redis-terminal:
	docker exec -it redis redis-cli
