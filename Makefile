IMAGE_NAME=python-base
CONTAINER_NAME=python-base

build:
	docker build --no-cache -f docker-local/python/Dockerfile -t ${IMAGE_NAME} .

up:
	docker run --rm -it --name ${CONTAINER_NAME} ${IMAGE_NAME}

shell:
	docker exec -it ${CONTAINER_NAME} base
