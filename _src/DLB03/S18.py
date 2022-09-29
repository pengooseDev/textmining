from konlpy.corpus import kolaw

const_doc = kolaw.open('constitution.txt').read()

print(type(const_doc))  # 가져온 데이터의 type을 확인
print(len(const_doc))
print(const_doc[:600])
