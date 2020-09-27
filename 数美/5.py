def func(strs, labels):
    assert len(strs) == len(labels)
    ls = len(strs)
    keys = []
    chuans = []
    key = ''
    chuan = ''
    key_flag = False
    chuan_flag = False
    for index, (c, label) in enumerate(zip(strs, labels)):
        if label == 0:
            if key_flag and key != '':
                keys.append(key)
                key = ''
                key_flag = False
            if chuan_flag and chuan != '':
                chuans.append(chuan)
                chuan = ''
                chuan_flag = False
            continue
        elif label == 1:
            key_flag = True
            key += c
        elif label == 2:
            key += c
        elif label == 3:
            chuan_flag = True
            chuan += c
        elif label == 4:
            chuan += c
    if chuan != '':
        chuans.append(chuan)
    if key != '':
        keys.append(key)
    print(keys)
    print(chuans)
str1 = '想知道如果提高王者荣耀水平，上分把妹不是梦，加微信：17252sugats78，加QQ：34676328889'
str2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,1,2,0,3,4,4,4,4,4,4,4,4,4,4]
func(str1, str2)