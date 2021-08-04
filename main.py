import json

from pygal.maps.world import World


from country_codes import get_country_code

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

#load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#build a dictionary of population data
cc_population = {}


#print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

#Group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World population in 2010, by country'
wm.add('0-10 mil', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_in_browser()
