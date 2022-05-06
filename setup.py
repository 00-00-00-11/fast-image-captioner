import os
from os.path import exists 
from clip_client import Client
from docarray import Document
from utils import *

if not exists("cc_captions.txt"):
  os.system("python -m wget https://raw.githubusercontent.com/annasajkh/30k-cc-captions/main/cc_captions.txt")


client = Client("http://demo-cas.jina.ai:51001")
captions = open("cc_captions.txt", "r").read().split("\n")
encoded = None

for batch in batching(captions, 200):
  if encoded is None:
    encoded = client.encode([Document(text=caption) for caption in batch], show_progress=True)
  else:
    encoded = encoded + client.encode([Document(text=caption) for caption in batch], show_progress=True)

del captions