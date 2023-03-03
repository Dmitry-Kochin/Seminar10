import pandas as pd
from sklearn.preprocessing import LabelBinarizer
lst = ['robot'] * 10
lst += ['human'] * 10
import random
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
y = LabelBinarizer().fit_transform(data)

print(data.head())
print (y)

