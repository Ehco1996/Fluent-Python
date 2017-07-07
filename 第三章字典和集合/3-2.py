'''
字典推导的应用
'''

DIAL_CODE = [
    (86, 'China'),
    (91, 'India'),
    (7, 'Russia'),
    (81, 'Japan'),
]

# 利用字典推导快速生成字典
country_code = {country: code for code, country in DIAL_CODE}
print(country_code)

# 将区域码最为键，国家名作为值，并过滤掉区域码大于等于86的国家：
country_code_1 = {code: country for code, country in DIAL_CODE if code < 86}
print(country_code_1)

'''
OUT:
{'China': 86, 'India': 91, 'Russia': 7, 'Japan': 81}

{7: 'Russia', 81: 'Japan'}
'''
