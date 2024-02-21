import base64
import json

def preprocessing(data: dict, context: any) -> dict: 
    
    if data is None:
        #raise RuntimeError("NO DATA!...............................")
        #print("NO DATA!...............................")
        return data 
    
    image_one = data[0].get("data1")
    image_two = data[0].get("data2") 
    #image_one = data[0].get("data") or data[0].get("body")
    
    # Base64 encode the image to avoid the framework throwing
    # non json encodable errors
    # base64.b64encode(image_two).decode()
    return [{
        "image_one": base64.b64encode(image_one).decode(), 
        "image_two": base64.b64encode(image_two).decode()
    }]
 