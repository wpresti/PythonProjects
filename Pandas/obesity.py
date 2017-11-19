#uncomment plt.show() if you want to see plot in GUI
import pandas as pd
import matplotlib.pyplot as plt

#import data
data = pd.ExcelFile("Obes-phys-acti-diet-eng-2014-tab.xls")
print("The sheet names are: ", data.sheet_names)

#define columns to be read in (note-- year doens't have a header)
#so we make one
columns1 = ['year', 'total', 'males', 'females']

data_gender = data.parse(u'7.1', skiprows=4, skipfooter=14, names=columns1)

print(data_gender)
#remove N/a from data. inplace means modify the existing Dataframe
data_gender.dropna(inplace = True)
#print(data_gender)

data_gender.set_index('year', inplace=True)
print(data_gender)

#plot all
data_gender.plot()

#plt.show()
plt.savefig('obesity-gender.png', bbox_inches='tight')

#read 7.2 section, by age

data_age = data.parse('7.2', skiprows = 4, skipfooter = 14)
print(data_age)

#rename unames to year
data_age.rename(columns={'Unnamed: 0': 'year'}, inplace=True)
print(data_age)

#drop empties and reset index
data_age.dropna(inplace = True)
data_age.set_index('year', inplace = True)
print(data_age)

data_age.plot()
plt.savefig('obesity-age-wTotal.png', bbox_inches='tight')

#plotting everything caused total to override verything so drop it.

#drop the total column and plot
data_age_minus_total = data_age.drop('Total', axis = 1)

data_age_minus_total.plot()
plt.savefig('obesity-age-totalDropped.png', bbox_inches='tight')

#plt.close()

#in panas, view any column by doing this. can plot any age group aswell
print("lets just look at under 16")
print(data_age['Under 16'])

plt.close("all")    #fixed issue with ovverride

# Plot children vs adults
data_age['Under 16'].plot(label="Under 16")
data_age['35-44'].plot(label="35-44")
plt.legend(loc="upper right")
#plt.show()
plt.savefig('obesity-ChildrenVsAdults')
