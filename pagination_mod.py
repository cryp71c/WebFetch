from colorama import Fore
import pandas as pd
import os

# FOR LATER IMPLEMENTATION

def more(df, page_size=10):
    total_rows = len(df)
    num_pages = total_rows // page_size + 1
    current_page = 0
    previous_page = None
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(df[current_page * page_size : (current_page + 1) * page_size])
            print(f"Page {current_page + 1}/{num_pages}")

            user_input = input(f"\n{Fore.YELLOW}Press {Fore.MAGENTA}'<Enter>'{Fore.YELLOW} for next page, {Fore.MAGENTA}'b'{Fore.YELLOW} for previous page,{Fore.MAGENTA}'q'{Fore.YELLOW} to quit: "+Fore.RESET)

            if user_input.lower() == "q":
                break
            elif user_input.lower() == "b" and previous_page is not None:
                current_page = current_page-1
            elif user_input == "":
                previous_page = current_page
                current_page = (current_page + 1) % num_pages
            else:
                print("Invalid input. Please try again.")
                
    except KeyboardInterrupt:
        print(Fore.YELLOW+f"[*] {Fore.MAGENTA} Exiting! Bye Bye! {Fore.RESET}")

## FOR TESTING
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', os.get_terminal_size().columns)
df = pd.read_excel('test.xlsx')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
more(df=df)