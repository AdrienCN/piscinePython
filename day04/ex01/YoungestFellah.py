def youngestfellah(df, year):
    try:
        sub_df = df[['Sex', 'Age', 'Year']]
        res = sub_df.loc[sub_df['Year'] == year]
        male_min = res.loc[res['Sex'] == 'M'].min()
        female_min = res.loc[res['Sex'] == 'F'].min()
        return ({'f': female_min.Age, 'm': male_min.Age})
    except Exception as msg:
        print(msg)
        return None
