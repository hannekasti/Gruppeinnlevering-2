# IS-118 Gruppeoppgave 2


poeng = 0

print("Velkommen til Erlings prosjekt!")
print("Du er prosjektleder for en ny digital medborgerportal.")
print("Det er problemer i teamet, og du må ta noen valg.")
print("Prototypen skal være ferdig om tre uker.")
print("Velg A eller B for å spille videre.")


# Første beslutning
print("\nBESLUTNING 1")
print("Silje og Elias krangler om design og teknologi.")
print("Du må finne en måte å løse konflikten på.")
print("A: Snakke med Silje og Elias hver for seg.")
print("B: Samle hele teamet til et møte.")

valg1 = input("Hva velger du? A eller B: ").upper()

if valg1 == "A":
    print("Begge får forklare seg og føler seg hørt.")
    print("Samarbeidet blir bedre, men det tar tid.")
    poeng = poeng + 1

elif valg1 == "B":
    print("Teamet bestemmer en løsning sammen.")
    print("Arbeidet går raskere, men noen blir misfornøyde.")

else:
    print("Ugyldig valg. Du får ingen poeng.")


# Andre beslutning
print("\nBESLUTNING 2")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Hamdi ønsker en kontrollert løsning.")
print("Hallgeir ønsker at innbyggerne skal kunne delta mer fritt.")
print("A: Arrangere et møte mellom dem.")
print("B: Vente og se om de løser problemet selv.")

valg2 = input("Hva velger du? A eller B: ").upper()

if valg2 == "A":
    print("De snakker sammen og finner en løsning.")
    print("Konflikten blir mindre.")
    poeng = poeng + 1

elif valg2 == "B":
    print("Du velger å vente.")
    print("Uenigheten fortsetter og skaper problemer.")

else:
    print("Ugyldig valg. Du får ingen poeng.")


# Tredje beslutning
print("\nBESLUTNING 3")
print("Teamet begynner å miste motivasjonen.")
print("Samtidig nærmer fristen seg.")
print("A: Ha et møte og lage en plan sammen.")
print("B: Fokusere bare på å bli ferdig med prototypen.")

valg3 = input("Hva velger du? A eller B: ").upper()

if valg3 == "A":
    print("Teamet får bedre samarbeid og en tydelig plan.")
    print("Motivasjonen øker.")
    poeng = poeng + 1

elif valg3 == "B":
    print("Teamet jobber videre med prototypen.")
    print("Men samarbeidsproblemene blir ikke løst.")

else:
    print("Ugyldig valg. Du får ingen poeng.")


# Avslutning
print("\nSPILLET ER FERDIG!")
print("Du fikk", poeng, "poeng.")

if poeng == 3:
    print("Bra jobbet!")
    print("Teamet samarbeider godt og går mot norming-fasen.")

elif poeng == 2 or poeng == 1:
    print("Prosjektet går videre.")
    print("Noen konflikter er løst, men det er fortsatt problemer.")

else:
    print("Prosjektet har store problemer.")
    print("Samarbeidet er dårlig og prototypen kan bli forsinket.")

print("\nTakk for at du spilte!")