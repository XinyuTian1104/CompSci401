import pickle
import pandas as pd
import os
from recom_model import Model
import datetime

model = Model()
raw_ds = pd.read_csv(os.environ['DATA'])
model.train(raw_ds)

e = datetime.datetime.now()
# print(model.train(raw_ds))
# print(model.rules)

model = dict(
        model = model,
        version = os.environ['VERSION'],
        model_date = e.strftime("%Y-%m-%d %H:%M:%S")
    )

pickle.dump(model, open('model.pkl','wb'))
