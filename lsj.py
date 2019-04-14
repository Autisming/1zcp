# ������չ��
import re # ������ʽ��
import collections # ��Ƶͳ�ƿ�
import numpy as np # numpy���ݴ����
import jieba # ��ͷִ�
import wordcloud # ����չʾ��
from PIL import Image # ͼ�����
import matplotlib.pyplot as plt # ͼ��չʾ��

# ��ȡ�ļ�
fn = open('a.txt') # ���ļ�
string_data = fn.read() # ���������ļ�
fn.close() # �ر��ļ�

# �ı�Ԥ����
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
string_data = re.sub(pattern, '', string_data)

# �ı��ִ�
seg_list_exact = jieba.cut(string_data, cut_all = False) 
object_list = []
remove_words = [u'��', u'��',u'��', u'��', u'����', u'����', u'��',u'��',u'��',u'��',u'��',u' ',u'��',u'��',u'��',u'��',
                u'ͨ��',u'���',u'����',u'��Ҫ'] 

for word in seg_list_exact: 
    if word not in remove_words: 
        object_list.append(word) 

# ��Ƶͳ��
word_counts = collections.Counter(object_list) 
word_counts_top10 = word_counts.most_common(10) 
print (word_counts_top10) # ������

# ��Ƶչʾ
mask = np.array(Image.open('wordcloud.jpg')) # �����Ƶ����
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # ���������ʽ
    mask=mask, # ���ñ���ͼ
    max_words=200, # �����ʾ����
    max_font_size=100 # �������ֵ
)

wc.generate_from_frequencies(word_counts) 
image_colors = wordcloud.ImageColorGenerator(mask) 
wc.recolor(color_func=image_colors) 
plt.imshow(wc) # ��ʾ����
plt.axis('off') # �ر�������
plt.show() # ��ʾͼ��
