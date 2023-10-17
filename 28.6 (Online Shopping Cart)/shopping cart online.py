import random
import time
from prettytable import PrettyTable
import re
class ShopCart:## Parent Class
    def __init__(self,idn,name,ph): ###Variable Defined using instance method
        self.idn=idn
        self.name=name
        self.__ph=ph
        self.cost_list=[]               
        self.shop_pro=[]
    def get_ph(self):
        return self.__ph
    def shop(self): ## function used to shop items and find its cost
        self.listno=["1","2","3"]
        self.pro=["Milk","Bread","Eggs"]
        self.price=[150,99,150]### 3 list are separated (product,no,cost)
        ch='1' #flag to looping
        table=PrettyTable(["No","Item","Price"])###pretty table function is used to print table format to cart items(item,price)
        for i,j,k in zip(self.listno,self.pro,self.price):
            table.add_row([i,j,k]) ### added rows 1 by 1
        while ch!="q":
            print(table)#print table
            while True:
                ch=input("\n\tEnter Item Number to Add to Cart (Press q to quit): ")### Choice get based on given validation
                try:
                    if re.match(r"[123qQ]",ch):
                        break
                    else:       
                        raise Exception("\n\tInvalid Choice ! ! !")
                except Exception as error:
                    print(error)
            if ch=="q" or ch=="Q": ## press q to quit , flag works to stop looping
                break
            while True:
                quan=input("\n\tEnter Quantity : ")### Quantity get based on given validations
                try:
                    a=quan.replace(".","")
                    if a.isnumeric():
                        quan=float(quan)
                        if quan>0:
                            break
                        else:
                            raise Exception("\n\t\tQuantity Should be One or More")
                    else:
                        raise Exception("\n\t\tPlease Enter Numeric Value ! ! !")
                except Exception as error:
                    print(error)
            for i,j,k in zip(self.listno,self.pro,self.price): ### Using zip function to combine 3 lists and shop product that calculate its value
                if i==ch:
                    cost=k*quan
                    self.cost_list.append(cost)
                    ### append cost 1 by 1 in the list
                    self.shop_pro.append(j)## append product name 1 by 1
                    print("\n\t\t",i," . ",j," Added to the Cart. Total Price Rs. ",cost)
        o=sum(self.cost_list)
        return o
class Discount(ShopCart): ### Child class inherit by parent class
    def __init__(self,idn,name,ph):## Variables defined in instance method
        super().__init__(idn,name,ph)### parent class variables declared to get some purpose using super()
        self.dis_pro={"Sugar":{1:5,5:10},"Rice":{10:4,25:8},"Atta":{5:6,10:12}} 
        self.dis_price={"1":{"Sugar":40},"2":{"Rice":50},"3":{"Atta":60}}### 2 nested dictionary are used valid name and calculate its value by given quantity and discounts
    def discount(self): ### fucntion defined to added discount product in cart
        table=PrettyTable(["Item","Quantity( Kg )","Discount ( % )"]) ## Those items also Create table format and denote discounts 
        for i,j in self.dis_pro.items():
            for k,l in j.items():
                table.add_row([i,k,l])
        table1=PrettyTable(["No","Product","Price"]) ### this item table to created for denote the price
        for i,j in self.dis_price.items():
            for k,l in j.items():
                table1.add_row([i,k,l])
        ch='1'
        print(table) ##print discount table
        while ch!='q':
            print("\n\tList Of Available Items for Shopping\n")
            print("\t",table1) #print price table
            while True:
                ch=input("\n\tEnter Items Number to Add to Cart (Press q to Quit) : ") ## choice get based on given validations
                try:
                    if re.match(r"[123qQ]",ch):
                        break
                    else:
                        raise Exception("\n\t\tInvalid Choice ! ! !")
                except Exception as error:
                    print(error)
            if ch=="q" or ch=="Q": ## Flag as set to stop looping
                break
            while True:
                quan=input("\n\tEnter Quantity : ") ## Get Quantity
                try:
                    a=quan.replace(".","")
                    if a.isnumeric():
                        quan=float(quan)
                        if   quan>0:
                            break
                        else:
                            raise Exception("\n\t\tQuantity Not Accept Zero & Negative ! ! !")
                    else:
                        raise Exception("\n\t\tPlease Enter Numeric Value ! ! !")
                except Exception as error:
                    print(error)
            for i,j in self.dis_price.items():  ## set discount based on particular product's quantity
                if i==ch:
                    for k,l in j.items():
                        price=l
                        product=k
                        self.shop_pro.append(product) ### this also added cart 
            for i,j in self.dis_pro.items():
                if i==product:
                    for k,l in j.items():
                        if quan>=k:
                            di=l
            di=price*(di/100)
            cost=price-di
            cost=cost*quan### get calculation that discount and its price by particular product's quantity
            self.cost_list.append(cost)
            print("\n\t\t",ch," . ",product," Added to the Cart. Total Price Rs. ",cost)
    def recipt(self,delivery,loc):
        self.cos=[]
        self.prod=set(self.shop_pro)
        self.prod=list(self.prod)
        self.delivery=delivery
        self.loc=loc
        print("\n\tCustomer Name\t\t: ",self.name)
        print("\tCustomer ID\t\t: ",self.idn)
        print("\tCustomer Phone Number\t: ",self.get_ph())
        print("\tCustomer Location\t: ",self.loc)
        for i in self.prod:
            c=0
            for j,k in zip(self.shop_pro,self.cost_list):
                if i==j:
                    c+=k
            self.cos.append(c)### this part is defined as same product comes repeat that convert into single product name and added price
        table2=PrettyTable(["Item","Price"]) ## This Table created for print bill
        for i,j in zip(self.prod,self.cos):
            table2.add_row([i,j])
        if self.delivery==1:
            self.delivery=0
            table2.add_row(["Delivery Charge","F R E E ! !"])
        elif self.delivery==0:
            table2.add_row(["Delivery Charge","-- NO --"])
        else:
            table2.add_row(["Delivery Charge",self.delivery])
        total=self.delivery+sum(self.cos)
        table2.add_row(["----------","-----------"])
        table2.add_row(["Total Cost",total])
        print(table2)
class LuckyDraw(Discount): ### Grandchild class inherit by child class
    def __init__(self,idn,name,ph):###Variable Defined using instance method
        super().__init__(idn,name,ph)
        self.luck_pro=["Speaker","TV","AC","Gold Coin","Bike","Better Luck Next Time","Spin Once More","Cycle","Laptop","Mobile","Play Station","Washing Machine"]
    def __luck(self):
        print("\n\t\tWelcome to Lucky Draw ! ! !")
        print("\tNow It's Time to Spin the Board....")
        while True:
            spin=input("\n\tEnter Any Key to Spin Lucky Draw\t: ")
            t=random.randint(3,7)
            print("\n\t\tPlease Wait ! ! !")
            time.sleep(t)
            won=random.choice(self.luck_pro) ### pick random prize in list
            if won=="Better Luck Next Time":
                print("\n\t\tOops ! Better Luck Next Time ! ! !")
                break
            elif won=="Spin Once More":
                print("\n\t\tSpin Again Chance ! ! ! ")
            else:
                print("\n\t\tCongradulations ! You Won ",won)
                print("\n\tThank You Shopping With Us And Participating in the Lucky Draw . Have a Great Day ! ! !")
                break
    def get_luck(self):
        return self.__luck()

rand_range=list(range(1000,10000))
cus_id_list=[]
user_id_num=[]
user_id_loc={"Adayar":"Ad","Besant nagar":"Bn","Indra nagar":"In","T-nagar":"Tn"} ## Dictionary is used to get location nick name to generate id
random_list=[]
cus_name=[]
cus_ph=[]
ph_no=[]
while True:
    print("\n\t\tOnline Shopping")
    print("\t\t~~~~~~~~~~~~~~~")
    print("\n\t1. Sign Up ( New User)")
    print("\t2. Sign In")
    print("\t3. Exit")
    while True:
        ch=input("\n\tEnter Your Choice : ")
        try:
            if ch.isnumeric():
                ch=int(ch)
                break
            else:
                raise Exception("\n\t\tPlease Enter Numeric Value ! ! !")
        except Exception as error:
            print(error)
    if ch==1:
        print("\n\tAvailable Locations Are\n")
        for i in user_id_loc.keys():
            print("\t > ",i)
        ############################
        ######
        while True:
            id_num=random.choice(rand_range)
            try:
                if not id_num in user_id_num:
                    id_num=str(id_num)
                    user_id_num.append(id_num)
                    break
                else:
                    raise Exception("\n\t\tPlease Wait ! ! !")
            except Exception as error:
                print(error)
        while True:
            loc=input("\n\tEnter Your Location : ").capitalize()
            try:
                if re.match(r"[A-Z\sa-z]{1,15}",loc):
                    if loc in list(user_id_loc.keys()):
                        for i,j in user_id_loc.items():
                            if i==loc:
                                loc_id=j
                        break
                    else:
                        raise Exception("\n\t\tPlease Enter Nearest Place ! ! !")
                else:
                    raise Exception("\n\t\tPlease Enter Alphabets ! ! !")
            except Exception as error:
                print(error)
        cus_id="ABC"+id_num+loc_id.upper()
        print("\n\tYour Customer ID is ",cus_id)
        ############
        ##################This part processed generate customer id
        cus_id_list.append(cus_id) ## And append it
        while True:
            name=input("\n\tEnter Your Name : ").capitalize() # Get name
            try:
                if re.match(r"^[A-Za-z\s]{3,15}$",name):
                        break
                else:
                    raise Exception("\n\t\tPlease Check Your Name ! ! !")
            except Exception as error:
                print(error)
        cus_name.append(name) ## Append it
        while True:
            ph=input("\n\tEnter Your Phone Number : ") ## Get Phone number
            try:
                if re.match(r"[987]{1}[0-9]{9}",ph):
                    c=ph.count("0") 
                    if not c>7:
                        if not ph in ph_no: ## Check Unique number
                            ph_no.append(ph)
                            break
                        else:
                            raise Exception("\n\t\tAlready Registered Phone Number  ! ! !")
                    else:
                        raise Exception("\n\t\tPhone Number Will Not Allowed Consecutive Zeroes ! ! !")
                else:
                    raise Exception("\n\t\tPlease Check Your Phone Number Pattern ! ! !")
            except Exception as error:
                print(error)
        cus_ph.append(ph) ### Append it
        print("\n\tHello ",name.upper())
    elif ch==2:
        if len(cus_id_list)>0: # validate customer id present or not
            while True:
                cus_id=input("\n\tEnter Your Customer ID : ").upper() ## Get Customer id
                try:
                    if cus_id in cus_id_list:
                        break
                    else:
                        raise Exception("\n\t\tInvalid Customer ID ! ! !")
                except Exception as error:
                    print(error)
            for i,j,k in zip(cus_id_list,cus_name,cus_ph): ### Combine 3 lists to set pairing
                if i==cus_id: ## compare customer id
                    s=LuckyDraw(i,j,k) ### Object creation or object instanciation
                    do="y"
                    while do!="n":
                        o=s.shop() ### class function call using object
                        if o>=500:
                            print("\n\tDiscount Products are Available ! ! !")
                            while True:
                                c=input("\n\tDo You Want to Purchase (y/n) : ").upper() ## get input for discount function call or not 
                                try:
                                    if re.match(r"[YN]",c):
                                        break
                                    else:
                                        raise Exception("\n\t\tPlease Enter Y or N ! ! !")
                                except Exception as error:
                                    print(error)
                            if c=='Y':
                                s.discount() ## if c is y then discount function can process
                        if len(s.shop_pro)>0: ## Check customer do shop or not 
                            print("\n\tAvailable Delivery Locations Are\n")
                            for i in user_id_loc.keys():
                                print("\t > ",i) ### Print Delivery locations
                            while True:
                                del_loc=input("\n\tEnter Delivery Location : ").capitalize() ## Get input for delivery place
                                try:
                                    if re.match(r"[A-Za-z-\s]{3,15}",del_loc):
                                        break
                                    else:
                                        raise Exception("\n\t\tPlease Enter Correct Pattern ! ! !")
                                except Exception as error:
                                    print(error)
                            if del_loc in user_id_loc: ### Check delivery location is available or not
                                if del_loc=="Adayar": ## Check location is deliverable or not
                                    print("\n\t\tSorry , Online Delivery is Not Available in ",del_loc," ! ! !") 
                                    while True:
                                        pic=input("\n\tWould You Like to Pick It Up From Our Nearest Store (y/n) : ").upper() ## get input for pick items in shop directly or not
                                        try:
                                            if pic.isalpha():
                                                if re.match(r"[YN]{1}",pic):
                                                    break
                                                else:
                                                    raise Exception("\n\t\tOnly Allowed Y or N ! ! !")
                                            else:
                                                raise Exception("\n\t\tOnly Allowed Alphabets ! ! !")
                                        except Exception as error:
                                            print(error)
                                    if pic=="N": ## delivery charge set based on user's delivery location
                                        delivery=40
                                        print("\n\t\tDelivery Charges Will Be Applied ! ! !")
                                    else:
                                        print("\n\t\tOk Fine ! ! !")
                                        delivery=0
                                else:
                                    delivery=0
                            s.recipt(delivery,loc) ### call recipt function to generate bill
                            s.get_luck() ### Spin Lucky draw function that call
                            break
                        else:
                            print("\n\t\tYour Cart is Empty Cart ! ! !")
                            while True:
                                do=input("\n\tDo You Purchase Any Product ? (Say y/n): ").lower()
                                try:
                                    if re.match(r"[yn]{1}",do):
                                        break
                                    else:
                                        raise Exception("Invalid Choice (Say y/n) ! ! !")
                                except Exception as error:
                                    print(error)
                            print("\n\t\tThank You For Visiting ! ! !")
        else:
            print("\n\t\tSign Up Please ! ! !")
    elif ch==3:
        break
                
        
        
        
                
            
        
        
