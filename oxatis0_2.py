import pandas as pd


class ArticoloAureliaCar:
    def __init__(self, SKU, Name, Description, LongDescription, Qty, TaxRate, price, category1, category2, ShipPrice,
                 BrandName,
                 MetaTitle, MetaDescription, ItemCondition, EANCode, UnitsForSale, ProductLanguage, MPN, Visibile,
                 Facets, URL, TaxCountry, ReleatedItems, TaxClass):
        self.SKU = SKU
        self.Name = Name
        self.Description = Description
        self.LongDescription = LongDescription
        self.Qty = Qty
        self.TaxRate = TaxRate
        self.price = price
        self.category1 = category1
        self.category2 = category2
        self.ShipPrice = ShipPrice
        self.Brand = BrandName
        self.MetaTitle = MetaTitle
        self.MetaDescription = MetaDescription
        self.ItemCondition = ItemCondition
        self.EANCode = EANCode
        self.UnitsForSale = UnitsForSale
        self.ProductLanguage = ProductLanguage
        self.mpn = MPN
        self.Visibile = Visibile
        self.Facets = Facets
        self.URL = URL
        self.TaxCountry = TaxCountry
        self.ReleatedItems = ReleatedItems
        self.TaxClass = TaxClass
        self.qty = Qty


    def getcategory1(self):
        return self.category1

    def getcategory2(self):
        return self.category2


def readOxatisCSV(file_path):
    required_columns = ["ItemSKU", "Name", "Category1Name", "Category2Name", "MPN"]

    df = pd.read_csv(file_path, sep=";", nrows=0, encoding="ISO-8859-1")

    missed_columns = [col for col in required_columns if col not in df.columns]

    if missed_columns:
        print(
            f"Warning: The following columns are REQUIRED but not present in the file: {', '.join(missed_columns)}")
        return None
    else:
        print(f"All required columns are present. I proceed with reading the file.")

    df = pd.read_csv(file_path, sep=";", encoding="windows-1252")
    articles = []

    for index, row in df.iterrows():
        article = ArticoloAureliaCar(
            SKU=str(row.get("ItemSKU")),
            Name=str(row.get("Name")),
            Description=row.get("Description"),
            LongDescription=row.get("LongDescription"),
            Qty=str(row.get("QtyInStock")),
            TaxRate=str(row.get("TaxRate")),
            price=row.get("Price1VATIncluded"),
            category1=str(row.get("Category1Name")),
            category2=str(row.get("Category2Name")),
            ShipPrice=row.get("ShipPrice"),
            BrandName=row.get("BrandName"),
            MetaTitle=row.get("MetaTitle"),
            MetaDescription=row.get("MetaDescription"),
            ItemCondition=row.get("ItemCondition"),
            EANCode=row.get("EANCode"),
            UnitsForSale=row.get("UnitsForSale"),
            ProductLanguage=row.get("ProductLanguage"),
            MPN=str(row.get("MPN")),
            Visibile=row.get("Visible"),
            Facets=row.get("Facets"),
            URL=row.get("1ere image zoom"),
            TaxCountry=row.get("TaxCountryISOCode"),
            ReleatedItems=row.get("RelatedItems"),
            TaxClass=row.get("TaxClassName")
        )
        articles.append(article)

    return articles
