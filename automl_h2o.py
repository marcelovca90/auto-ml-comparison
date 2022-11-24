from h2o.sklearn import H2OAutoMLClassifier

from common import (DATASET_FOLDER, EXEC_TIME_MINUTES, EXEC_TIME_SECONDS, SEED,
                    TIMER, collect_and_persist_results, load_data_delegate)

try:

    X_train, X_test, y_train, y_test = load_data_delegate()

    clf = H2OAutoMLClassifier(max_runtime_secs=EXEC_TIME_SECONDS, nfolds=5, seed=SEED, sort_metric='accuracy')

    TIMER.tic()
    clf.fit(X_train, y_train)
    training_time = TIMER.tocvalue()

    TIMER.tic()
    y_pred = clf.predict(X_test)
    test_time = TIMER.tocvalue()

    collect_and_persist_results(y_test, y_pred, training_time, test_time, "h2o")

except Exception as e:
    print(f'Cannot run h2o for dataset {DATASET_FOLDER}. Reason: {str(e)}')
