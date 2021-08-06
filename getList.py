import pandas as pd

#  Skill::updateOrCreate(['en_US' => 'Hà Nội, Việt Nam','ja_JP' => '設計']);

df = pd.read_excel (r'worldcities.xlsx')
city = df["city_ascii"]
country = df["country"]
raw_name_en = []
raw_name_jp = []
name = []

with open('raw_en_ja.txt', 'r') as f:
    raw_name_jp = f.readlines()

raw_name_jp = [x.strip() for x in raw_name_jp] 

for i in range(0, len(city)):
  raw_name_en.append(", ".join([city[i], country[i]]))
  name.append("".join(["Skill::updateOrCreate(['en_US' => '",raw_name_en[i],"','ja_JP' => '",raw_name_jp[i],"']);"]))

with open('list.txt', 'w') as f:
  f.write("\n".join(name))

# with open('raw.txt', 'w') as f:
#   f.write('\n'.join(raw_name_en))




