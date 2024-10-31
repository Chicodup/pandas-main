import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?

# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?

paid_apps = df[df['Type']=='paid']
# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
print(paid_apps['Price'].min())
# print(df[df['Type'] == 'Paid']['Reviews'].max() - df[df['Type'] == 'Free']['Reviews'].max())
art= df[df['Category'] == "ART_AND_DESIGN"]
# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')
print(round(art[installs].median()))
# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?
paid_apps = df[df['Type']=='Paid']
free_apps = df[df['Type']=='Paid']
max_paid = paid_apps['Reviews'].max()
max_free = free_apps['Reviews'].max()
print(max_free - max_paid)

# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
business = df[df['category']