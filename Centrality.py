


import pandas as pd



input_file=pd.read_csv('../dataset//weatherAUS.csv')


# ## Variables in the data


input_file.columns


# ## Calculating Mean, Median and Mode of all columns:


print("\n----------- Calculate Mean -----------\n")
print(input_file.mean())



print("\n----------- Calculate Median -----------\n")
print(input_file.median())



print("\n----------- Calculate Mode -----------\n")
print(input_file.mode().iloc[0])



print("Mode of column 'Location':  "+str(input_file['Location'].mode().iloc[0]))
print("Mode of column 'Date':  "+str(input_file['Date'].mode().iloc[0]))
print("Mode of column 'WindGustDir':  "+str(input_file['WindGustDir'].mode().iloc[0]))
print("Mode of column 'WindDir9am':  "+str(input_file['WindDir9am'].mode().iloc[0]))
print("Mode of column 'WindDir3pm':  "+str(input_file['WindDir3pm'].mode().iloc[0]))
print("Mode of column 'RainToday':  "+str(input_file['RainToday'].mode().iloc[0]))
print("Mode of column 'RainTomorrow':  "+str(input_file['RainTomorrow'].mode().iloc[0]))




