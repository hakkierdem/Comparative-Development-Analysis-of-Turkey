import pandas as pd
import glob

keyword_translations = {
    "Turkey": {"konser": "concert", "sinema": "cinema", "müze": "museum", "kitap": "book", "tiyatro": "theater"},
    "Germany": {"Konzert": "concert", "Kino": "cinema", "Museum": "museum", "Buch": "book", "Theater": "theater"},
    "Japan": {"コンサート": "concert", "映画館": "cinema", "博物館": "museum", "書籍": "book", "劇場": "theater"},
    "Brazil": {"concerto": "concert", "cinema": "cinema", "museu": "museum", "livro": "book", "teatro": "theater"},
    "Poland": {"koncert": "concert", "kino": "cinema", "muzeum": "museum", "książka": "book", "teatr": "theater"},
    "Sweden": {"konsert": "concert", "bio": "cinema", "museum": "museum", "bok": "book", "teater": "theater"},
    "South Korea": {"콘서트": "concert", "영화": "cinema", "박물관": "museum", "책": "book", "연극": "theater"},
    "Canada": {"Concert": "concert", "Cinéma": "cinema", "Musée": "museum", "Livre": "book", "Théâtre": "theater"},
    "United Kingdom": {"Concert": "concert", "Cinema": "cinema", "Museum": "museum", "Book": "book", "Theatre": "theater"},
    "Jordan": {"حفلة موسيقية": "concert", "سينما": "cinema", "متحف": "museum", "كتاب": "book", "مسرح": "theater"},
    "Malaysia": {"Konsert": "concert", "Panggung wayang": "cinema", "Muzium": "museum", "Buku": "book", "Teater": "theater"}
}


file_to_country = {
    "Türkiye.csv": "Turkey",
    "Germany.csv": "Germany",
    "Japan.csv": "Japan",
    "Canada.csv": "Canada",
    "Brazil.csv": "Brazil",
    "Malaysia.csv": "Malaysia",
    "Jordan.csv": "Jordan",
    "UnitedKingdom.csv": "United Kingdom",
    "SouthKorea.csv": "South Korea",
    "Sweden.csv": "Sweden",
    "Poland.csv": "Poland"
    
}

dfs = []
for file in glob.glob("*.csv"):

    country = None
    for f, c in file_to_country.items():
        if f.lower() in file.lower():
            country = c
            break
    
    if not country:
        print(f"Uyarı: {file} için ülke bulunamadı, atlanıyor...")
        continue
    
    try:
        df = pd.read_csv(file, skiprows=1)
        df.columns = [col.split(":")[0].strip() for col in df.columns]
        

        rename_dict = {k: v for k, v in keyword_translations[country].items() if k in df.columns}
        df.rename(columns=rename_dict, inplace=True)
        
        df["Country"] = country
        df.rename(columns={df.columns[0]: "Date"}, inplace=True)
        dfs.append(df)
    except Exception as e:
        print(f"Hata: {file} işlenirken - {str(e)}")

if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    final_df["Date"] = pd.to_datetime(final_df["Date"])
    print("Eksik veri sayısı:\n", final_df.isnull().sum())
    final_df.to_csv("global_cultural_trends.csv", index=False)
    print("Başarıyla kaydedildi!")
else:
    print("İşlenecek veri bulunamadı!")
