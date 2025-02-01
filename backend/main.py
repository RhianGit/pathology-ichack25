from transformers import pipeline
from PIL import Image
import requests
import torch as T
import matplotlib.pyplot as plt

device = T.device("cpu")

checkpoint = "facebook/sam-vit-base"
mask_generator = pipeline(model=checkpoint, task="mask-generation", device=device)

img_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"
image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")

masks = mask_generator(image, points_per_batch=128, pred_iou_thresh=0.88)

plt.imshow(image, cmap='gray')

for i, mask in enumerate(masks["masks"]):
    plt.imshow(mask, cmap='viridis', alpha=0.1, vmin=0, vmax=1)

plt.axis('off')
plt.show()