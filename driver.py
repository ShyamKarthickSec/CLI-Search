from exa_py import Exa

exa = Exa('a3fd55f8-9e77-45d7-a584-7e7f0d184e2d')

def welcome_banner():
    print('''
      _____ __                         _          _____                      __       ______            _          
     / ___// /_  __  ______ _____ ___ ( )_____   / ___/___  ____ ___________/ /_     / ____/___  ____ _(_)___  ___ 
     \__ \/ __ \/ / / / __ `/ __ `__ \|// ___/   \__ \/ _ \/ __ `/ ___/ ___/ __ \   / __/ / __ \/ __ `/ / __ \/ _ \
     ___/ / / / / /_/ / /_/ / / / / / / (__  )   ___/ /  __/ /_/ / /  / /__/ / / /  / /___/ / / / /_/ / / / / /  __/
    /____/_/ /_/\__, /\__,_/_/ /_/ /_/ /____/   /____/\___/\__,_/_/   \___/_/ /_/  /_____/_/ /_/\__, /_/_/ /_/\___/ 
           /____/                                                                          /____/               
          ''')
    print("Your one stop solution for Querying/interacting with AI/LLMs through terminal!")
    return 

def get_input():
    print("You can choose to get data from all-sites or restrict it to few specific domains/websites as well!")
    options = ["All","instagram.com","google.com","x.com","stackoverflow.com","stackexchange.com"]
    print("Select from the list of options available below.")
    for index,option in enumerate(options,start=1):
        print(f"{index}.{option}")
    
    user_input = input("Select your choice: ")

    selected_option = None

    if user_input.isdigit():
        choice_num = int(user_input)
        if 1 <= choice_num <= len(options):
            selected_option = options[choice_num - 1]
        else:
            print("Invalid options! Choose one from above.")
    else:
        for option in options:
            if user_input.strip().lower() == option.lower():
                selected_option = option
                break
        if selected_option is None:
            print("Select an option from above!")

    if selected_option is not None:
        print(f"Your option was {selected_option}|")
        return selected_option

def all():
    print("Thanks for choosing an option from above.")
    query = input("Please Input your query here: ")
    response = exa.search(
        query,
        num_results=2,
        type="keyword"
    )
    for results in response.results:
        print(f'Title: {results.title}')
        print(f'URL: {results.url}')
        print()
    return

def custom_domain_search(get_inputs):
    print("Thanks for choosing a custom option from above.")
    query = input("Please Input your query here: ")
    response = exa.search(
        query,
        num_results=2,
        include_domains=[get_inputs],
        type="keyword"
    )
    for results in response.results:
        print(f'Title: {results.title}')
        print(f'URL: {results.url}')
        print()
    return



def main():
    welcome_banner()
    print("Do you want to search through a particular domain/site?")
    self_input = input("Select Yes/No[Y/N]: ")
    print(self_input)
    if self_input.strip().lower() == "yes" or self_input.strip().lower() == "y":
        get_inputs = get_input()
        custom_domain_search(get_inputs)
    else:
        get_inputs = "all"
        all()   

if __name__=="__main__":
    main()

