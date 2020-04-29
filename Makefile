PROJECT_NAME := exporter_waqi

docker:
	DOCKER_BUILDKIT=1 docker build -t $(PROJECT_NAME) .
