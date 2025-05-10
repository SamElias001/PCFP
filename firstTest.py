import json
description = 'Sorvete'
price = 5.50
date = '10/05/2025'
data = {
    'Descrição': description,
    'Preço': price,
    'Data': date,
}
# Convert the dictionary to a JSON string
with open ('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)