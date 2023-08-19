import os
import requests
import time
import random

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": os.getenv("HF_API_KEY")}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def gen_boomer_text():
    blacklist = [17]
    valid_numbers = [num for num in range(-1000, 1000) if num not in blacklist]
    seed = random.choice(valid_numbers)

    parameters = {
        "max_new_tokens": 40,
        "temperature": 0.7,
        "repetition_penalty": 1.5,
        "top_k": 10
    }

    output = query({
        "inputs": str(seed) + "VEAN LA FOTO DE ESTE GATO, ESTE GATO ES LA MERA VRG, LO QUIERO MUCHO, SE LA PASA TODO EL DIA",
        "parameters": parameters
    })

    parameters["seed"] = seed

    return (output[0]["generated_text"].split(str(seed))[1], parameters)
