import random
import get_data

while True:
    selected = input("Please select the number for the option you want:\n"
                     "1) Show team information by name\n"
                     "2) Top scorer in the Premiership in a given year\n"
                     "3) Most red cards in the premiership in a given year\n"
                     "4) Current players by last name in the premiership\n"
                     "5) Random league\n")

    if selected == '1':
        return_query = input("Please enter a team name (check spelling): ")
        return_query = {"name": return_query}
        data = get_data.get_info(return_query, 'teams')
        print(data['response'][0]['team']['name'])
        print(data['response'][0]['team']['code'])
        print(data['response'][0]['team']['country'])
        print(data['response'][0]['team']['founded'])
        print("Stadium Name: " + data['response'][0]['venue']['name'])

    elif selected == '2':
        year = int(input("Please enter a year(2010-2022): "))
        if year < 2010 or year > 2022:
            print("invalid input")
            continue

        year = str(year)
        return_query = {"league": "39", "season": year}
        data = get_data.get_info(return_query, "players/topscorers")
        print(data['response'][0]['player']['firstname'] + " " + data['response'][0]['player']['lastname'])
        print(data['response'][0]['statistics'][0]['team']['name'])
        print(str((data['response'][0]['statistics'][0]['goals']['total'])) + " goals")

    elif selected == '3':
        year = int(input("Please enter a year(2010-2022): "))
        if year < 2010 or year > 2022:
            print("invalid input")
            continue

        year = str(year)
        return_query = {"league": "39", "season": year}
        data = get_data.get_info(return_query, "players/topredcards")
        print(data['response'][0]['player']['firstname'] + " " + data['response'][0]['player']['lastname'])
        print(data['response'][0]['statistics'][0]['team']['name'])
        print(str((data['response'][0]['statistics'][0]['cards']['red'])) + " red cards")

    elif selected == '4':
        name = input("Please enter a last name: ")
        return_query = {"league": "39", "search": name}
        data = get_data.get_info(return_query, "players")
        print(data['response'][0]['player']['firstname'] + " " + data['response'][0]['player']['lastname'])
        print("age " + str(data['response'][0]['player']['age']))
        print(data['response'][0]['player']['nationality'])
        print(data['response'][0]['statistics'][0]['team']['name'])

    elif selected == '5':
        id = str(random.randint(1, 959))
        return_query = {"id": id}
        data = (get_data.get_info(return_query, "leagues"))
        print(data['response'][0]['league']['name'])
        print(data['response'][0]['country']['name'])
    else:
        print("Invalid selection")
        continue

    response = input("Would you like to search for something else? (yes or no): ")
    if response == "y" or response == "yes":
        continue
    else:
        break

print("Goodbye!")
