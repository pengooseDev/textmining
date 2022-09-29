from konlpy.tag import Okt

sentence = '''절망의 반대가 희망은 아니다.
어두운 밤하늘에 별이 빛나듯
희망은 절망 속에 싹트는 거지
만약에 우리가 희망함이 적다면
그 누가 세상을 비출어줄까.
정희성, 희망 공부'''
t = Okt()
print('형태소:', t.morphs(sentence))
print()
print('명사:', t.nouns(sentence)) #조사
print()
print('품사 태깅 결과:', t.pos(sentence))
