import pandas as pd
import random
from sklearn. preprocessing import OneHotEncoder
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)
print()
encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder. fit_transform(data[['whoAmI']]). toarray ())
encoder_df.columns = ['human', 'robot']
print(encoder_df)

