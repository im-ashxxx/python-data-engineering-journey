sales = [1200, 2500, 1800, 3200, 1500]
  #Total sales Average sales, Highest sales ,Lowest sales ,Number of sales greater than 2000 

add = 0
for i in range(len(sales)):
    add = sales[i] + add
print("total sales of company C : ",add)

avg= add/len(sales)
print("Average sales of company C : ",avg)

print("Highest sales of company C : ",max(sales))
print("Lowest sales of company C : ",min(sales))

count = 0
for i in range(len(sales)):
    if sales[i] > 2000:
        count += 1
print("Number of sales greater than 2000 for company C : ",count)
  
  
# using functions to calculate total, average, highest, lowest and count of sales greater than 2000 
def calculate_total(sales):
    total = 0

    for value in sales:
        total += value

    return total

total_sales = calculate_total(sales)
print("Total sales of company C : ",total_sales)


def calculate_average(sales):
    total_sales = calculate_total(sales)
    average = total_sales / len(sales)
    
    return average

average_sales = calculate_average(sales)
print("Average sales of company C : ",average_sales)


def find_highest(sales):
    highest = sales[0]
    for value in sales:
        if value > highest:
            highest = value
    
    return highest

highest_sales = find_highest(sales)
print("Highest sales of company C : ",highest_sales)

def find_lowest(sales):
    lowest = sales[0]
    for value in sales:
        if value <lowest :
            lowest = value 
            
    return lowest 
    
lowest_sales= find_lowest(sales)
print("Lowest sales of company C : ",lowest_sales)

def count_above_2000(sales):
    count=0 
    for value in sales:
        if value > 2000:
            count += 1
            
    return count
        
count=count_above_2000(sales)
print("Number of sales greater than 2000 : ",count)
