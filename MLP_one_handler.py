import torch 
import base64
import io
import time 
import os 
import ast 

from PIL import Image
from torchvision import transforms
from ts.torch_handler.image_classifier import ImageClassifier
from torch.profiler import ProfilerActivity
import json


class CustomImageInput(ImageClassifier):

    image_processing = transforms.Compose([
       transforms.Grayscale(1), 
       transforms.Resize((100, 10)), 
       transforms.ToTensor()
    ])

    def __init__(self):
        super(CustomImageInput, self).__init__()

    
    def get_json_from_bytesarray(self, data: bytearray) -> dict:
        """ Converting messages between model modules into json for multiple input 
        Args: 
            data (bytesarray): message from preprocessing modules 
            
        Returns: 
            Dict: dictiniary object with two  images 
        """
        data = data[0].get("body")
        data = io.BytesIO(data)
        data = data.getvalue()
        data = data.decode("UTF-8")
        data = ast.literal_eval(data)
        
        return data
        
    
    def preprocess(self, data: list) -> torch.float32:
        """The preprocess function of MNIST program converts the input data to a float tensor

        Args:
            data (List): Input data from the request is in the form of a Tensor

        Returns:
            list : The preprocess function returns the input image as a list of float tensors.
        """
        #TO DO: handle in future to raise Spec error form torchserve 
        #if len(data) > 1: 
        #    raise RuntimeError("No batch ")
        
        #image = data[0].get("preprocessing").decode()
    
        images = self.get_json_from_bytesarray(data)
       
        image = base64.b64decode(images["image_one"])
        image = self.image_processing(Image.open(io.BytesIO(image)))
        
        return image.to(self.device)

    def inference(self, data, *args, **kwargs):
        """
        The Inference Function is used to make a prediction call on the given input request.
        The user needs to override the inference function to customize it.

        Args:
            data (Torch Tensor): A Torch Tensor is passed to make the Inference Request.
            The shape should match the model input shape.

        Returns:
            Torch Tensor : The Predicted Torch Tensor is returned in this function.
        """
        with torch.no_grad():
            marshalled_data = data.to(self.device)
            result = self.model(marshalled_data).cpu().detach().tolist()
        
        return result
    
    def handle(self, data, context):
        """Entry point for default handler. It takes the data from the input request and returns
           the predicted outcome for the input.

        Args:
            data (list): The input data that needs to be made a prediction request on.
            context (Context): It is a JSON Object containing information pertaining to
                               the model artefacts parameters.

        Returns:
            list : Returns a list of dictionary with the predicted response.
        """

        # It can be used for pre or post processing if needed as additional request
        # information is available in context
        start_time = time.time()

        self.context = context
        metrics = self.context.metrics
        
        
        data_preprocess = self.preprocess(data)
        output = self.inference(data_preprocess)
        output = self.postprocess(output)
       
        stop_time = time.time()
        metrics.add_time(
            "HandlerTime", round((stop_time - start_time) * 1000, 2), None, "ms"
        )
        return output


    def postprocess(self, data):
        """The post process of MNIST converts the predicted output response to a label.
        Args:
            data (list): The predicted output from the Inference with probabilities is passed
            to the post-process function
        Returns:
            list : A list of dictionaries with predictions and explanations is returned
        """
        #postdata = data.cpu().detach().tolist()
        return data