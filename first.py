# import pprint


# def main():

#     print("GUIDE >> Data [input_example]: <write input> ")

#     print()
#     # Mendapatkan input dari user
#     uName = input('Name [Bambang]: ')
#     uAdd = input('Address [60 Sudirman]: ')

#     # Hasil berupa array yg di-split berdasarkan ','
#     uHobb = input('Hobbies [Read, Swim, Sing, ...]: ').split(',')
#     uMar = input('Married [False]: ')

#     # String tidak bisa diubah langsung menjadi boolen dengan
#     # bool(str), sehingga dibuat if statements dengan return boolean
#     if uMar.lower() == "true":
#         uMar = True
#     if uMar.lower() == "false":
#         uMar = False

#     uHSchool = input('High School [SMAN 1]: ')
#     uUniv = input('University [Universitas Indonesia]: ')

#     # Hasil berupa Array/List e.g ['Pyhon=Intermediete', ..]
#     # yang nantinya tiap element dr array/list tersebut akan di-split
#     # lagi berdasarkan '=' di dalam function get_json_formet
#     uSkills = input(
#         'Skills [Python=Intermediete, JS=Beginner, ...]: ').split(',')

#     print()

#     # Hasil input user menjadi operand bagi function get_json_format
#     pprint.pprint(get_json_format(uName, uAdd, uHobb,
#                                   uMar, uHSchool, uUniv, uSkills))

#     return


# def get_json_format(name, address, hobbies, marital, hschool, univ, skills):
#     bio = [{'name': name.strip(),
#             'address': address.strip(),

#             # Menggunakan list comprehension untuk mempersingkat
#             'hobbies': [hobby.strip() for hobby in hobbies],
#             'is_married': marital,
#             'school': {'highSchool': hschool.strip(), 'university': univ.strip()},

#             # skills di-split berdasarkan '=' lalu dijadikan key dan value
#             'skills': [{s[0].strip(): s[1].strip()} for s in [skill.split('=') for skill in skills]]
#             }]

#     return bio


# if __name__ == '__main__':
#     main()

import json
import pprint

bio = {
    'name': 'Rizqullah Taufanriansyah',
    'age': 21,
    'address': 'Ahmad Yani 60, Kota Bogor',
    'hobbies': ['Reading', 'Coding', 'Learning'],
    'is_married': False,
    'list_school': [
        {
            'name': 'SMAN 2 Bogor',
            'year_in': 2013,
            'year_out': 2016,
            'major': 'IPA',
        },
        {
            'name': 'Universitas Bakrie',
            'year_in': 2017,
            'year_out': 2021,
            'major': 'Informatics',
        }
    ],
    'skills': [
        {
            'skill_name': 'English',
            'level': 'Advanced',
        },
        {
            'skill_name': 'Python',
            'level': 'Advanced'
        }
    ],
    'interest_in_coding': True,
}


def get_json_format(dic):
    return json.dumps(dic)


pprint.pprint(get_json_format(bio))
