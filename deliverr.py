class InventoryAllocator:
    def __init__(self):
        f = open('testcases.txt', 'r')
        inputs = f.read().split("\n")
        print("=================================================================")
        for i in inputs:
            print("INPUT: ")
            print(i)
            print("\n")
            print("OUTPUT")
            self.process(i)
            print("=================================================================")



    def process(self, input_text):
        #process data and find basic input errors
        input_data = input_text.replace(" ","")
        if "},[" not in input_data:
            print("Wrong input format. Enter order and inventory seperated by comma")
            return 0

        #find first comma and separate order and warehouse data
        split_pos = 0
        for i in range(len(input_data)):
            if input_data[i] == "}" and input_data[i+1] == ",":
                split_pos = i+1
                break

        # split_pos points to the comma between order and <[> warehouses <]>
        order_str = input_data[1:split_pos-1]
        order_arr = order_str.split(",")

        #convert ['apple:5','banana:5'] ==> {apple: 5, banana: 5} 
        order = {}
        for i in order_arr:
            item_name = i.split(":")[0]
            item_quantity = int(i.split(":")[1])
            order [item_name] = item_quantity


        inventory_str = input_data[split_pos+2:-1]
        total = {}
        # Will hold the data in format 
        '''
            total: {
                banana: [total_count, (name_of_warehouse, storage), ...],
                apple: [total_count, (name_of_warehouse, storage), ...],
                .
                .
                .
            }
        '''
        start = 0
        inv_str_arr = []
        # Hold string data of every warehouse => inv_str_arr = ['{name: warehouse_name, inventory: {item: quantity}','...',...]
        for end in range(1,len(inventory_str)):
            if inventory_str[end] == "}" and inventory_str[end-1] == "}":
                inv_str_arr.append(inventory_str[start:end+1])
                start = end + 2

        # Create dict for every element in inv_str_arr
        for i in inv_str_arr:
            if 'name' not in i:
                print("Wrong format, name of warehouse missing!")
                return 0
            if 'inventory' not in i:
                print("Wrong format, inventory storage of warehouse missing!")
                return 0
            
            # Split name and inventory data
            pos = 0
            for j in range(len(i)):
                if i[j] == ",":
                    pos = j
                    break
            name = i[:pos].split(":")[1]
            inv = i[pos+1:-1]
            # Split at first : in inventory:{}
            for j in range(len(inv)):
                if inv[j] == ":":
                    pos = j
                    break
            inv_data_arr = inv[pos+2:-1].split(",")
            
            # Create total dict in the above shown format
            for i in inv_data_arr:
                if not i:
                    print("Empty Inventory => " + name)
                    continue
                item_name = i.split(":")[0]
                item_quantity = int(i.split(":")[1])
                if item_name in total:
                    total[item_name][0] += item_quantity
                else:
                    total[item_name] = [item_quantity]

                total[item_name].append((name, item_quantity))
            

        ans = {}
        for i in order:
            order_quantity = order[i]
            # order 'apple' not present in total
            if i not in total:
                print("Item not in storage")
                print([])
                return 0
            # order quantity greater than total stock
            if order_quantity > total[i][0]:
                print("Not enough stock")
                print([])
                return 0

            # Greedy approach => exhaust inventories sequentially to minimize cost 
            warehouses = total[i][1:]
            x = 0
            while order_quantity > 0:
                warehouse_name = warehouses[x][0]
                warehouse_quantity = warehouses[x][1]
                # if order_quantity fulfilled by current warehouse, add to result and stop
                if warehouses[x][1] >= order_quantity:
                    if warehouse_name in ans:
                        ans[warehouse_name][i] = order_quantity
                    else:
                        ans[warehouse_name] = { i : order_quantity }
                    order_quantity -= order_quantity

                # if not, take all stock in current warehouse and move to next
                else:
                    if warehouse_name in ans:
                        ans[warehouse_name][i] = warehouse_quantity
                    else:
                        ans[warehouse_name] = { i : warehouse_quantity }
                    order_quantity -= warehouse_quantity
                    x += 1

        # create array of dicts as final answer
        ans_arr = []          
        for i in ans:
            ans_arr.append({i:ans[i]})
        print(ans_arr)

iA = InventoryAllocator()