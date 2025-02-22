def add_anime():
    anime_name = input("Enter Anime Name: ")
    status = input("Have you watched this anime? (Yes/No): ")
    if status.lower() == "yes":
        status = "Watched"
        anime_rating = input("Enter your rating for this anime out of 5: ")
    else:
        status = "Not Watched"
    with open("anime_list.txt", "a") as file:
        file.write(f"{anime_name} - {status} - {anime_rating}\n")
    print("Anime added successfully")
def update_anime():
    anime_name = input("Enter the anime name you want to update: ")
    new_status = input("Have you watched this anime? (Yes/No): ")
    if new_status.lower() == "yes":
        new_status = "Watched"
        anime_rating = input("Enter your rating for this anime out of 5: ")
    else:
        new_status = "Not Watched"
    with open("anime_list.txt", "r") as file:
        lines = file.readlines()
    with open("anime_list.txt", "w") as file:
        for line in lines:
            if anime_name in line:
                file.write(f"{anime_name} - {new_status} - {anime_rating}\n")
            else:
                file.write(line)
    print("Anime updated successfully")
def delete_anime():
    anime_name = input("Enter the anime name you want to delete: ")
    with open("anime_list.txt", "r") as file:
        lines = file.readlines()
    with open("anime_list.txt", "w") as file:
        for line in lines:
            if anime_name not in line:
                file.write(line)
    print("Anime deleted successfully")
def display_anime_list():
    with open("anime_list.txt", "r") as file:
        print(file.read())
def exit():
    print("Exiting Anime Tracker")
    quit()
while(True):
    print("\n")
    print("Anime Tracker Menu:")
    print("1. Add Anime")
    print("2. Update Anime Status")
    print("3. Delete Anime")
    print("4. Display Anime List")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_anime()
    elif choice == 2:
        update_anime()
    elif choice == 3:
        delete_anime()
    elif choice == 4:
        display_anime_list()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")