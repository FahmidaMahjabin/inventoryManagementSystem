import datetime
import random
class Product:
    def __init__(self, name, productid):
        self.name = name
        self.productid = productid 
    def __str__(self):
        return f"name:{self.name}, Id:{self.idnumber}"

class Purchase:
    def __init__(self, productid, quantity, price, date):
        self.productid = productid
        self.quantity = quantity
        self.price = price
        self.date = date

class Sale:
    def __init__(self, productid,quantity, price, date):
        self.productid = productid
        self.quantity = quantity
        self.price = price
        self.date = date
        
    def __str__(self):
        return f"productid : {self.productid}, price : {self.price}, date : {self.date}, quantity : {self.quantity}"

class Inventory:
    def __init__(self):
        self.listOfPurchase = []
        self.listOfSale = []
        self.productList = []
    def addPurchase(self, purchase):
        self.listOfPurchase.append(purchase)
        print(self.listOfPurchase)
        
    def addSale(self, sale):    
        self.listOfSale.append(sale)
    
    def addProduct(self, name, productid):
        theProduct = Product(name, productid)
        self.productList.append(theProduct)
        
#         function- purchase a product
#         1.input = productid, quantity and price per item
#         2.output = purchase the product and add to the purchase list
#         3.take today's date as date
#         4.calculate total price from quantity and price per item
#         5.productid ta productList e ache kina check korbo
#         6.thakle hasProduct = True rakhbo and stop kore dibo
#         6.hasProduct False hole exception raise korbo
#         7.hasProduct True hole purchase korbo and purchaseList e add korbo
#       

    def purchase(self, productid,quantity, pricePerItem):
        today = datetime.datetime.now()
        price = quantity * pricePerItem
        hasProductid = False
        for product in self.productList:
            if productid == product.productid:
                hasProductid = True
                break
        if hasProductid is False:
            raise Exception("product is not in productList")
        if hasProductid is True:
            thePurchase = Purchase(productid, quantity, price, today)
            self.addPurchase(thePurchase)
       
    
    #show purchase list:
#     1.purchaseList = ""
#     2.self.listOfPurchase er sob purchase er productid, quantity, price er string concatinate kore boshabo.
    def showPurchaseList(self):
        purchaseList = ""
        for purchase in self.listOfPurchase:
            purchaseList += purchase.productid + str(purchase.quantity) + str(purchase.price) + "\n"
        return purchaseList
    
    def showSaleList(self):
        saleList = ""
        for sale in self.listOfSale:
            f"saleList += productid:{sale.productid} quantity:{sale.quantity} price: {sale.price}\n"
        print(saleList)

#         showProducts e dictionary of products productid and product quantity show korbe
#         input = self
#         output = dictionary ofproduct
#         1.initialize empty dictionary,dictOfProduct = {}
#         2.
    def getDictOfProductBalance(self):
        dictOfProduct = {}
        for product in  self.productList:
            dictOfProduct[product.name] = self.getBalance(product.productid)
        return dictOfProduct
#     1.self.showProducts():
#         1.self = 008989898
#         2.listOfProduct = {}
#         3.for product in  self.productList:
#         4.for product in 008989898.productList
      
#      1.jei product ta sell korbo tar object theSale banabo
#      2.getBalance function theke oi product er balance theke product er sell quantity subtract korbo
#      3.jodi subtraction >= 0 hoy tahole addSale e add korbo and True return korbo
#      4.else False return korbo
#     exceptions for sale:
#         1.expire date add korte hobe and er cheye sell date kom hote hobe
#         2.purchase price er cheye sell price beshi hote hobe
#         3.product ta purchase list e ase kina dekhte hobe
#         4.quantity purchased quantityr cheye kom hote hobe

#     exceptions in error
#     1.purchase list e product ta ache kina check korte hobe and na thakle exception raise korte hobe
#           1.purchaseList e productid ta ache kina check korte hobe
#           2.initialize hasProduct = False
#           3.jodi productid ta purchaselist e pawa jay then hasProduct = True hobe
#           4.hasProduct False hole product ta list e nai and exception raise korte hobe ("product is not purchased yet")
#     2.purchase quantity sell quantity theke kom hole exception raise korbe
#           1.getBalance() function theke productid diye quantity ber korbo
#           2.check korbo balance quantity beshi kina
#           3.balance quantity beshi hole purchase korbo
#           4.else exception raise korbo("quantity exceeds purchase quantity")     

#     3.quantity or price integer value na diye string value dite pare. ValueError
    
        
    def sell(self, productid,quantity, pricePerItem):
        date = datetime.datetime.now()
        price = quantity * pricePerItem
        if price <= 0:
            raise Exception("price can't be zero or negative")
        if (self.getBalance(productid) >= quantity):
            theSale = Sale(productid, quantity, price, date)
            self.addSale(theSale)
        else:
            raise Exception("quantity exceeds purchase quantity")


#         1.productid input nibo
#         2.oi product er present e  ki quantity ase ta output dibe i.e purchase - sale quantity
#         3.initialize totalQuantity = 0
#         4.productid ta listOfPurchase e ache kina check korbo, thakle totalQuantity te sum korbo oi product er quantity
#         5.productid ta listofSale e ache kina check korbo, thakle totalQuantity theke subtract korbo
#         6.totalQuantity  ta return korbe
    def getBalance(self, productid ):
        totalQuantity = 0
        for purchase in self.listOfPurchase:
            if purchase.productid == productid:
                totalQuantity += purchase.quantity
        for sale in self.listOfSale:
            if sale.productid == productid:
                totalQuantity -= sale.quantity
        return totalQuantity
      
#     function- get average purchase price
#     input = productid
#     output = avg purchase price of that product
#     1.initialize totalprice = 0, totalQuantity = 0
#     1.listOfPurchase e oi productid ta ache kina check korbo
#     2.oi productid ta thakle tar price k totalPrice er sathe sum korbo and quantity k totalQuantity er sathe sum korbo
#     3.if totalPrice = 0 or totalQuantity = 0 then raise exception(product is not purchesed yet)
#     3.avgPurchasePerPrice = totalPrice / totalQuantity
    def getAveragePurchasePrice(self, productid):
        totalPrice = 0
        totalQuantity = 0
        for purchase in self.listOfPurchase:
            if purchase.productid == productid:
                totalPrice += purchase.price
                totalQuantity += purchase.quantity
        if totalPrice == 0 or totalQuantity ==0:
            raise Exception("product is not purchesed yet")
        averagePurchasePrice = totalPrice / totalQuantity
        return averagePurchasePrice
    
#     function - get total purchased quantity
#     input = productid
#     output = purchased quantity of that product
#     1.productid ta listOfPurchase er purchase er productid er moddhe ache kina check korte hobe
#     2.thakle totalPurchasedQuantity = 0 er sathe oita add korte hobe
#     3.totalPurchasedQuantity retturn korbo
    def getPurchasedQuantity(self, productid):
        totalPurchasedQuantity = 0
        for purchase in self.listOfPurchase:
            if purchase.productid == productid:
                totalPurchasedQuantity += purchase.quantity
        return totalPurchasedQuantity
    
    def getSaleQuantity(self, productid):
        totalSaleQuantity = 0
        for sale in self.listOfSale:
            if sale.productid == productid:
                totalSaleQuantity += sale.quantity
        return totalSaleQuantity

    def getAvgSellPrice(self, productid):
        totalPrice = 0
        totalQuantity = 0
        for sale in self.listOfSale:
            if sale.productid == productid:
                totalPrice += sale.price
                totalQuantity += sale.quantity
        if totalPrice == 0 or totalQuantity == 0:
            raise Exception("product is not sold yet")
        averageSalePrice = totalPrice / totalQuantity
        return averageSalePrice
        
#        function- getProfitPerItem
#        input = productid
#        output = netProfit
#        1.get average profit per item
#        2.get total sold quantity of items
#        3.netProfit = averageProfitPerItem * totalSoldQuantity
#        4.return netProfit
        
    def getProfitPerItem(self, productid):
        profitPerItem = self.getAvgSellPrice(productid) - self.getAveragePurchasePrice(productid)
        soldItem = self.getSaleQuantity(productid)
        netProfit = profitPerItem * soldItem
        return netProfit
    
#     function - show dictionary of sales profit and total profit
#     input = nothing
#     output = show dictionary of  profit and sum of all profit
#     1.listOfProduct er protita product er jonno
#         1.productid er respect e profit dictionary te add korbo
#     2.print dictionary
#     3.print sum of all profit

    def showAllProfit(self):
        dictOfProfit = {}
        for product in self.productList:
            dictOfProfit[product.productid] = self.getProfitPerItem(product.productid)
        print(dictOfProfit)
        totalProfit = 0
        for productid in dictOfProfit:
            totalProfit += dictOfProfit[productid]
        print(totalProfit)
    
#     function - netProfit
#     output = total Interest
#     1.dictOfInterest theke value gulo sum korbo
#     def netProfit(self):
#         totalProfit = 0
#         for productid in self.showAllInterest:
#             totalProfit += dictOfInterest[productid]
#         return "totalProfit = ", totalProfit
   
        #5000 sale or purchase object create
    # 1.choose a random product
    # 2.decide purchase or sale
    # 3.if sale:
    #     1.if can't sale go to purchase
    #     2.else sell randomly
    # 4.else purchase
    # 5.go to 1 until 5000 creats
    def create5000PurchaseorSaleObject(self):
        for transactionNumber in range (5000):
            product = random.choice(self.productList)
            choice = random.randint(0, 1)
            if choice == 1:
                try:
                    self.sellRandomQuantity(product.productid)
                except Exception as e:
                    print(e)
            else:
                self.purchaseRandomQuantity(product.productid)

            #        func purchaseRandomQuantity
        # input = productid
        # price = random  
    def purchaseRandomQuantity(self, productid):
        quantity = random.randint(10, 200)
        price = random.randint(20, 300)
        self.purchase(productid, quantity, price)
    
    def sellRandomQuantity(self, productid):
        if self.getBalance(productid) < 1:
            raise Exception ("Product can't sell.Purchase first")
        else:
            quantity = random.randint(1, self.getBalance(productid))
            price = random.randint(20, 300)
            self.sell(productid, quantity, price)
                
    #create menu bar
# 1. print all the options
# 2.take an input number to go to the specific function
# 3.if the input is 1 then call that function and so on for the rest of all
    def menuBar(self):
        while True:
            print(""" 1.show product list
         2.add new product
         3.purchase
         4.sale
         5.show product balance
         6.show all product balance
         7.transaction history
         8.see net Profit
         9.quit
         10.close your option""")
            option = int(input("Enter the option number:",))
            if option == 1:
                products = " "
                for product in self.productList:
                    products += product.name + " "+ str(product.productid) + "\n"
                print(products)
                    
            if option == 2:
                name = input("enter product name:",)
                id = input("enter product id",)
                self.addProduct(name, id)
            if option == 3:
                productid = input("enter productid:",)
                quantity = int(input("enter product quantity:",))
                price = int(input("enter price:",))
                try:
                    self.purchase(productid, quantity, price)
                except Exception as e:
                    print(e)
            if option == 4:
                try:
                    productid = input("enter productid:",)
                    quantity = int(input("enter product quantity:",))
                    price = int(input("enter price:",))
                    self.sell(productid, quantity, price)
                    print(True)
                except ValueError as e: 
                    print("productid, quantity, price should be integer value")
                
                except Exception as e:
                    print(e)
                         
            if option == 5:
                productid = input("enter productid:",)
                print(self.getBalance(productid))
                
            if option == 6:
                print(self.getDictOfProductBalance())
                
#             if option == 7:
                
            if option == 8:
                print(self.showAllProfit())
               
            if option == 9:
                break   