from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(webpage.content, "html.parser")

find_rating = soup.find_all(attrs={"class": "Rating"})
ratings = []
for text in find_rating[1:]:
    txt = text.get_text()
    ratings.append(float(txt))

plt.hist(ratings)
plt.show()

company_data = soup.find_all(attrs={"class": "Company"})
companies = []
for company in company_data[1:]:
    company = company.get_text()
    companies.append(company)

d = {'Company': companies, 'Rating': ratings}

df = pd.DataFrame.from_dict(d)
df.head()

mean_ratings = df.groupby("Company").Rating.mean()
ten_best = mean_ratings.nlargest(10)

cocoa_data = soup.find_all(attrs={'class': 'CocoaPercent'})
cocoa = []
for percent in cocoa_data[1:]:
    percent = percent.get_text()
    cocoa.append(float(percent.strip('%')))

df['CocoaPercentage'] = cocoa
df.head()

plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()

plt.cla()
plt.scatter(df.CocoaPercentage, df.Rating)

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
