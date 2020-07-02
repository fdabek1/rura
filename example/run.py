from rura.logic.runner import Runner

if __name__ == '__main__':
    runner = Runner('sample.yaml', analysis='sample')
    runner.execute_pipeline('simple')
