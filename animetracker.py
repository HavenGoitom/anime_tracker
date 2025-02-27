filename = "anime_tracker.txt"
def add_anime():
    name = input("Enter the name: ").replace(" ", "").strip()
    anime_type = input("Enter the type: ").strip()
    status = input("Have you watched it (yes/no): ").strip().lower()
    
    while True:
        if status == "yes":
            rating = input("Enter the rating: ").strip()
            status = "watched"
            break
        elif status == "no":
            rating = "N/A"
            status = "unwatched"
            break
        else:
            print("You should enter yes or no, please try again!")
            status = input("Have you watched it (yes/no): ").strip().lower()
    
    with open(filename, 'a') as file:
        file.write(f"{name}||{anime_type}||{status}||{rating}\n")
    
    print(f"{name} added successfully!\n")

def update_anime():
    input_name = input("Enter the name of the anime you want to update: ").replace(" ", "").strip().lower()
    
    with open(filename, 'r') as file:
        anime_list = file.readlines()
    
    anime_split_list = []
    for anime in anime_list:
        anime_split = anime.strip().split("||")
        anime_split_list.append(anime_split)
    
    updated = False
    
    for anime in anime_split_list:
        stored_name = anime[0].replace(" ", "").strip().lower()
        if input_name == stored_name:
            while True:
                new_status = input("Did you watch this anime (yes/no): ").strip().lower()
                if new_status == "yes":
                    anime[2] = "watched"
                    anime[3] = input("Enter rating out of 5: ").strip()
                    updated = True
                    break
                elif new_status == "no":
                    anime[2] = "unwatched"
                    anime[3] = "N/A"
                    updated = True
                    break
                else:
                    print("You should enter yes or no, please try again!")
            break

    if updated:
        with open(filename, 'w') as file:
            for anime in anime_split_list:
                file.write("||".join(anime) + "\n")
        print("Anime updated successfully!")
    else:
        print("The name you entered is not on the anime list.")

def delete_anime():
    input_name = input("Enter the name of the anime you want to delete: ").replace(" ", "").strip().lower()
    
    with open(filename, 'r') as file:
        anime_list = file.readlines()
    
    new_anime_list = []
    found = False
    
    for line in anime_list:
        parts = line.strip().split("||")
        stored_name = parts[0].replace(" ", "").strip().lower()
        if stored_name == input_name:
            found = True
        else:
            new_anime_list.append("||".join(parts) + "\n")
    
    if not found:
        print(f"The anime '{input_name}' was not found.")
    else:
        with open(filename, 'w') as file:
            file.writelines(new_anime_list)
        print(f"{input_name} deleted successfully!\n")

def display_anime():
    with open(filename) as file:
        contents = file.read()
        print(contents)

while True:
    print("Anime Tracker Menu:")
    print("1. Add Anime")
    print("2. Update Anime Status")
    print("3. Delete Anime")
    print("4. Display Anime List")
    print("5. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        add_anime()
    elif choice == "2":
        update_anime()
    elif choice == "3":
        delete_anime()
    elif choice == "4":
        display_anime()
    elif choice == "5":
        print("Exiting Anime Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
