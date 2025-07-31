import json

net_company_count = {}
district_count = {}


with open('food_services.json', 'r', encoding='utf-8') as file:
    foods = json.load(file)

for food in foods:
    district = food['District']
    if district not in district_count:
        district_count[district] = 1
    else:
        district_count[district] += 1

    is_net_object = food['IsNetObject']
    if is_net_object == 'да':
        operating_company = food['OperatingCompany']
        if operating_company not in net_company_count:
            net_company_count[operating_company] = 1
        else:
            net_company_count[operating_company] += 1

max_district = max(district_count.items(), key=lambda x: x[1])
max_net = max(net_company_count.items(), key=lambda x: x[1])


print(f"{max_district[0]}: {max_district[1]}")
print(f"{max_net[0]}: {max_net[1]}")

