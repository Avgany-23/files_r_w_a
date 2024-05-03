import codecs


files = ('1.txt', '2.txt', '3.txt')
info = []
for file in files:
    with codecs.open(file, 'r', 'utf') as f:
        info_file = [element for element in f.readlines()]
        info.append([f"\n{file}", len(info_file), info_file])
info = sorted(info, key=lambda x: x[1])
info[0][0] = info[0][0][1:]

with codecs.open('result_4.txt', 'a', 'utf') as f:
    for inf in info:
        f.write(f'{inf[0]}\n'), f.write(f'{inf[1]}\n')
        file_append_text = [f.write(el) for el in inf[2]]
