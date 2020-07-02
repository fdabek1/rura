from rura.logic.runner import Runner

if __name__ == '__main__':
    runner = Runner('sample.yaml', analysis='sample')
    runner.clean_dataset('raw')
    runner.clean_dataset('a')
    runner.clean_dataset('b')
    runner.clean_pipeline('simple')
    runner.execute_pipeline('simple', until=1)
    # runner.execute_pipeline('simple')
