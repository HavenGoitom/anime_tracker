ANIME_FILE = "anime_tracker.txt"

def load_anime_list():
    """Load anime list from file."""
    try:
        with open(ANIME_FILE, "r") as file:
            return [line.strip().split(" - ") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_anime_list(anime_list):
    """Save anime list to file."""
    with open(ANIME_FILE, "w") as file:
        for anime in anime_list:
            file.write(" - ".join(anime) + "\n")

def add_anime():
    """Add a new anime to the list."""
    name = input("Enter anime name: ").strip()
    watched = input("Have you watched this anime? (yes/no): ").strip().lower()
    
    if watched == "yes":
        rating = input("Rate the anime out of 5: ").strip()
        anime_list.append([name, "Watched", rating])
    else:
        anime_list.append([name, "Not Watched", "N/A"])
    
    save_anime_list(anime_list)
    print(f"{name} added successfully!\n")

def update_anime():
    """Update watch status of an anime."""
    name = input("Enter the anime name to update: ").strip()
    for anime in anime_list:
        if anime[0].lower() == name.lower():
            watched = input("Have you watched this anime? (yes/no): ").strip().lower()
            if watched == "yes":
                anime[1] = "Watched"
                anime[2] = input("Enter rating out of 5: ").strip()
            else:
                anime[1] = "Not Watched"
                anime[2] = "N/A"
            save_anime_list(anime_list)
            print(f"Updated {name} successfully!\n")
            return
    print("Anime not found.\n")

def delete_anime():
    """Delete an anime from the list."""
    name = input("Enter the anime name to delete: ").strip()
    global anime_list
    anime_list = [anime for anime in anime_list if anime[0].lower() != name.lower()]
    save_anime_list(anime_list)
    print(f"{name} deleted successfully!\n")

def display_anime_list():
    """Display all anime sorted by rating."""
    sorted_list = sorted(anime_list, key=lambda x: (x[2] != "N/A", x[2]), reverse=True)
    
    if not sorted_list:
        print("No anime in the list.\n")
        return
    
    print("Anime List:")
    for anime in sorted_list:
        print(f"- {anime[0]} | Status: {anime[1]} | Rating: {anime[2]}")
    print()

def main():
    """Main menu loop."""
    global anime_list
    anime_list = load_anime_list()
    
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
            display_anime_list()
        elif choice == "5":
            print("Exiting Anime Tracker. Goodbye!")
            save_anime_list(anime_list)
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
