# Travel log,  which is simply the cities visited by a person in a country
travel_log_simple={'France':'Paris','India':'Mumbai'}
travel_log_nested={'France':['Paris','Lille','Lyon'], 'India':['Mumbai','New Delhi','Kolkata']}

# lets build a dictionary inside a dictionary,  say we need to keep the no of visits to each country

travel_log={'France':['Paris','Lille','Lyon'], 'India':['Mumbai','New Delhi','Kolkata']}

cities_visited={}
for key in travel_log:
    cities_visited[key]=2
print(cities_visited)
print(travel_log)
