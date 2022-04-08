import math
data = pd.read_excel("C:\\users\\HP\\Documents\\Datascience task\\car_prediction.xlsx")
data = data.drop(['Unnamed: 3'],axis='columns')

x = data[['Weight','Insurance']].values 
y = data[['Road Tax']].values

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x,y)
g = lr.predict([[2400,334]]) # Input: Weight,Insurance 
print(g) # Output: array([[1211.70744527]])
