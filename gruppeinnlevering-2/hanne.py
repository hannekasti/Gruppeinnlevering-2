# -------------Gruppeinnlevering 2-------------

print("Erling trenger hjelp til å velge hvordan han skal håndtere konfliktene som har oppstått!")

print("================================================")


print(
    "\nDet har gått seks uker siden prosjektet startet opp, "
    "og det har begynt å murre innad i prosjektgruppa. Erling står overfor flere utfordringer " \
    "han må håndtere i tiden framover. " 
)

poeng = 0

print(
    "\nHovedutfordring 1: Konflikten mellom Silje og Elias har utviklet seg " 
    "fra å være en sakskonflikt til å bli en personkonflikt. " 
    "Konflikten bunner i en uenighet om teknologivalg og design.\n" 
)


print("================================================")


Hovedutfordring_1 = input("\nErling har to valgmuligheter i denne situasjonen: "
                    "individuelle samtaler (A) eller felles møte (B) ")

if Hovedutfordring_1 == "A":
    print(f"\nErling velger å innkalle Silje og Elias til individuelle samtaler {Hovedutfordring_1}.")
    print("Individuelle samtaler kan være enn god løsning hvor Erling får mulighet til å få innsikt i konflikten fra begge sider. " 
    "Risikoen ved denne løsningen er at gruppen ikke rekker å bli ferdig med prototypen innen oppsatt tidsfrist.\n")
elif Hovedutfordring_1 == "B":
    print(f"\nErling velger å innkalle til et felles møte {Hovedutfordring_1}.")
    print("Et felles møte kan være en god løsning, fordi det åpner kommunikasjonen og skaper høy effektivitet i prosjektarbeidet. "
    "Risikoen ved denne løsningen er at gruppemedlemmene kan oppleve nedsatt motivasjon og trivsel i arbeidsgruppa.\n")
    poeng += 1
else:
    print("Ugyldig valg. Velg enten A eller B.")


print("================================================")


print(
    "\nHovedutfordring 2: Konflikten mellom Hamdi og Hallgeir er foreløpig lavmælt, "
    "men Erling merker at frustrasjonen vokser. Den ulmende konflikten "
    "bunner i en uenighet om hvordan innbyggerne skal kunne delta i digitale "
    "folkemøter."
)


Hovedutfordring_2 = input("Erling har to valgmuligheter i denne situasjonen:" \
                    "felles samtale (A) eller vente og se (B) ")



if Hovedutfordring_2 == "A":
    print(f"\nErling velger å innkalle Hamdi og Hallgeir til en felles samtale {Hovedutfordring_2}.")
    print("En felles samtale kan være en god løsning i denne situasjonen, fordi begge parter får mulighet til å dele sine synspunkt." \
    "Risikoen er at slike samtaler kan ta lang tid, og gå utover prosjektarbeidet.\n")
    poeng += 1
elif Hovedutfordring_2 == "B":
    print(f"\nErling avventer situasjonen, og ser om konflikten går over av seg selv {Hovedutfordring_2}.")
    print("Å vente og se kan være en god løsning, det kan jo hende at Hamdi og Hallgeir finner en løsning på egenhånd. " \
    "Risikoen er at konflikten eskalerer, som igjen går utover prosjektarbeidet.\n")
else:
    print("Ugyldig valg. Velg enten A eller B.")


print("================================================")


print(
    "\nHovedutfordring 3: Konfliktene i prosjektgruppa kan påvirke motivasjonen "
    "til hele teamet, også de som ikke er direkte involvert. Erling må finne ut "
    "hvordan han skal bevare motivasjonen i teamet som helhet." 
)



Hovedutfordring_3 = input("Erling har to valgmuligheter i denne situasjonen: " \
                    "forbedre samarbeidet (A) eller prioritere fremdrift (B) ")


if Hovedutfordring_3 == "A":
    print(f"\nErling velger å fokusere på å forbedre samarbeidet i teamet {Hovedutfordring_3}.")
    print("Å fokusere på å forbedre samarbeidet i teamet kan være en god løsning, fordi det bidrar til å skape et mer positivt arbeidsmiljø, " \
    "som igjen vil påvirke motivasjonen og trivselen til gruppemedlemmene. Risikoen er at det er tidkrevende, og dermed påvirker fremdriften " \
    "i prosjektet.\n")
    poeng += 1
elif Hovedutfordring_3 == "B":
    print(f"\nErling velger å prioritere fremdrift i prosjektet {Hovedutfordring_3}.")
    print("Å prioritere fremdrift i prosjektet kan være en god løsning, fordi det sikrer at prosjektet blir levert til oppsatt tidsfrist. " \
    "Risikoen er at det kan påvirke motivasjon og tillit i prosjektgruppa negativt.\n")
else:
    print("Ugyldig valg. Velg enten A eller B.")



# --------- Endelig resultat ---------

print("================================================")


print(f"\nDu har fått {poeng} av 3 mulige poeng!")

if poeng == 3:
    print("Prosjektgruppa løser konfliktene og går inn i normingfasen.")
elif poeng >= 1:
    print("Prosjektgruppa løser konfliktene delvis, de oppplever fortsatt noen uenigheter og utfordringer med motivasjon. " \
    "De jobber likevel godt nok sammen til at prototypen kan leveres.")
else:
    print("Prosjektgruppa løser ikke konfliktene, og prototypen blir forsinket.")






