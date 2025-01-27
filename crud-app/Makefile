test:
	cd crud-app
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	pytest tests/crud_test.py

build: test
	colima start
    	docker build -t crud-app:1.0.0 .
	colima stop

release: build
	colima start
	docker-compose up --build # Integration test
	docker-compose down
	docker tag crud-app:1.0.0 crud-app:latest
	docker image save crud-app:latest -o crud-app-latest.tar
	colima stop

deploy:
	minikube image load crud-app-latest.tar # Updates local cache on all minikube nodes
	helm uninstall crud-app ./crud-app
	helm install crud-app ./crud-app

create-cluster:
        podman machine init --cpus 4 --memory 5000 --rootful # setup podman VMs
        minikube start --driver=podman --container-runtime=cri-o  --addons=metrics-server --nodes=1 --memory=4096M --cpus=4 --kubernetes-version=v1.26.5 #Setup minikube
        minikube image load crud-app-image.tar # install the crud-app image into the local container cache of all nodes of minikube cluster 
	minikube images # Hack to not setup new registry and treat local filesystem as artifact registry # also optional image loads

	cd k8s/1-observability-components
	helm dependency update 
	cd ..
	kubectl create namespace observability
	helm install -n observability observability ./1-observability-components --debug
	
	cd k8s/crud-app
	helm dependency update 
	cd ..
	kubectl create namespace crud-app
	helm install -n crud-app crud-app ./crud-app --debug

teardown-cluster:
        minikube delete
	podman machine stop
	podman machine rm
