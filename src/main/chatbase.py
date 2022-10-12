import enum

try:
    import colorama
except ModuleNotFoundError as e:
    print("Lütfen requirements.txt dosyasını kurun.")
    exit()

class LogType(enum.Enum):
    DEFAULT = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

colorama.init(autoreset=True)

def write(text, type=LogType.INFO, end="\n"):
    resultText = ""
    if type == LogType.DEFAULT:
        resultText = f"{colorama.Fore.White} [*] {text}"
    if type == LogType.INFO:
        resultText = f"{colorama.Fore.BLUE} [I] {text}"
    if type == LogType.WARNING:
        resultText = f"{colorama.Fore.YELLOW} [W] {text}"
    if type == LogType.ERROR:
        resultText = f"{colorama.Fore.RED} [E] {text}"
    
    print(resultText, end=end)