from datasets import load_dataset
import pandas as pd

dataset = load_dataset("OpenAssistant/oasst1")
#dataset = pd.read_csv("OpenAssistant/oasst1")
dataset_filtrado= dataset.filter(lambda x : x["lang"]=="es")

print("-------------------------------------------------------------------------------------------------------\n-------------------------------------------------------------------------------------------------------")
print(dataset)
print("-------------------------------------------------------------------------------------------------------\n-------------------------------------------------------------------------------------------------------")
print (dataset_filtrado)