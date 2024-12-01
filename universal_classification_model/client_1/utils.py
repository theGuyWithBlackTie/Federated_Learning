import pandas as pd

def load_data():
    data_file = "client_1/amazon_cells_labelled.txt"

    with open(data_file, 'r') as f_obj:
        data = f_obj.readlines()

    raw_text = []
    label = []
    for each_elem in data:
        content = each_elem.split("\t")
        raw_text.append(content[0].strip(" \n."))
        label.append("Negative" if '0' in content[1].strip(" \n.") else "Positive")
    
    dataframe = pd.DataFrame.from_dict({"text": raw_text, "label": label})
    return dataframe