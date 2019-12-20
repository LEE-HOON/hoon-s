from prediction_util import PredictionUtil
gildong = PredictionUtil()
gildong.read('insurance.csv')
gildong.show_unique_column()

gildong.heatmap(['age','sex','bmi','children','charges'])
gildong.boxplot('age', 'charges')
gildong.plot_3d('age', 'bmi', 'charges')gildong.run_linear_regress(['age', 'bmi', 'children'], 'charges')

gildong.run_all(['age', 'bmi', 'children'], 'charges')
