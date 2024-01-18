try:
    faila_nosaukums = input("Ievadiet faila nosaukumu (piemēram, fails): ")
    paplasinajums = input("Ievadiet faila paplašinājumu (piemēram, txt): ")
    faila_ceels = f"{faila_nosaukums}.{paplasinajums}"
    with open(faila_ceels, 'r') as fails:
        faila_saturs = fails.read()

    print(f"\nFaila '{faila_ceels}' saturs:\n")
    print(faila_saturs)

except FileNotFoundError:
    print(f"Kļūda: Fails '{faila_ceels}' nav atrasts.")
except PermissionError:
    print(f"Kļūda: Nav atļaujas lasīt failu '{faila_ceels}'.")
except Exception as e:
    print(f"Nezināma kļūda: {e}")