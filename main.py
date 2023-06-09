# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages by converting
conversion = {"M": 1000000,
              "B": 1000000000}


def updating_damages(damage_list, converting):
    updated_damages = []
    for item in damage_list:
        if item == "Damages not recorded":
            updated_damages.append(item)
        else:
            if item[-1:] == "B":  # delete the letter 'B' if there is this letter in the end of the item (str)
                item = item.strip("B")
                updated_damages.append((float(item) * converting["B"]))
            else:
                item = item.strip("M")
                updated_damages.append((float(item) * converting["M"]))
    return updated_damages


# print(updating_damages(damages, conversion))

# 2
# Create a Table
# created the dictionary with all parameters of hurricanes for future easy usage of this info
hurricane_information = {"Name": names, "Month": months, "Year": years, "Max_sustained_winds": max_sustained_winds,
                         "Areas_affected": areas_affected, "Damage": damages, "Deaths": deaths}


def hurricanes_by_name(name, information):
    dictionary = {}
    if name in information["Name"]:
        index = names.index(name)
        for key, value in information.items():
            dictionary[key] = value[index]
    else:
        print("There is no such name of hurricane.")
    return dictionary


# Create and view the hurricanes dictionary
# print(hurricanes_by_name(names[0], hurricane_information))

# 3
# Organizing by Year


def hurricanes_by_year(year, information):
    dictionary = {}
    if year in information["Year"]:
        index = years.index(year)
        for key, value in information.items():
            dictionary[key] = value[index]
    else:
        print("There is no such year of hurricane.")
    return dictionary


# create a new dictionary of hurricanes with year and key
# print(hurricanes_by_year(years[3], hurricane_information))

# 4
# Counting Damaged Areas


def hurricanes_areas(areas):
    dictionary = {}
    for area_list in areas:
        for item in area_list:
            if item not in dictionary:
                dictionary[item] = 1
            else:
                dictionary[item] += 1
    return dictionary


# create dictionary of areas to store the number of hurricanes involved in
# print(hurricanes_areas(areas_affected))

# 5
# Calculating Maximum Hurricane Count


def maximum_hurricane(hurricanes_amount):
    dictionary = {}
    max_value = 0
    for key, value in hurricanes_amount.items():
        if max_value < value:
            dictionary.clear()
            dictionary[key] = value
            max_value = value
    return dictionary


# find most frequently affected area and the number of hurricanes involved in
# print(maximum_hurricane(hurricanes_areas(areas_affected)))

# 6
# Calculating the Deadliest Hurricane


def hurricanes_deaths(information):
    dictionary = {}
    max_deaths = 0
    for value_deaths in information["Deaths"]:
        if value_deaths > max_deaths:
            max_deaths = value_deaths
    index = information["Deaths"].index(max_deaths)
    dictionary[information["Name"][index]] = max_deaths
    return dictionary


# find highest mortality hurricane and the number of deaths
# print(hurricanes_deaths(hurricane_information))

# 7
# Rating Hurricanes by Mortality


def hurricanes_by_mortality(information):
    # mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
    index = 0
    for name in information["Name"]:
        death = information["Deaths"][index]
        if death == 0:
            mortality_dict[0].append(name)
        elif death <= 100:
            mortality_dict[1].append(name)
        elif death <= 500:
            mortality_dict[2].append(name)
        elif death <= 1000:
            mortality_dict[3].append(name)
        else:
            mortality_dict[4].append(name)
        index += 1
    return mortality_dict


# categorize hurricanes in new dictionary with mortality severity as key
# print(hurricanes_by_mortality(hurricane_information))

# 8 Calculating Hurricane Maximum Damage


def hurricane_cost(information, converting):
    dictionary = {}
    clear_damages = updating_damages(information["Damage"], converting)
    greatest_deaths = 0
    for value in clear_damages:
        if value == 'Damages not recorded':
            continue
        else:
            index = clear_damages.index(value)
            dictionary[information["Name"][index]] = value
            if greatest_deaths < value and greatest_deaths == 0:
                greatest_deaths = value
            elif greatest_deaths < value:
                greatest_index = clear_damages.index(greatest_deaths)
                dictionary.pop(information["Name"][greatest_index])
                greatest_deaths = value
            else:
                dictionary.pop(information["Name"][index])
    return dictionary


# find highest damage inducing hurricane and its total cost
# print(hurricane_cost(hurricane_information, conversion))

# 9
# Rating Hurricanes by Damage


def hurricanes_by_damage(information, converting):
    # damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
    clear_damages = updating_damages(information["Damage"], converting)
    index = 0
    for name in information["Name"]:
        damage = clear_damages[index]
        if damage == 'Damages not recorded':
            index += 1
            continue
        elif damage == 0:
            damage_dict[0].append(name)
        elif damage <= 100000000:
            damage_dict[1].append(name)
        elif damage <= 1000000000:
            damage_dict[2].append(name)
        elif damage <= 10000000000:
            damage_dict[3].append(name)
        else:
            damage_dict[4].append(name)
        index += 1
    return damage_dict


# categorize hurricanes in new dictionary with damage severity as key
# print(hurricanes_by_damage(hurricane_information, conversion))
