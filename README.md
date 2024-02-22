# Simple torchserve service 
- Multiple torch models, MLP as examples
- Possibility run on Nvidia-gpu and CPU 

## Steps 
- Install all dependencies 
- Override the model_handler.py for your input/output API 
- Generate .mar file using torchserve-model-archiver 
- Define for workflow_handler.py for muiltiple file input 
- Generate .war file via .mar and workflow_handler.py by torchserve-workflow-archiver.py 
- Run on Torchserve 


## Running on GPU 
- need to change base image in Dockerfile 
- Install all cuda drivers inside Docker  