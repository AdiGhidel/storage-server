build-docker:
	docker build -f server/Dockerfile -t storageserver .

run-docker:
	docker run -p 5000:5000 storageserver

run-local-server:
	python3 server/server.py   

run-gui:
	cd gui; yarn start

test-server:
	./server/testscript.sh