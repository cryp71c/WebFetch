from colorama import *
import MultiDownloader, os

banner = """
 /$$      /$$           /$$       /$$$$$$$$          /$$               /$$      
| $$  /$ | $$          | $$      | $$_____/         | $$              | $$      
| $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$     /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$$$$ /$$__  $$|_  $$_/   /$$_____/| $$__  $$
| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$__/| $$$$$$$$  | $$    | $$      | $$  \ $$
| $$$/ \  $$$| $$_____/| $$  | $$| $$   | $$_____/  | $$ /$$| $$      | $$  | $$
| $$/   \  $$|  $$$$$$$| $$$$$$$/| $$   |  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$
|__/     \__/ \_______/|_______/ |__/    \_______/   \___/   \_______/|__/  |__/"""


options = {
    'set'   : ["help","url","tag","class","href","string","download"],
    'clear' : ["help","all","url","tag","class","href","string"],
    'show'  : ["help","opts","options","url","tag","class","href","string","download"],
    "build" : ['exclude','fetch'],
    "exec"  : ['download','outfile']
}

class WebFetch:
    def __init__(self) -> None:
        self.url = ""
        self.tag = ""
        self.class_ = ""
        self.href = ""
        self.string = ""
        self.download = False
        self.excludes = None
    
    def show_opts(self):
        print(f"""{Fore.CYAN}URL=>{Fore.MAGENTA}{self.url}
{Fore.CYAN}TAG=>{Fore.MAGENTA}{self.tag}
{Fore.CYAN}CLASS=>{Fore.MAGENTA}{self.class_}
{Fore.CYAN}HREF=>{Fore.MAGENTA}{self.href}
{Fore.CYAN}STRING=>{Fore.MAGENTA}{self.string}
{Fore.CYAN}DOWNLOAD=>{Fore.MAGENTA}{self.download}""")

    # SETS #
    def clear_all(self):
        self.download=False
        self.url=''
        self.tag=''
        self.class_=''
        self.href=''
        self.string=''
        self.excludes = None
        self.all_params = ['url', 'tag', 'class', 'href', 'string'] # NOT SETTABLE

    def thread_execute(self, threads=5):
        pass

    def set_download(self, download):
        self.download = download

    def set_url(self, url):
        self.url = url
    
    def set_tag(self, tag):
        self.tag = tag
    
    def set_class(self, class_):
        self.class_ = class_
    
    def set_href(self, href):
        self.href = href

    def set_string(self, string):
        self.string = string

    # GETS #
    def get_download(self):
        print(Fore.CYAN+"DOWNLOAD=>"+Fore.MAGENTA+self.download+Fore.RESET)

    def get_url(self):
        print(Fore.CYAN+"URL=>"+Fore.MAGENTA+self.url+Fore.RESET)
    
    def get_tag(self):
        print(Fore.CYAN+"TAG=>"+Fore.MAGENTA+self.tag+Fore.RESET)
    
    def get_class(self):
        print(Fore.CYAN+"CLASS=>"+Fore.MAGENTA+self.class_+Fore.RESET)
    
    def get_href(self):
        print(Fore.CYAN+"HREF=>"+Fore.MAGENTA+self.href+Fore.RESET)

    def get_string(self):
        print(Fore.CYAN+"STRING=>"+Fore.MAGENTA+self.string+Fore.RESET)

    def build(self, excluded_params=None):
        self.excludes = excluded_params
        for i in excluded_params:
            pass
        
    
    def execute(self, task):
        pass

def MultiDownloader():
    fetch = WebFetch()
    try:
        while True:
            choice = str(input(f"{Fore.LIGHTBLUE_EX}WebFech{Fore.RESET}:{Fore.BLUE}WeCrawlInYourSkin{Fore.RESET}>> ")).lower()
            parsed = choice.split(" ")
            if parsed[0] == 'help':
                print(Fore.YELLOW+"Options: ")
                for i in options.keys():
                    print("\t" + Fore.CYAN + i + "\t:: " + Fore.MAGENTA + str(options.get(i)) + Fore.RESET)
                print()
            elif parsed[0] not in options.keys():
                print(f"Invalid Option! {choice}")
                continue
            elif parsed[0] in options.keys():
                if parsed[1] in options.get(parsed[0]):
                    if parsed[0] == 'set':
                        if parsed[1] == "help":
                            print(Fore.YELLOW+"Settable Options:")
                            for i in options.get(parsed[0])[1:]:
                                print(Fore.YELLOW+"\t"+i)
                            print(Fore.RESET)
                        elif parsed[1] == "url":
                            fetch.set_url(parsed[2])
                            print(Fore.GREEN+f"SET URL => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "tag":
                            fetch.set_tag(parsed[2])
                            print(Fore.GREEN+f"SET TAG => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)    
                        elif parsed[1] == "class":
                            fetch.set_class(parsed[2])
                            print(Fore.GREEN+f"SET CLASS => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "href":
                            fetch.set_href(parsed[2])
                            print(Fore.GREEN+f"SET HREF => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "string":
                            fetch.set_string(parsed[2])
                            print(Fore.GREEN+f"SET STRING => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "download":
                            fetch.set_download(parsed[2].lower().capitalize())
                            print(Fore.GREEN+f"SET DOWNLOAD => {Fore.CYAN}{' '.join(parsed[2:]).lower().capitalize()}"+Fore.RESET)
                        else:
                            print(Fore.RED+"[!!!] Unknown Failure")
                    
                    elif parsed[0] == 'clear':
                        c=''
                        if parsed[1] == "help":
                            print(Fore.YELLOW+"Settable Options:")
                            for i in options.get(parsed[0])[1:]:
                                print(Fore.CYAN+"\t"+i)
                            print(Fore.RESET)
                        elif parsed[1] == "all":
                            print(Fore.YELLOW+f"[**] {Fore.CYAN}Clearing All!"+Fore.RESET)
                            fetch.clear_all()
                        elif parsed[1] == "url":
                            fetch.set_url(c)
                            print(Fore.GREEN+f"CLEARED URL => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "tag":
                            fetch.set_tag(c)
                            print(Fore.GREEN+f"CLEARED TAG => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)    
                        elif parsed[1] == "class":
                            fetch.set_class(c)
                            print(Fore.GREEN+f"CLEARED CLASS => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "href":
                            fetch.set_href(c)
                            print(Fore.GREEN+f"CLEARED HREF => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "string":
                            fetch.set_string(c)
                            print(Fore.GREEN+f"CLEARED STRING => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        elif parsed[1] == "download":
                            fetch.set_download(c)
                            print(Fore.GREEN+f"CLEARED DOWNLOAD => {Fore.CYAN}{' '.join(parsed[2:])}"+Fore.RESET)
                        else:
                            print(Fore.RED+"[!!!] Unknown Failure")

                    elif parsed[0] == 'show':
                        if parsed[1] == "help":
                            print(Fore.YELLOW+"Settable Options:")
                            for i in options.get(parsed[0])[1:]:
                                print(Fore.CYAN+"\t"+i)
                            print(Fore.RESET)
                        elif parsed[1] == "url":
                            fetch.get_url()
                        elif parsed[1] == "tag":
                            fetch.get_tag()
                        elif parsed[1] == "class":
                            fetch.get_class()
                        elif parsed[1] == "href":
                            fetch.get_href()
                        elif parsed[1] == "string":
                            fetch.get_string()
                        elif parsed[1] == "download":
                            fetch.get_download()
                        elif parsed[1].strip().lower() in ['opts', 'options']:
                            fetch.show_opts()
                        else:
                            print(Fore.RED+"[!!!] Unknown Failure")

                    elif parsed[0] == 'build':
                        if parsed[1] == 'exclude':
                            exclude = []
                            failed_exclusions = []
                            for i in parsed[2:]:
                                if i not in options.get('set')[1:]:
                                    failed_exclusions.append(i)
                                else:
                                    exclude.append(i)

                                if i == parsed[-1]:
                                    print(Fore.YELLOW+f"[*] {Fore.CYAN}Building with excluded params :: {Fore.MAGENTA}{exclude}")
                                    print(Fore.RED+f"[!] Probably a typo but failed to exclude params :: {Fore.MAGENTA}{failed_exclusions}")
                                    fetch.build()

                    elif parsed[0] == 'exec':
                        pass

                    else:
                        print(Fore.RED+"[!!!] You broke my code. * heres a star for you. Now stop breaking my shit."+Fore.RESET)
            else:
                print(Fore.RED+"[!!!] I am not really sure how you managed this either but you fucked up somehow. * heres a star for you. Now stop breaking my shit."+Fore.RESET)


    except KeyboardInterrupt:
        exit()
    except IndexError:
        print(Fore.LIGHTRED_EX+f"[!] {Fore.RED}Need more arguments!{Fore.RESET}")
        MultiDownloader()

if __name__ == "__main__":
    os.system("clear")
    print(banner+"\n")
    MultiDownloader()