import pandas as pd
import matplotlib.pyplot as plt

def get_top_cities(df, num_cities=10):
    # Get city to counts
    city_to_count = dict()
    for _, row in df.iterrows():
        if row['City'] in city_to_count:
            city_to_count[row['City']] += int(row['Num_Conf'])
        else:
            city_to_count[row['City']] = 0
    # Create list of [city, counts]
    city_count = []
    for city in city_to_count:
        city_count.append([city, city_to_count[city]])
    # Sort list
    city_count.sort(key=lambda x: x[1], reverse=True)
    # Getting list of top 
    cities = []
    for i in range(min(num_cities, len(city_count))):
        cities.append(city_count[i][0])

    return cities

plt.figure().set_figwidth(400)
plt.figure().set_figheight(800)
df = pd.read_csv(
    'MAY_num_conf_per_city_per_year.csv', 
    sep='\t', 
    names=['Year', 'City', 'Num_Conf'], 
    header=None
)
years = df['Year'].unique()
for i in range(len(years)):
    years[i] = int(years[i])
years = sorted(years)
# df = df.head(10)

plt.rcParams.update({'font.size': 40})
plt.figure(figsize=(40, 40))

cities = get_top_cities(df, 10)
for city in cities:
    counts = []
    for year in years:
        result = df.query(f'City == "{city}" and Year == {year}')
        if result.shape[0]:
            counts.append(result.iloc[0].iloc[2])
        else:
            counts.append(0)
    plt.plot(years, counts, label=city)


plt.title('Number of Conferences per City per Year', fontdict={'fontsize':50})
plt.xlabel('Year', fontdict={'fontsize':45})
plt.xticks(years, years)
plt.ylabel('Number of Conferences', fontdict={'fontsize':45})
plt.legend(loc='upper right')
plt.savefig('num_conf_per_city_per_year.pdf')