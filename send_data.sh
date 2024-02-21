
# curl http://127.0.0.1:8080/wfpredict/seq_mlp -T /home/adil/Downloads/123.jpg

curl -X POST http://localhost:8080/wfpredict/seq_mlp \
     -F  data1='@./test_images/IMG_0520.JPG' \
     -F data2='@./test_images/sample_1.jpg'

# curl -X POST http://localhost:8080/predictions/test_mlp  -F  data='@/home/adil/Downloads/123.jpg' & \
# curl -X POST http://localhost:8080/predictions/test_mlp  -F data='@/home/adil/Downloads/crop_12.jpg'

#POST workflows pipeline 
# curl -X POST "http://127.0.0.1:8081/workflows?url=seq_mlp.war"

#Check the model property
# curl http://localhost:8081/models/test_mlp

#healthy check
# curl -X POST http://0.0.0.0:8080/ping 
