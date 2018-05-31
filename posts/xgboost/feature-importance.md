# Show feature importance


```
# reference: https://www.kaggle.com/mmueller/xgb-feature-importance-python/code

name = 'model_name'
bst = xgb.Booster(model_file = './models/{}.model'.format(name))


importance = bst.get_fscore(fmap='featmap.txt')
importance = sorted(importance.items(), key=operator.itemgetter(1))

df = pd.DataFrame(importance, columns=['feature', 'fscore'])
df['fscore'] = df['fscore'] / df['fscore'].sum()

plt.figure()
df.plot()
df.plot(kind='barh', x='feature', y='fscore', legend=False, figsize=(60, 100))
plt.title('XGBoost Feature Importance')
plt.xlabel('relative importance')
plt.gcf().savefig('{}_feature_importance_xgb.png'.format(name))
```
