from datasets import load_dataset
import csv

dataset = load_dataset("OpenAssistant/oasst1")
#dataset = pd.read_csv("OpenAssistant/oasst1")
dataset_filtrado= dataset.filter(lambda x : x["lang"]=="es")

print("-------------------------------------------------------------------------------------------------------\n-------------------------------------------------------------------------------------------------------")
print(dataset)
print("-------------------------------------------------------------------------------------------------------\n-------------------------------------------------------------------------------------------------------")
print (dataset_filtrado)

def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def process_data(csv_data):
    # You can implement your processing logic here
    # For example, you might want to convert it to a dictionary
    # or perform any other data manipulation required for your chatbot
    processed_data = []
    for row in csv_data:
        processed_data.append({
            'question': row[0],
            'answer': row[1]
        })
    return processed_data

csv_data = read_csv("nombre csv")
processed_data = process_data(csv_data)

for item in processed_data:
    print("User: ", item['question'])
    print("Bot: ", item['answer'])
