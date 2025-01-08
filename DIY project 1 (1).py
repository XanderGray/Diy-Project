SAR = str(input("Do you want to search for a preexisting item or add a new item to a list?")).title()

if SAR == 'Search':
    loop = True
    while loop == True:
        NoID = str(input("Do you want to search by name or ID number?")).title()
        if NoID == 'Name':
                loop = False
                name = str(input("Please enter the name of the item")).title()
                file = open("Stock.txt","r")
                line = file.readline()
                data = line.split(":")
                while line:
                    if name == data[0]:
                        quantity = data[4].replace("\n", "")
                        print(f"The {name} is located in {data[3]} and there are currently {quantity} in stock")
                        take = str(input(f"Would you like to take some of these {data[2]}?")).title()
                        if take == 'Yes':
                            bigloop = True
                            while bigloop == True:
                                       amount = int(input("How many would you like to take?"))
                                       quantity = int(quantity)
                                       if (quantity-amount) <= 0:
                                            print("That is too much to take")
                                       else:
                                            print("Perfect")
                                            quantity = (quantity-amount)
                                            bigloop = False
                        
                    line = file.readline()
                    data = line.split(":")
                file.close()
                variable = ''
                file = open("Stock.txt","r")
                line = file.readline()
                data = line.split(":")
                while line:
                    if name == data[0]:
                        name = data[0].replace("/n", "")
                        num = data[1].replace("/n", "")
                        dep = data[2].replace("/n", "")
                        place = data[3].replace("/n", "")
                        quantity = str(quantity)
                        variable = (variable+name+":"+num+":"+dep+":"+place+":"+quantity+"\n")
                        
                    else:
                        variable = (variable + line)
                    
                    line = file.readline()
                    data = line.split(":")
                file.close()
                file = open("Stock.txt","w")
                file.write(variable)
                file.close()
                
        elif NoID == 'Number':
                loop = False
                subloop = True
                while subloop == True:
                    IDnum = str(input("Please enter the ID number of the item"))
                    if len(IDnum) == 7:
                        subloop = False
                    
                    else:
                        print("Error answer not 7 characters")
                        
                file = open("Stock.txt","r")
                line = file.readline()
                data = line.split(":")
                while line:
                    if IDnum == data[1]:
                        quantity = data[4].replace("\n", "")
                        name = data[0]
                        print(f"The {name} is located in {data[3]} and there are currently {quantity} in stock")
                        take = str(input(f"Would you like to take some of these {data[2]}?")).title()
                        if take == 'Yes':
                            bigloop = True
                            while bigloop == True:
                                       amount = int(input("How many would you like to take?"))
                                       quantity = int(quantity)
                                       if (quantity-amount) <= 0:
                                            print("That is too much to take")
                                       else:
                                            print("Perfect")
                                            quantity = (quantity-amount)
                                            bigloop = False
                                   
                    line = file.readline()
                    data = line.split(":")
                file.close()
                variable = ''
                file = open("Stock.txt","r")
                line = file.readline()
                data = line.split(":")
                while line:
                    if IDnum == data[1]:
                        name = data[0].replace("/n", "")
                        num = data[1].replace("/n", "")
                        dep = data[2].replace("/n", "")
                        place = data[3].replace("/n", "")
                        quantity = str(quantity)
                        variable = (variable+name+":"+num+":"+dep+":"+place+":"+quantity+"\n")
                        
                    else:
                        variable = (variable + line)
                    
                    line = file.readline()
                    data = line.split(":")
                file.close()
                file = open("Stock.txt","w")
                file.write(variable)
                file.close()
                    
                
    
                
                
        else:
                print("Please choose one or the other")
        



elif SAR == 'Add':
    exists = str(input("Does this item already exist?")).title()
    if exists == 'Yes':
        file = open("Stock.txt","r")
        line = file.readline()
        data = line.split(":")
        NorID = str(input("Please enter either the product name or the product ID")).title()
        while line:
            if data[0] == NorID:
                name = data[0]
                quantity = int(input(f"We have located {name} how much do you wish to add?"))
                current = int(data[4])
                total = (current+quantity)
                print("Ok")
            elif data[1] == NorID:
                name = data[0]
                quantity = int(input(f"We have located {name} how much do you wish to add?"))
                current = int(data[4])
                total = (current+quantity)
                print("Ok")
                
                
                
            line = file.readline()
            data = line.split(":")
        file.close()
        variable = ''
        file = open("Stock.txt","r")
        line = file.readline()
        data = line.split(":")
        while line:
                if name == data[0]:
                        name = data[0].replace("/n", "")
                        num = data[1].replace("/n", "")
                        dep = data[2].replace("/n", "")
                        place = data[3].replace("/n", "")
                        total = str(total)
                        variable = (variable+name+":"+num+":"+dep+":"+place+":"+total+"\n")
                        
                else:
                        variable = (variable + line)
                    
                line = file.readline()
                data = line.split(":")
        file.close()
        file = open("Stock.txt","w")
        file.write(variable)
        file.close()
            

            
    
    else:
        loop0 = True
        while loop0 == True:
            name = str(input("PLease enter the name of the equiptment")).title()
            file = open("Stock.txt","r")
            line = file.readline()
            data = line.split(':')
            same = False
            while line:
                if data[0] == name:
                    same = True
                line = file.readline()
                data = line.split(':')
            if same == True:
                print("This item already exists in our system.")
                
            else:
                print("New item accepted")
                loop0 = False
            
        file.close()
        loop1 = True
        while loop1 == True:
            num = int(input("Please enter a 6 digit number that that doesnt start with 0 for the unique ID code"))
            num = str(num)
            if len(num) == 6:
                num = "0"+num
                file = open("Stock.txt","r")
                line = file.readline()
                data = line.split(':')
                Same = False
                while line:
                    if data[1] == num:
                        Same = True
                    line = file.readline()
                    data = line.split(":")
                if Same == True:
                    print("This id code is already taken")
                    
                else:
                    print("ID code accepted")
                    loop1 = False
                      
            else:
                print("Please enter 6 digit number")
        file.close()
        dep = str(input("Please enter the name of the department this is in")).title()
        file = open("Stock.txt","r")
        line = file.readline()
        data = line.split(':')
        Exists = False
        x = 0
        while line:
            if dep == data[2]:
                area = data[3]
                Exists = True
            line = file.readline()
            data = line.split(':')
            x = (x+1)
        file = file.close()
        if Exists == True:
            print(f"Adding {name} to the {dep} department located on {area}")
            quantity = int(input("Please enter the amount you are adding"))
            quantity = str(quantity)
            variable = ''
            file = open("Stock.txt","r")
            line = file.readline()
            data = line.split(':')
            done = False
            while line:
                print(line)
                variable = (variable+line)
                if dep == data[2] and done == False:
                    variable = (variable + name+":"+num+":"+dep+":"+area+":"+quantity+"\n")
                    done = True
                line = file.readline()
                data = line.split(":")
            file.close()
            file = open("Stock.txt","w")
            file.write(variable)
            file.close()
            
            
            
        
        else:
            file = open("Stock.txt","r")
            line = file.readline()
            data = line.split(':')
            while line:
                if x == 1:
                    for char in data[3]:
                        if char == '1':
                            area = data[3].replace("1","2")
                            
                        elif char == '2':
                            letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P''Q','R','S','T','U','V','W','X','Y','Z')
                            LETTERS = ('B','C','D','E','F','G','H','I','J','K','L','M','N','O','P''Q','R','S','T','U','V','W','X','Y','Z','A')
                            for char in data[3]:
                                if char in letters:
                                    find = 0
                                    loop3 = True
                                    while loop3 == True:
                                        if char == letters[find]:
                                            area = (LETTERS[find]+"1")
                                            loop3 = False   
                                        else:
                                            find = (find+1)
                            
                line = file.readline()
                data = line.split(':')
                x = (x-1)
            file.close()
            quantity = int(input("Please enter the amount you wish to add"))
            quantity = str(quantity)
            file = open("Stock.txt","r")
            line = file.readline()
            variable = ''
            while line:
                variable = (variable+line)
                line = file.readline()
            file.close()
            variable = (variable + name+":"+num+":"+dep+":"+area+":"+quantity+"\n")
            file = open("Stock.txt","w")
            file.write(variable)
            file.close()
                
            
            
    
            
        
    
#Screwdriver:0987654:Tools:A1:3
#Hammer:0123456:Tools:A1:23
#Ruler:0876234:Tools:A1:23
#Glue:0111111:Chemicals:A2:123
#FoamFiller:0234234:Chemicals:A2:12
#Nails:0121212:Fasteners:B1:298
#Screws:0210210:Fasteners:B1:178
#Bolts:0234532:Fasteners:B1:126