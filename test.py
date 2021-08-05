import pandas as pd

#  Skill::updateOrCreate(['en_US' => 'Hà Nội, Việt Nam','ja_JP' => '設計']);

df = pd.read_excel (r'worldcities.xlsx')
city = df["city_ascii"]
country = df["country"]
raw_name_en = []
name_en = []

for i in range(0, len(city)):
  raw_name_en.append(", ".join([city[i], country[i]]))
  name_en.append("".join(["Skill::updateOrCreate(['en_US' => '",raw_name_en[i],"','ja_JP' => '設計']);"]))

with open('test.txt', 'w') as f:
  f.write("\n".join(name_en))

