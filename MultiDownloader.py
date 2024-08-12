import concurrent.futures, urllib.request, urllib.parse, argparse, os, ssl, interactor, shutil
from colorama import *
from urllib.error import URLError, HTTPError

def download_file(url, output_path):
    fName = os.path.join(output_path, urllib.parse.unquote(url).split("/")[-1])
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        print(Fore.YELLOW+f"[*] {Fore.CYAN}Trying to download : {url}{Fore.RESET}")
        urllib.request.urlretrieve(url, fName)
        print(Fore.GREEN+f"[+] {Fore.CYAN}File Store Successfully At: {fName}{Fore.RESET}")
    except HTTPError as h:
         print(Fore.RED+f"[!] HTTPError not able to download {url} because of : {h.code}{Fore.RESET}")
    except URLError as u:
        print(Fore.RED+f"[!] HTTPError not able to download because of : {u.reason}{Fore.RESET}")
    except Exception as f:
        print(f"Catchall Error: {f}")
    
def read_url_from_file(fName):
    try:
        with open(fName,'r') as f:
            urls=(f.readlines())
        f.close()
        urls = [line.rstrip() for line in urls]
        return urls
    
    except FileNotFoundError:
        print(f"{Fore.RED}[!] File not found:\n\t{fName}{Fore.RESET}")
        exit()

    except Exception as e:
        print(Fore.RED+f"[!] Unknown Error"+Fore.RESET)

def create_directory(dirname):
    if '/' not in dirname or '\\' not in dirname:
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path,dirname)
        print(f"{Fore.YELLOW}[*] Attempting to create directory: {Fore.CYAN}{path}{Fore.RESET}")
        try:
            os.makedirs(path)
        except Exception as e:
            print(Fore.RED+f"[!!] Failed to create output directory do you have valid permissions?\n\tDirectory: {path}"+Fore.RESET)
        return(path)
    else:     
        os.makedirs(dirname)
        return(dirname)

def main(args):
    if args.ufile:
        urls = read_url_from_file(fName=args.ufile)
    
    files = len(urls)
    if args.directory:
        path = create_directory(args.directory)
    
    print("DEBUG :: " + path)
    
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    current_url_index_pos = 0
    while current_url_index_pos <= files-1:
        if current_url_index_pos+1 == args.threads:
            import time
            time.sleep((args.threads%2))

        pool.submit(download_file, url=urls[current_url_index_pos], output_path=path)
        current_url_index_pos+=1

if __name__ == '__main__':
    m=''
    file_extensions = ['txt', 'doc', 'docx', 'pdf', 'jpg', 'jpeg', 'png', 'xls', 'xlsx', 'ppt', 'pptx', 'mp3', 'mp4', 'zip']
    parser = argparse.ArgumentParser(prog='main.py',formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('-f', '--ufile', type=str ,help="urlfile to parse",metavar=m)
    parser.add_argument('-u', '--url', type=str,metavar=m)
    parser.add_argument('-t', '--threads', type=int, default=5, help="thread count",metavar=m)
    parser.add_argument('-d', '--directory', type=str, default="out directory",metavar=m)
    parser.add_argument('-l', '--list', action='store_true', help="print supported file types")
    parser.add_argument('-i', '--interactive', action='store_true', help="WebFetch Module!")
    args = parser.parse_args()

    if args.interactive:
        os.system("clear")

    else:
        if args.list == True:
            print(Fore.YELLOW+"Supported File Types:")
            for ext in file_extensions:
                print("\t"+ext)
            print(Fore.RESET)
        elif not args.ufile and not args.url:
            print(Fore.RED+f"[!] {Fore.YELLOW}Divide by 0 error, cannot divide 0 files amongst {args.threads} threads.")
        else:
            main(args)