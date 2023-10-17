table2=PrettyTable(["Item","Price"])
        for i,j in zip(self.shop_pro,self.cost_list):
            table2.add_row([i,j])
        table2.add_row(["Delivery Charges",self.delivery])
        total=self.delivery+sum(self.cost_list)
        table2.add_row(["----------","-----------"])
        table2.add_row(["Total Cost",total])
        print(table2)
