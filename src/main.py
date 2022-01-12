import pandas as pd
import numpy as np


def main():
    df_titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    mean_age = df_titanic['Age'].mean()

    df_titanic['Age'] = np.where(df_titanic['Age'].isna(), mean_age, df_titanic['Age'])

    print(df_titanic.head())


if __name__ == '__main__':
    main()
