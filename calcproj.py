print("Welcome to the Python Calculator\n\nWhat would you like to do?")

fruits = ["Banana", "Apples", "Grapes", "Pineapple", "Oranges", "Mango","Peaches", "Watermelon", "Melon"]
veggies = ["Carrots", "Asparagus", "Cabbage", "Lettuce", "Onions", "Greens", "Peas", "Yams", "Beans"]
meat = ["Steak", "Chicken", "Fish", "Hamburger", "Beef", "Ham", "Pork", "Turkey"]
unhealthy =["Candy", "Waffle", "Chicken Nuggets", "Fries", "Fried Chicken", "Pizza"]

fruitsdict = { "Banana": 105, "Apples":95, "Grapes": 62, "Pineapple": 452, "Oranges":45, "Mango":201,"Peaches": 59, "Watermelon": 85, "Melon":360}
veggiesdict = {"Carrots": 25, "Asparagus": 3, "Cabbage": 6, "Lettuce": 5, "Onions":44, "Greens":11, "Peas": 118, "Yams": 177, "Beans": 42}


userfruits= input("What fruit do you like to eat?")
userveggies = input("What vegetable do you like to eat?")
usermeat = input("What meat do you like to eat?")
userunhealthy = input ("What unhealthy food do you like to eat?")
userweight = int(input("How much do you weigh?"))
caloriecount = 0




for x in range (len(fruits)):
    if fruits[x] == userfruits:
      caloriecount += fruitsdict[fruits[x]]
      
for x in range(len(veggies)):
    if veggies[x] == userveggies:
        caloriecount+= veggiesdict[veggies[x]]

print (caloriecount)       
       
    
    
    