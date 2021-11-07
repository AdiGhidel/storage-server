# storage-server

Built with:
- `python flask` for backend
- `react` for frontend
## Prerequisites
- npm
- yarn
- docker
- python3

### Note: prerequisites installation is not present here


## Scenarios
1. Run local tests
- `make run-local-server`
- `make test-server`

2. Run Gui
- `make run-local-server`
- `make run-gui` # this will open a browser with the gui

3. Build docker:
- if you want to run in a containerized environment you can build as a docker image
- can be deployed to k8s with a few extra steps (not present here)
- `make build-docker` 
