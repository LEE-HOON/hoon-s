# 건강 보험의 가격을 예측해보자

## 요약
* 수업시간에 진행했던 prediction_util 라이브러리를 활용
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
<pre><code>gildong.show_unique_column()
</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D.PNG)

## 데이터 표현하기
나이와 성별 그리고 bmi 자녀수, 가격을 heatmap.
<pre><code>gildong.heatmap(['age','sex','bmi','children','charges'])</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/%ED%9E%88%ED%8A%B8%EB%A7%B5.PNG)

나이와 가격에 대한 boxplot.
<pre><code>gildong.boxplot('age', 'charges')</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/boxplot.png)

나이와 bmi와 가격에 대한 3d plot.
<pre><code>gildong.plot_3d('age', 'bmi', 'charges')</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/3d.png)

## 데이터 학습 및 예측
linear_regress, kneighbor_regress 학습
<pre><code>gildong.run_linear_regress(['age', 'bmi', 'children'], 'charges')</pre></code>
<pre><code>gildong.run_kneighbor_regress(['age', 'bmi', 'children'], 'charges')</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/LR_K-NR.PNG)

decision tree, random_forest 학습
<pre><code>gildong.run_decision_tree(['age', 'bmi', 'children'], 'charges')</pre></code>
<pre><code>gildong.run_random_forest(['age', 'bmi', 'children'], 'charges')</pre></code>
![](https://github.com/LEE-HOON/hoon-s/blob/master/DT_RANDOM.PNG)
