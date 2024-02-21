torchserve --start \
            --model-store model-store/ \
            --workflow-store wf-store/ \
            --ncs #> /dev/null 2>&1 && \ 
            # curl -X POST "http://localhost:8081/workflows?url=seq_mlp.war"
            #--models MLP_one=./model_store/MLP_one.mar \
            #MLP_two=./model_store/MLP_two.mar 