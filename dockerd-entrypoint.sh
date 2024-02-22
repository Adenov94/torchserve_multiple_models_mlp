#!/bin/bash
set -e

if [[ "$1" = "serve" ]]; then
    shift 1
    torchserve --start \
            --model-store model-store/ \
            --workflow-store wf-store/ \
            --ncs  > /dev/null 2>&1 && \
            sleep 5
            curl -X POST "http://0.0.0.0:8081/workflows?url=seq_mlp.war"

    
else
    eval "$@"
fi

# prevent docker exit
tail -f /dev/null
