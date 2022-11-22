import pandas as pd

df = pd.read_csv('C:\\WGU\\D211 Advanced Data Acquisition\\tables\\WA_Fn-UseC_-Telco-Customer-Churn.csv')

print(df.info())

# print list of column names to confirm which columns need to be modified & how they are named.
for col in df.columns:
    print(col)

# columns to replace: Contract & PaymentMethod

# print value counts to view values & their spelling
print(df.Contract.value_counts())

df.Contract.replace(['Month-to-month', 'One year', 'Two year'], [1, 2, 3], inplace=True)

# print new value counts to confirm the replace took correctly
print(df.Contract.value_counts())

# print value counts to view values & their spelling
print(df.PaymentMethod.value_counts())

df.PaymentMethod.replace(['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'],
                         [1, 2, 3, 4], inplace=True)

# print new value counts to confirm the replace took correctly
print(df.PaymentMethod.value_counts())

# export to csv to be imported into database as table
df.to_csv('C:\\WGU\\D211 Advanced Data Acquisition\\tables\\competitor_churn_scraped.csv')