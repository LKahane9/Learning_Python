# input a fruit, output the number of calories in one portion
# per this https://cs50.harvard.edu/python/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf
# assume that users input it as it is written exactly in the poster (strawberries, not strawberry)

fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 15,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80        
}

def main():
    fruit = input("Item: ").strip().lower()
    calories(fruit)

def calories(f):
    if f in fruits:
        print(f"Calories: {fruits[f]}")

main()