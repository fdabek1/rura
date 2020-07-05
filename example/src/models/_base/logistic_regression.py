from sklearn.linear_model import LogisticRegression
from rura.pipeline import Model
import mlflow.sklearn
import mlflow
from joblib import dump, load


class LogReg(Model):
    # noinspection PyPep8Naming
    def __init__(self, penalty='l2', C=1.0, class_weight=None, solver='liblinear', max_iter=100, l1_ratio=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.penalty = penalty
        self.C = C
        self.class_weight = class_weight
        self.solver = solver
        self.max_iter = max_iter
        self.l1_ratio = l1_ratio

        if self.penalty == 'elasticnet':
            self.solver = 'saga'

    def load(self):
        self.model = load(self.get_path('model.joblib'))

    def build(self):
        self.model = LogisticRegression(penalty=self.penalty, C=self.C, class_weight=self.class_weight,
                                        solver=self.solver, max_iter=self.max_iter, l1_ratio=self.l1_ratio)

    def log_parameters(self):
        mlflow.log_params({
            'penalty': self.penalty,
            'C': self.C,
            'class_weight': self.class_weight,
            'solver': self.solver,
            'max_iter': self.max_iter,
        })

    def fit(self, x, y, x_val=None, y_val=None):
        self.model.fit(x, y)

    def fit_metrics(self, x, y, x_val=None, y_val=None):
        mlflow.log_metric('train_score', self.model.score(x, y))
        mlflow.log_metric('val_score', self.model.score(x_val, y_val))

    def log_model(self):
        dump(self.model, self.get_path('model.joblib'))
        mlflow.sklearn.log_model(self.model, 'model')

    def predict(self, x, data_type=None):
        return self.model.predict(x).astype(int)
