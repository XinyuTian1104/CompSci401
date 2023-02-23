DOCKER_REGISTRY=docker.io
DOCKER_USERNAME=michelletian1104
IMAGE1_NAME=frontend
IMAGE2_NAME=ml
TAG=latest

.PHONY: build-image1
build-image1:
	docker buildx build --platform linux/amd64 --file docker/frontend.dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG) .

.PHONY: build-image2
build-image2:
	docker buildx build --platform linux/amd64 --file docker/ml.dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG) .

.PHONY: push-image1
push-image1:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG)

.PHONY: push-image2
push-image2:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG)

.PHONY: docker 
docker: build-image1 build-image2 push-image1 push-image2