import os
import requests
import random

def interact_with_model(model_name, inputs, params=None, with_seed=False, seed_blacklist=None):
    """
    Interact with a Hugging Face model API to generate text.

    Args:
        model_name (str): The name of the Hugging Face model.
        inputs (str or int): The input text or seed number for generation.
        params (dict, optional): Generation parameters. Default is None.
        with_seed (bool, optional): Whether to use a seed for generation. Default is False.
        seed_blacklist (list of int, optional): List of seed numbers to exclude. Default is None.

    Returns:
        tuple: A tuple containing the API response JSON and the used parameters.
    """
    if params is None:
        params = {
            "max_new_tokens": 40,
            "temperature": 0.6,
            "repetition_penalty": 1,
            "top_k": 15
        }

    if with_seed:
        if seed_blacklist is None:
            seed_blacklist = []
        valid_numbers = [num for num in range(-19000, 19000) if num not in seed_blacklist]
        seed = random.choice(valid_numbers)

        if isinstance(inputs, str):
            inputs = str(seed) + inputs

    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": os.getenv("HF_API_KEY")}
    response = requests.post(api_url, headers=headers, json={
        "inputs": inputs,
        "parameters": params
    })

    resp = response.json()
    generated_text = resp[0]["generated_text"]

    if with_seed and generated_text:
        params["seed"] = seed
        generated_text = generated_text.split(str(seed))[1]

    return generated_text, params
