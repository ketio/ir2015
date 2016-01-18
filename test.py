#coding=UTF-8

import jieba

import jieba.posseg as pseg
jieba.set_dictionary('dict.txt.big')

test_str = "妙蛙種子與火球鼠和傑尼龜"
words = pseg.cut(test_str)
for word, flag in words:
    print('%s %s' % (word, flag))
print(test_str)


seg_list = jieba.cut(test_str, cut_all=True)
seg_list2 = jieba.cut(test_str, cut_all=False)
print("/ ".join(seg_list))  # 全模式
print("/ ".join(seg_list2))  # 全模式

print(test_str)

# seg_list = jieba.cut(test_str, cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut(test_str)  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search(test_str)  # 搜索引擎模式
# print(", ".join(seg_list))

