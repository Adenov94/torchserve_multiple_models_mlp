#For Multi model in Torchserve 
#FILENAME=test_mlp


#archive the model and convert to .mar file
torch-model-archiver --model-name  MLP_one \
                     --version  1.0 \
                     --model-file   mlp_arch.py \
                     --serialized-file  mlp.pth \
                     --handler MLP_one_handler.py \
                     --export-path model-store --force

torch-model-archiver --model-name  MLP_two \
                     --version  1.0 \
                     --model-file   mlp_arch.py \
                     --serialized-file  mlp.pth \
                     --handler MLP_two_handler.py \
                     --export-path model-store --force


#workflow preparation
torch-workflow-archiver -f \
                    --workflow-name seq_mlp \
                    --spec-file workflow_pipeline.yaml \
                    --handler workflow_handler.py \
                    --export-path wf-store/ \
                    --force


