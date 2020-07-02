from rura.logic.runner import Runner

if __name__ == '__main__':
    runner = Runner('sample.yaml', analysis='sample')
    runner.clean_pipeline('simple')
    runner.execute_pipeline('simple', until=2)
    runner.execute_pipeline('simple')
