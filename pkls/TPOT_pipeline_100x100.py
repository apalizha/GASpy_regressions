import numpy as np

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import Binarizer, MinMaxScaler, Normalizer
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = np.recfromcsv('PATH/TO/DATA/FILE', delimiter='COLUMN_SEPARATOR', dtype=np.float64)
features = np.delete(tpot_data.view(np.float64).reshape(tpot_data.size, -1), tpot_data.dtype.names.index('class'), axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data['class'], random_state=42)

exported_pipeline = make_pipeline(
    make_union(
        make_pipeline(
            MinMaxScaler(),
            Normalizer()
        ),
        Binarizer(threshold=0.95)
    ),
    GradientBoostingRegressor(learning_rate=0.1, loss="huber", max_depth=8, max_features=0.1, min_samples_leaf=2, min_samples_split=10, n_estimators=100, subsample=0.95)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
