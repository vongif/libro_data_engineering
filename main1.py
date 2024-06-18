from faker import Faker
import json
import pandas as pd
import pandas.io.json as pd_JSON

#output=open('data.JSON','w')

fake=Faker()

alldata={}
alldata['records']=[]

for x in range(1000):
    data={"name":fake.name(),"age":fake.random_int
        (min=18, max=80, step=1),
        "street":fake.street_address(),
        "city":fake.city(),"state":fake.state(),
        "zip":fake.zipcode(),
        "lng":float(fake.longitude()),
        "lat":float(fake.latitude())}
    alldata['records'].append(data)

with open('data.json', 'w') as output:
    json.dump(alldata, output)
#json.dump(alldata,output)

with open("data.JSON","r") as f:
    data=json.load(f)
    data['records'][0]
    data['records'][0]['name']

df=pd.read_json('data.JSON')


# Normalizar los datos JSON
normalized_df = pd.json_normalize(df['records'])

# Ahora `normalized_df` contiene el DataFrame normalizado
print(normalized_df.head())  # Muestra las primeras filas del DataFrame normalizado

