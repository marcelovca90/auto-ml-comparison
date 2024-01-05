from tpot import TPOTClassifier

from common import *

if __name__ == "__main__":

    for SEED in PRIME_NUMBERS:
        
        try:

            set_random_seed(SEED)
                
            X_train, X_test, y_train, y_test = load_data_delegate(SEED)

            clf = TPOTClassifier(
                max_time_mins=EXEC_TIME_MINUTES, 
                max_eval_time_mins=EXEC_TIME_MINUTES//10, 
                cv=5, 
                n_jobs=NUM_CPUS,
                random_state=SEED
            )

            TIMER.tic()
            clf.fit(X_train, y_train)
            training_time = TIMER.tocvalue()

            TIMER.tic()
            y_pred = clf.predict(X_test)
            test_time = TIMER.tocvalue()

            collect_and_persist_results(y_test, y_pred, training_time, test_time, "tpot", SEED)

        except Exception as e:
            print(f'Cannot run tpot for dataset {get_dataset_ref()} (seed={SEED}). Reason: {str(e)}')
