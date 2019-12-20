# 건강 보험의 가격을 예측해보자

## 요약
* 건강 보험에 드는 나이, 성별, BMI 등 데이터를 받아들인다
* 데이터를 받아들여 데이터를 분석한다.
* 학습시키고 건강 보험의 가격을 예측한다.

데이터 출처 : <https://www.kaggle.com/annetxu/health-insurance-cost-prediction>

## 데이터 불러오기
<pre><code>from prediction_util import PredictionUtil
gildong = PredictionUtil()
gildong.read('insurance.csv')
</pre></code>


## 데이터 분석
나이와 성별 그리고 bmi 자녀수, 가격을 heatmap.
![Alt text](C:\Users\nakyu\Desktop\히트맵.jpg)

나이와 가격에 대한 boxplot.
![Alt text](C:\Users\nakyu\Desktop\boxplot.jpg)

나이와 bmi와 가격에 대한 3d plot.
![Alt text](C:\Users\nakyu\Desktop\3d.jpg)

##데이터 학습 및 예측

