# 时间：2023/6/15 14:08
# 人员: 莉光哈哈哈
from faker import Faker

fake = Faker(locale='zh_CN')
a = fake.name()
b = fake.job()
c = fake.credit_card_number(card_type=None)
d = fake.phone_number()
print(a, b, c, d)
