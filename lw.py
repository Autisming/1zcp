#��ȡ���ʺ�������
def getTxt():
    txt = open('hamlet.txt').read()
    txt = txt.lower()
    for ch in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}': #�滻�����ַ�
        txt.replace(ch, ' ')
    return txt
#1.��ȡ����
hamletTxt = getTxt()

#2.�и�Ϊ�б��ʽ
txtArr = hamletTxt.split()

#3.����ͳ��
counts = {}
for word in txtArr:
    counts[word] = counts.get(word, 0) + 1

#4.ת����ʽ�������ӡ�����ֵ�ת��Ϊ�б�
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#�������Ӵ�С����

#5.��ӡ
for i in range(10):
    word, count = countsList[i]
    print('{0:<10}{1:>5}'.format(word,count))
