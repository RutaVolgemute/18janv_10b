def lasīt_datnī():
    try:
        with open("dati.txt", "r", encoding="utf-8") as datne:
            for x in datne:
                print(x)
    except FileNotFoundError:
        print("Datne nav atrasta!")
if __name__=="__main__":
    lasīt_datnī()