
import pandas as pd

# Load Dataset Efficiently

data = pd.read_csv("unclean_orders_500.csv")

print(data)
# Initial Data Profiling
print(data.shape)
print(data.head())
print(data.info())
print(data.describe())

# Cleaning column name
data.columns = (data.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove white spaces from row.
data = data.map(
    lambda x: x.strip() if isinstance(x, str) else x
)
data.head()


#  Fix Age
# convert age colum to numeric and if error in converting unknown value then covert NaN
data['age'] = pd.to_numeric(data['age'], errors = 'coerce')

# fill NaN value with median
data['age'].fillna(data['age'].median(), inplace = True)


#  Fix numeric columns
data['price'] =    pd.to_numeric   (data['price'], errors = 'coerce') 
data['quantity'] = pd.to_numeric(data['quantity'], errors = 'coerce')

# systematic date formate
data['order_date'] = pd.to_datetime(
    data['order_date'], errors = 'coerce'
)

# fill the missing dates
data['order_date'].fillna(method = 'ffill', inplace = True)

#  Convert to standard format
data['order_date'] = data['order_date'].dt.strftime('%y-%m-%d')


print(data.columns)

# Handle missing payment method
data['payment_method'].fillna("Unknown", inplace=True)


# Remove rows with missing date
data.dropna(subset=['order_date'], inplace=True)


# Remove invalid emails
data = data[data['email'].str.contains("@",na = False)]


# Recalculate total amount
data['total_amount'] = data['price'] * data['quantity']


# Standardize text
data['gender'] = data['gender'].str.capitalize()
data['country'] = data['country'].str.title()


# Remove invalid values
data = data[(data['price'] > 0) & (data['quantity'] > 0)] 


# Save cleaned data
data.to_csv("cleaned_datset2.csv", index = False)

print(data['order_date'].head(20))






