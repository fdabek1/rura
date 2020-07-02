from rura.pipeline import Transform


class Outputs(Transform):
    def __init__(self, **kwargs):
        super().__init__(has_y=False, **kwargs)

    def transform(self, data, data_type):
        model = self.sources[1]
        return model.predict(data)
