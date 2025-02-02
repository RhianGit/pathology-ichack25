import torch
import torch.nn as nn
import torchvision
from torchvision import models, transforms, utils
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
from PIL import Image
import json
import cv2 as cv

SIZE = (224, 224)
device = torch.device("cpu")

transform = transforms.Compose([
    transforms.Resize(SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=0., std=1.)
])

LAYER_NO = 8
image = Image.open("sample.jpeg")

model = models.resnet18(pretrained=True).to(device)

#we will save the 49 conv layers in this list
conv_layers = []
# get all the model children as list
model_children = list(model.children())
#counter to keep count of the conv layers
counter = 0
#append all the conv layers and their respective wights to the list
for i in range(len(model_children)):
    if type(model_children[i]) == nn.Conv2d:
        counter+=1
        conv_layers.append(model_children[i])
    elif type(model_children[i]) == nn.Sequential:
        for j in range(len(model_children[i])):
            for child in model_children[i][j].children():
                if type(child) == nn.Conv2d:
                    counter+=1
                    conv_layers.append(child)

def process(image, cb):
    image = transform(image).unsqueeze(0).to(device)

    for i, layer in enumerate(conv_layers[:LAYER_NO+1]):
        image = layer(image)
    output = image.squeeze(0)
    gray = torch.sum(output, 0)
    gray /= output.shape[0]
    processed = gray.data.cpu().numpy()
    processed = cv.resize(processed, dsize=SIZE, interpolation=cv.INTER_CUBIC)
    lb = processed.min()
    ub = processed.max() - lb
    processed -= lb
    processed /= ub
    # processed = processed ** 3

    out = np.zeros((processed.shape[0], processed.shape[1], 4), dtype=np.uint8)
    out[:,:,0] = 255 if not cb else 0  #blue
    out[:,:,1] = 0
    out[:,:,2] = 0
    out[:,:,3] = (processed*255).astype(np.uint8)
    out[:,:,3] //= 2
    return out
