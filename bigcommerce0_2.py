import csv
class ArticoloBigCommerce:
    def __init__(self, ProductName, SKU, Brand, ProductDescription, Price, Weight,
                 Category, URL, metaTile, metaDesc, MPN, EAN, Qty):
        self.ItemType = "Product"
        self.ProductId = ''
        self.ProductName = ProductName
        self.ProductType = "Physical"
        self.SKU = SKU
        self.Brand = Brand
        self.ProductDescription = ProductDescription
        self.Price = Price
        self.Weight = Weight
        self.Visible = False
        self.Stock = Qty
        self.LowStock = 5
        self.Category = Category
        self.URL = URL
        self.metaTile = metaTile
        self.metaDesc = metaDesc
        self.Condition = "New"
        self.showCondition = ""
        self.ProductTaxClass = "Default Tax Class"
        self.EAN = EAN
        self.MPN = MPN
        self.allowPurchase = True

    def getSKU(self):
        return self.SKU

    def setPrice(self, param):
        self.Price = param

    def getMPN(self):
        return self.MPN

    def getPrice(self):
        return self.Price


def writeBigCommerceCSV(file_path, articoli):
    """Write the CSV file for BigCommerce"""
    columns = [
        "Item Type", "Product ID", "Product Name", "Product Type", "Product Code/SKU", "Bin Picking Number",
        "Brand Name", "Option Set", "Option Set Align", "Product Description", "Price", "Free Shipping", "Product Warranty", "Product Weight",
        "Product Width", "Product Height", "Product Depth", "Allow Purchases?", "Product Visible?",
        "Product Availability", "Track Inventory", "Current Stock Level", "Low Stock Level", "Category",
        "Product Image ID - 1", "Page Title", "Meta Description", "Product Condition", "Show Product Condition?",
        "Product Tax Class", "Product UPC/EAN", "Stop Processing Rules", "Product URL", "Redirect Old URL?",
        "Global Trade Item Number", "Manufacturer Part Number"
    ]
    with open(file_path, mode='w', newline='', encoding="ISO-8859-1") as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')

        # Scrive l'intestazione
        writer.writeheader()

        # Itera su ogni articolo e scrive i dati nel CSV
        for articolo in articoli:
            writer.writerow({
                "Item Type": articolo.ItemType,
                "Product ID": articolo.ProductId,
                "Product Name": articolo.ProductName,
                "Product Type": articolo.ProductType,
                "Product Code/SKU": articolo.SKU,
                "Bin Picking Number": '',
                "Brand Name": articolo.Brand,
                "Option Set": '',
                "Option Set Align": '',
                "Product Description": articolo.ProductDescription,
                "Price": articolo.Price,
                "Free Shipping": '',
                "Product Warranty": '',
                "Product Weight": articolo.Weight,
                "Product Width": '',
                "Product Height": '',
                "Product Depth": '',
                "Allow Purchases?": articolo.allowPurchase,
                "Product Visible?": articolo.Visible,
                "Product Availability": '',
                "Track Inventory": "by product",
                "Current Stock Level": articolo.Stock,
                "Low Stock Level": articolo.LowStock,
                "Category": articolo.Category,
                "Product Image ID - 1": articolo.URL,
                "Page Title": articolo.metaTile,
                "Meta Description": articolo.metaDesc,
                "Product Condition": articolo.Condition,
                "Show Product Condition?": articolo.showCondition,
                "Product Tax Class": articolo.ProductTaxClass,
                "Product UPC/EAN": articolo.EAN,
                "Stop Processing Rules": '',
                "Product URL": '',
                "Redirect Old URL?": '',
                "Global Trade Item Number": '',
                "Manufacturer Part Number": articolo.MPN
            })

def readBigCommerceCSV(file_path):
    article = []
    with open(file_path, mode='r', newline='', encoding="ISO-8859-1") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            article = ArticoloBigCommerce(
                ProductName=row.get("Product Name"),
                SKU=row.get("Product Code/SKU"),
                Brand=row.get("Brand Name"),
                ProductDescription=row.get("Product Description"),
                Price=row.get("Price"),
                Weight=row.get("Product Weight"),
                Category=row.get("Category"),
                URL=row.get("Product Image ID - 1"),
                metaTile=row.get("Page Title"),
                metaDesc=row.get("Meta Description"),
                MPN=row.get("Manufacturer Part Number"),
                EAN = row.get("Product UPC/EAN")
            )
            article.append(article)

    return article
