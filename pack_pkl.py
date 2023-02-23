import pickle
import pandas as pd
import os
from project2.CompSci401.recom_model import Model
import datetime

def main():
    model = Model()
    raw_ds = pd.read_csv(os.environ['DATA'])
    model.train(raw_ds)

    e = datetime.datetime.now()
    print('model training')
    model = dict(
            model = model,
            version = os.environ['VERSION'],
            model_date = e.strftime("%Y-%m-%d %H:%M:%S")
        )
    print('model trained')
    pickle.dump(model, open('/data/model.pkl','wb'))
    print('model saved')

if __name__ == '__main__':
    main()
