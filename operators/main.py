# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# 1.
language_spain = 'Spanish'
language_switzerland = 'German'
print(language_spain is language_switzerland)

# 2.
religion_spain = 'Catholic'
religion_switzerland = 'Catholic'
print(religion_spain is religion_switzerland)

# 3.
capital_spain = 'Madrid'
capital_switzerland = 'Bern'
print(len(capital_spain) != len(capital_switzerland))

# 4.
gdp_spain = 1778000000000000
gdp_switzerland = 580000000000
print(gdp_switzerland > gdp_spain)

# 5.
population_growth_spain = 0.67
population_growth_switzerland = 0.66
print(population_growth_spain and population_growth_switzerland < 1)

# 6.
population_spain = 50000000
population_switzerland = 8400000
print(population_spain > 10000000 or population_switzerland > 10000000)

# 7.
print(not population_switzerland or population_spain > 10000000)