def youngestfellah(df, year):
    sample = df[['Sex', 'Age', 'Year']]
    print(sample)
    res = sample.loc[sample['Year'] == 200]
    print("Res: ", res)
    index = df.columns.get_indexer(['Year'])
    print("Index : ", index)
    #res = sample.get_value(9, year, True)
    #print("Res: ", res)
    
