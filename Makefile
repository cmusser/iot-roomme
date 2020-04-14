NAME ?= iot-roomme
APP_VER ?= 1.0.0

.PHONY: build version

build:
	export APP_VER=$(APP_VER)
	docker build -t $(NAME) .
	docker tag $(NAME) $(NAME):$(APP_VER)

version:
	@echo $(APP_VER)
