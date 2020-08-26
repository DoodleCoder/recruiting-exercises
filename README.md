# recruiting-exercises

Details - 
1. deliverr.py contains the python script
2. testcases.txt contains test run input

Assumptions - 
1. Only correct input format => {order_item: order_quantity}, [{name: inventory_name, inventory: {item: quantity}}]
2. All count is integer 
3. No item can be named -> "name" or "inventory"
4. No item name can have special chars (!@#$%^&*(),.:'";/?><")

Logic - 
1. All warehouses are sorted in increasing order of shipping cost.
2. Convert string data to dictionary formats
3. Greedy approach to select max from warehouses in sequential order, starting from first.

Run -
python deliverr.py

Output format - 
=================================================================
INPUT-
<input from testcases.txt>
OUTPUT-
<Output generated after processing>
=================================================================
