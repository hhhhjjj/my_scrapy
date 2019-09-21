# coding=utf-8
from snownlp import sentiment
sentiment.train(r'E:\analysis_emotion\Lib\site-packages\snownlp\sentiment\negative.txt', r'E:\analysis_emotion\Lib\site-packages\snownlp\sentiment\positive.txt')
sentiment.save(r'E:\analysis_emotion\Lib\site-packages\snownlp\sentiment\sentiment.marshal')
