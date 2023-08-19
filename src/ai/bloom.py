from src.utils.huggingface import interact_with_model

def gen_boomer_text():
    model_name = "bigscience/bloom"
    inputs = "VEAN LA FOTO DE ESTE GATO, ESTE GATO ES LA MERA VRG, LO QUIERO MUCHO, SE LA PASA TODO EL DIA"
    
    blacklist = [17]

    generated_text, parameters = interact_with_model(model_name, inputs, with_seed=True, seed_blacklist=blacklist)

    return generated_text, parameters
