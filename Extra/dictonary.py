# without repeat values
# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }

# for language in set(favorite_languages.values()):
#     print(language)
# ============================================
# nested
course = [
    {
        'title': 'DS 1501',
        'credit': 3
    },
    {
        'instructor': 'Dr. Saddam',
        'duration': 1.2
    },
    {
        'book': 'python crash course',
        'pages': 84
    }
]

# print(len(course))
# print(course[0].keys())
# print(course[0].values())

# update value
# course[0]['title'] = 'DS 151'
# print(course[0])
# Append
# camp={'campus':'UIU', 'time':'1.51PM'}
# course.append(camp)
# print(course)
# Insert
# course.insert(1, {'trimester':'spring2023','classMode':'hybrid'})
# print(course)

# delete
# del course[1]['classMode']
# print(course)

# course[0]['course_name']=course[0].pop('title')
# print(course)

# ========================================================

    # tracks = {
    #     "software": ["Project management", "SystemAnalysis", "Software Engg", "Web programming"],
    #     "iot": ["Cloud computing", "Green computing",
    #             "robotics", "Sensor network"],
    #     "hardware": ["Computer Architecture", "DLD",
    #                  "Microprocessor and Microcontroller",
    #                  "Interfacing"]
    # }

    # for key, val in tracks.items():
    #     for i in val:
    #         print(f"{key} : {i}")

    # print(tracks["software"][1:3])