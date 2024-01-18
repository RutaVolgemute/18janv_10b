faila_nosaukums = "lietotajs.txt"
lietotaja_vards = input("Ievadiet savu vārdu: ")
try:
    with open(faila_nosaukums, "a") as fails:
        fails.write(lietotaja_vards + "\n")
    print(f"Lietotāja vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
except FileNotFoundError:
    print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
except IOError as e:
    print(f"Kļūda: Nevarēja ierakstīt failā '{faila_nosaukums}'. {e}")
except Exception as e:
    print(f"Nezināma kļūda: {e}")
