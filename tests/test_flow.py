import unittest
import sys
import os


class FlowTest(unittest.TestCase):

    @staticmethod
    def test_simple():
        os.chdir('../example')
        sys.path.insert(0, os.getcwd())
        from rura.logic.runner import Runner
        runner = Runner('sample.yaml', analysis='sample')
        runner.clean_pipeline('simple')
        runner.execute_pipeline('simple')

        # Dataset files
        raw = os.path.join('data', 'processed', 'sample', 'raw')
        assert os.path.exists(os.path.join(raw, 'mapping_diagnoses.v1.csv'))
        assert os.path.exists(os.path.join(raw, 'mapping_procedures.v1.csv'))
        assert os.path.exists(os.path.join(raw, 'test.v1.feather'))
        assert os.path.exists(os.path.join(raw, 'train.v1.feather'))
        assert os.path.exists(os.path.join(raw, 'val.v1.feather'))

        # Features files
        features = os.path.join('data', 'processed', 'sample', 'simple', '0', '_1')
        assert os.path.exists(os.path.join(features, 'test_x.npy'))
        assert os.path.exists(os.path.join(features, 'test_y.npy'))
        assert os.path.exists(os.path.join(features, 'train_x.npy'))
        assert os.path.exists(os.path.join(features, 'train_y.npy'))
        assert os.path.exists(os.path.join(features, 'val_x.npy'))
        assert os.path.exists(os.path.join(features, 'val_y.npy'))

        # Model files
        model = os.path.join('data', 'processed', 'sample', 'simple', '1', '_1')
        assert os.path.exists(os.path.join(model, 'model.joblib'))
