import pickle
import pandas as pd
import os
from recom_model import Model
import time

def main():
    model = Model()
    raw_ds = pd.read_csv(os.environ['DATA'])
    model.train(raw_ds)

    print('==== model training ====')
    model = dict(
            model = model,
            version = os.environ['VERSION'],
            model_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )
    print('==== model trained ====')

    pickle.dump(model, open('/data/model.pkl','wb'))
    print('==== model saved ====')

if __name__ == '__main__':
    main()
