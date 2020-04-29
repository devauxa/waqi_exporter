PROJECT_NAME := exporter_external

docker:
	DOCKER_BUILDKIT=1 docker build -t $(PROJECT_NAME) .
