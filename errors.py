import numpy as np

def choose_restaurant():
    restaurants = ["Panda Express", "Ginger + Soy", "McDonalds", "The Loop"]
    rand_int = np.random.randint(20)

    try:
        restaurant = restaurants[rand_int]
    except IndexError:
        rand_int = np.random.randint(len(restaurants))
        print("Prune the random number so that index is in range!")
        restaurant = restaurants[rand_int]

    return restaurant

def main():
   print(choose_restaurant())


if __name__ == "__main__":
    main()