import os
from typing import Dict, List
from bigcommerce0_2 import*
from oxatis0_2 import*
import pandas as pd

def wrapperFromOxatisToBigCommerce():

    colonne = ["ItemSKU", "Name", "Description", "LongDescription", "QtyInStock", "TaxRate", "Price1VATIncluded",
               "Category1Name", "Category2Name", "ShipPrice", "BrandName", "MetaTitle", "MetaDescription",
               "ItemCondition", "EANCode", "UnitsForSale", "ProductLanguage", "MPN", "Visible", "Facets",
               "1ere image zoom", "TaxCountryISOCode", "RelatedItems", "TaxClassName"]
    df = pd.DataFrame(columns=colonne)

    df.to_csv('import oxatis.csv', sep=';', index=False)
    os.startfile('import oxatis.csv')
    input("Press Enter to continue(WARNING: it's important that you save and close the Excel file before you continue)\t")
    aureliacar = readOxatisCSV("import oxatis.csv")
    bigcommerce = FromOxatisToBigCommerce(aureliacar)
    writeBigCommerceCSV("import bigcommerce.csv", bigcommerce)
    os.startfile('import bigcommerce.csv')
    print("Your file has been created successfully")


def FromOxatisToBigCommerce(aureliacar: List[ArticoloAureliaCar]):
    """This method can beh modified for match different categories from tho website"""
    bigcommerce = []
    for articolo in aureliacar:
        bigcommerce.append(ArticoloBigCommerce(articolo.Name, articolo.SKU, articolo.Brand, articolo.LongDescription, articolo.price, peso , categoria ,articolo.URL ,articolo.MetaTitle, articolo.MetaDescription, articolo.mpn, articolo.EANCode,articolo.Qty))
    return bigcommerce

