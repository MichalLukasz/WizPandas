import pandas as pd


print('zadanie 1\n')
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

print('\nzadanie 2\n')
print(df[df['Liczba'] > 1000])

print(df[df['Imie'] == 'MICHAŁ'])

print(df.agg({'Liczba': ['sum']}))

print(df[(df.Rok < 2006) & (df.Rok > 1999)].agg({'Liczba': ['sum']}))

print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))

new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")

print('chlopiec')
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])

print('dziewczynka')
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
print('\nzadanie 3\n')
df = pd.read_csv("zamowienia.csv", header=0, sep=';', decimal=".")

# lista sprzedawców (bez powtórzeń)
print(df['Sprzedawca'].unique())

# top 5 najdroższych zamównień
print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])

# suma wg sprzedawców
print(df.groupby(['Sprzedawca']).size())

# suma wg krajów
print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))

# suma 2005 PL
print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') &
          (df['Kraj'] == 'Polska'))].agg({'Utarg': ['sum']}))

# średnia kwota 2004
print(df[(df['Data zamowienia'].str[:4] == '2004')]['Utarg'].mean())

# zapisanie danych
rok_2004 = df[(df['Data zamowienia'].str[:4] == '2004')]
rok_2005 = df[(df['Data zamowienia'].str[:4] == '2005')]
rok_2004.to_csv("zamowienia_2004.csv", sep=';', index=False)
rok_2005.to_csv("zamowienia_2005.csv", sep=';', index=False)
