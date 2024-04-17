from hw5.src import gemeni
import json
#gemeni("Hello")
data=[]
with open("./hellaswag_val.300.jsonl", "r") as file:
    for line in file:
        data.append(json.loads(line))
questions=[]
for query in data:
    questions.append({"q":query["ctx"], "a":query["endings"], "c":query["label"]})

for q in questions:
    q["basic_prompt"]=f'Finish the statement: \"{q["q"]}\" with:\nA. {q["a"][0]}\nB. {q["a"][1]}\nC. {q["a"][2]}\nD. {q["a"][3]}'
    q["prompt"]=f'Given the statement: \"{q["q"]}\" choose the ending which matches best:\nA. {q["a"][0]}\nB. {q["a"][1]}\nC. {q["a"][2]}\nD. {q["a"][3]}'
gemeni("hi")