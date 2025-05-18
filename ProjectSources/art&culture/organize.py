import pandas as pd
import glob


keyword_translations = {
    "Türkiye": {"konser": "concert", "sinema": "cinema", "müze": "museum", "kitap": "book", "tiyatro": "theater"},
    "Germany": {"Konzert": "concert", "Kino": "cinema", "Museum": "museum", "Buch": "book", "Theater": "theater"},
    "Japan": {"コンサート": "concert", "映画館": "cinema", "博物館": "museum", "書籍": "book", "劇場": "theater"},
    "Brazil": {"concerto": "concert", "cinema": "cinema", "museu": "museum", "livro": "book", "teatro": "theater"},
    "Poland": {"koncert": "concert", "kino": "cinema", "muzeum": "museum", "książka": "book", "teatr": "theater"},
    "Egypt": {"حفلة موسيقية": "concert", "سينما": "cinema", "متحف": "museum", "كتاب": "book", "مسرح": "theater"},
    "Usa": {"concert": "concert", "cinema": "cinema", "museum": "museum", "book": "book", "theater": "theater"},
    "India": {"concert": "concert", "cinema": "cinema", "museum": "museum", "book": "book", "theatre": "theater"},
    "Sweden": {"konsert": "concert", "bio": "cinema", "museum": "museum", "bok": "book", "teater": "theater"}
}

dfs = []
for file in glob.glob("*.csv"):

    country = file.split(".")[0].title()  
    

    df = pd.read_csv(file, skiprows=1)
    

    df.columns = [col.split(":")[0].strip() for col in df.columns]
    

    df.rename(columns=keyword_translations[country], inplace=True)
    

    df["Country"] = country
    

    df.rename(columns={df.columns[0]: "Date"}, inplace=True)
    dfs.append(df)


final_df = pd.concat(dfs, ignore_index=True)


final_df["Date"] = pd.to_datetime(final_df["Date"])


print("Eksik veri sayısı:\n", final_df.isnull().sum())


final_df.to_csv("global_cultural_trends.csv", index=False)
print("Tüm ülkelerin verileri birleştirildi ve 'global_cultural_trends.csv' olarak kaydedildi!")
