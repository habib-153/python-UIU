upozilla_map = {

    "Dighinata": ["Panchari", "Khagrachari"],

    "Panchari": ["Dighinata", "Khagrachori", "Mati Ranga"],

    "Mati Ranga": ["Panchari", "Khagrachari", "Ramgarh"],

    "Ramgarh": ["Mati Ranga", "Khagrachari", "Mohal Chari", "Lakshmichari", "Manikchari"],

    "Mohal Chari": ["Khagrachari", "Lakshmichari", "Ramgarh"],

    "Lakshmichari": ["Mohal Chari", "Manikchari", "Ramgarh"],

    "Manikchari": ["Lakshmichari", "Ramgarh"],

    "Khagrachari": ["Dighinata", "Panchari", "Mati Ranga", "Ramgarh", "Mohalchari"]

}

maximum = max(len(values) for values in upozilla_map.values())

for key,value in upozilla_map.items():
    if len(value) == maximum:
        print(key)
print(maximum)