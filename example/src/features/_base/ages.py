from rura.pipeline import Transform


class Ages(Transform):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def transform(self, data, data_type):
        data = data.drop_duplicates('PatientID')
        data = data['PatientAge'].values
        return data.reshape((-1, 1)), data > 30
