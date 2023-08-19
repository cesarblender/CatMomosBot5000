import random
from src.utils.huggingface import interact_with_model

def gen_text(text: str):
    model_name = "bigscience/bloom"
    inputs = text
    
    blacklist = [17, -2063]

    generated_text, parameters = interact_with_model(model_name, inputs, with_seed=True, seed_blacklist=blacklist)

    return generated_text, parameters

def gen_boomer_text():
    texts = [
        "VEAN LA FOTO DE ESTE GATO, ESTE GATO ES LA MERA VRG, LO QUIERO MUCHO, SE LA PASA TODO EL DIA",
        "ESTE GATO ES UN PENDEJO, LO QUIERO MUUUUCHOOO, ESTOY FELIZ DE QUE ESTE GATO ME QUIERA MIN TAMBIEN, ES QUE",
        "HOLA BECIS, COMO ESTAN AQUI ESTOY CON MI GATICO LO QUIERO MUCHO ANQUE ES PENDEJO Y NO CAZA, EL GATO",
        "MIREN A MI GATO BESIS, ME DICE TE QUIERO TODOS LOS DIAS,",
        "ESTE GATO LO QUIERO MUCHO, ES MUY LINDO Y",
        "Miau miau miau miau miau miau miau miau miau",
        "Soy consciente, soy consistente, Soy consciente, soy consistente, Soy consciente, soy consistente, Para que se den cuenta, para que vean que soy consciente, miren, la consciencia es"
    ]

    return gen_text(random.choice(texts))

