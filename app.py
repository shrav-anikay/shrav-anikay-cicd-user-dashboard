from flask import Flask, render_template
import pandas as pd
import boto3
import os

app = Flask(__name__)

BUCKET_NAME = 'shravani-cicd-user-dashboard'
FILE_NAME = 'u.user'

def download_dataset():
    s3 = boto3.client('s3')

    if not os.path.exists(FILE_NAME):
        s3.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)

columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']

@app.route('/')
def home():

    download_dataset()

    df = pd.read_csv(
        FILE_NAME,
        sep='|',
        names=columns
    )

    total_users = len(df)

    age_distribution = (
        df['age']
        .value_counts()
        .sort_index()
        .to_dict()
    )

    occupation_group = (
        df['occupation']
        .value_counts()
        .to_dict()
    )

    return render_template(
        'index.html',
        total_users=total_users,
        age_distribution=age_distribution,
        occupation_group=occupation_group
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)