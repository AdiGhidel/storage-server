# storage-server

Built with:
- `python flask` for backend
- `react` for frontend
## Prerequisites
- npm
- yarn
- docker
- python3
- curl

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


## Implementation details
1. Backend
- The back-end runs with python flask
- it supports the three API routes from the requirement + OPTIONS which was needed for the preflighted requests (CORS)
- it has a small functional test script which runs curl to check the basic backend operations
- this module still needs unit-tests 
- the dependencies should be covered in requirement.txt and are automatically installed in the docker image. They can be installed locally for deployment

2. FrontEnd
- The front-end was done in React
- It supports the basic requirements, but nothing more
- It was my first attempt at doing front-end so it most likely is not using the well known practices. This is just manually tested
- The dependencies should be managed by yarn / package.json



