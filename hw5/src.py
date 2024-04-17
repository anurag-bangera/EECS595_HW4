from transformers import AutoTokenizer, AutoModelForCausalLM

def gemeni(prompt):
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
    model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

    input_text = prompt
    input_ids = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(**input_ids,max_new_tokens=10)
    print(tokenizer.decode(outputs[0]))
