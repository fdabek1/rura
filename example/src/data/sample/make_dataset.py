from rura.pipeline.dataset import Dataset
import pandas as pd
import numpy as np
import datetime
import random


class MakeDataset(Dataset):
    def __init__(self, num_patients=1000, **kwargs):
        super().__init__(version=1, files={
            'mapping_diagnoses': 'csv',
            'mapping_procedures': 'csv',
            'train': 'feather',
            'val': 'feather',
            'test': 'feather',
        }, **kwargs)

        self.num_patients = num_patients

    @staticmethod
    def generate_diagnoses(num_encounters, den=20):
        return [random.randint(0, 4) if random.randint(0, den) != 1 else np.nan
                for _ in range(num_encounters)]

    def generate_patient(self, patient_id):
        num_encounters = random.randint(2, 8)
        output = random.randint(0, 1)
        start_date = datetime.date(2017, 1, 25)
        dates = [start_date + datetime.timedelta(random.randint(1, 365)) for _ in range(num_encounters)]
        max_date = max(dates)

        age = random.randint(20, 40)
        gender = random.choice(['M', 'F'])

        return pd.DataFrame({
            'PatientID': [patient_id] * num_encounters,
            'PatientAge': [age] * num_encounters,
            'PatientGender': [gender] * num_encounters,
            'EncounterDate': dates,
            'PredictionDate': [max_date] * num_encounters,
            'Output': [output] * num_encounters,
            'Diagnosis1': self.generate_diagnoses(num_encounters, 50),
            'Diagnosis2': self.generate_diagnoses(num_encounters, 15),
            'Diagnosis3': self.generate_diagnoses(num_encounters, 10),
            'Procedure1': self.generate_diagnoses(num_encounters, 10),
            'Procedure2': self.generate_diagnoses(num_encounters, 10),
            'Procedure3': self.generate_diagnoses(num_encounters, 10),
        })

    def make(self):
        diagnoses = pd.DataFrame({
            'ID': [0, 1, 2, 3, 4],
            'Diagnosis': ['34612', 'R51', 'H93239', 'H9190', '38920']
        })

        procedures = pd.DataFrame({
            'ID': [0, 1, 2, 3, 4],
            'Procedure': ['00322', '3601', 'G9194', '0126', '0016077']
        })

        df = pd.concat([self.generate_patient(i + 1) for i in range(self.num_patients)])
        i = self.num_patients + 1
        while df['PatientID'].nunique() < self.num_patients:
            df = pd.concat([df, self.generate_patient(i)])
            i += 1

        df['mTBIDays'] = (df['PredictionDate'] - df['EncounterDate']).dt.days

        df = df.sort_values(['PatientID', 'EncounterDate'])

        diagnoses.to_csv(self.get_path('mapping_diagnoses'), index=False)
        procedures.to_csv(self.get_path('mapping_procedures'), index=False)

        return df
