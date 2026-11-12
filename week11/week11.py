path = "A2_1_W_X"
factory = path[0:2]
path = path[3:]
print(factory, path)
path = path.split("_")  # 구분기호 기준으로 문자열을 분리하고 분리된 원소들을 리스트에 담아 리턴
print(path)