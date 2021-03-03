# 6-5
countries = {'nile': 'egypt', 'rhine': 'france', 'yellow': 'china'}
for river, country in countries.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in countries.keys():
    print(river.title())
for country in countries.values():
    print(country.title())
# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
available_people = ['jen', 'jack', 'rose', 'phil']
for people in available_people:
    if people in favorite_languages.keys():
        print(f"Thank you, {people}.")
    else:
        print(f"{people}, please take a poll.")
# 6-7
people_0 = {'first_name': 'jack', 'last_name': 'john', 'age': 17, 'city': 'London'}
people_1 = {'first_name': 'wick', 'last_name': 'leo', 'age': 23, 'city': 'beijing'}
people_2 = {'first_name': 'rose', 'last_name': 'may', 'age': 13, 'city': 'hunan'}
people = [people_0, people_1, people_2]
for one in people:
    print(f"{one['first_name'].title()} {one['last_name'].title()}:\n\tage: {one['age']}\n\tcity: {one['city']}")
