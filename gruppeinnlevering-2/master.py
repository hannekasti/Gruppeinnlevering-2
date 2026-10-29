poeng = 0
print("""
Velkommen til Erlings prosjekt!

Seks uker har gått siden Erling startet utviklingen av kommunens nye digitale medborgerportal.

Prosjektgruppen opplever nå konflikter og samarbeidsproblemer. Silje og Elias er uenige om design og teknologi, mens Hamdi og Hallgeir har ulike meninger om hvordan innbyggerne skal delta i digitale folkemøter.

Den første prototypen skal leveres om tre uker.

Du spiller som Erling, prosjektlederen. Gjennom tre viktige beslutninger skal du forsøke å sikre både fremdrift og samarbeid.

""")

print ("""
BESLUTNING 1: Konflikten mellom Silje og Elias

Silje og Elias er uenige om hvilken teknologisk løsning
som skal brukes i medborgerportalen.

Konflikten har utviklet seg fra en faglig uenighet til
en personkonflikt. Begge søker støtte hos andre i teamet.

Erling må bestemme hvordan konflikten skal håndteres.

A: Gjennomføre individuelle samtaler med Silje og Elias.
B: Samle hele teamet til et felles møte.
""")

valg1 = input("Hva velger du? (A/B): ").strip().upper()

while valg1 != "A" and valg1 != "B":
    print("Ugyldig valg. Vennligst velg A eller B.")
    valg1 = input("Hva velger du? (A/B): ").strip().upper()

if valg1 == "A":
        print("""Erling gjennomfører individuelle samtaler med Silje og Elias. Begge får forklare sitt syn, og det åpnes for et kompromiss. Samarbeidet kan forbedres, men prosessen tar verdifull tid fra utviklingen.""")
elif valg1 == "B":
        print("""Erling samler hele teamet til et møte. Etter diskusjon blir retningen bestemt gjennom en avstemning. Prosjektet får raskere fremdrift, men noen gruppemedlemmer føler seg overkjørt, og motivasjonen svekkes.""")
        poeng +=1

print ("""
BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir

En ny konflikt er i ferd med å utvikle seg i prosjektgruppen.

Hamdi ønsker å bruke kommunens eksisterende plattform
til digitale folkemøter, mens Hallgeir ønsker en mer åpen
løsning hvor innbyggerne kan komme med spontane innspill.

Uenigheten er foreløpig liten, men frustrasjonen vokser.
Erling må avgjøre om han skal gripe inn eller avvente.

A: Innkalle Hamdi og Hallgeir til et felles møte.
B: Avvente situasjonen og la dem forsøke å løse konflikten selv.
""")

valg2 = input("Hva velger du (A/B): ").strip().upper()

while valg2 != "A" and valg2 != "B":
    print("ugyldig valg. Vennligst velg A eller B.")
    valg2 = input("Hva velger du (A/B): ").strip().upper()

if valg2 == "A":
         print("""Erling innkaller Hamdi og Hallgeir til et møte. Begge får forklare sine synspunkter, og etter en konstruktiv diskusjon finner de en løsning begge kan akseptere. Samarbeidet styrkes, men møtet tar tid fra utviklingsarbeidet.""")
         poeng +=1
elif valg2 == "B":
         print("""Erling velger å ikke gripe inn. Teamet sparer tid på kort sikt, men uenigheten mellom Hamdi og Hallgeir fortsetter. Frustrasjonen øker, samarbeidet blir vanskeligere, og prosjektet risikerer forsinkelser.""")

print ("""
BESLUTNING 3: Motivasjonen i prosjektgruppen

Konfliktene har begynt å påvirke hele prosjektgruppen.
Flere gruppemedlemmer opplever mindre motivasjon, og
samarbeidet er ikke like godt som tidligere.

Samtidig nærmer fristen for den første prototypen seg.
Erling må balansere behovet for godt samarbeid med
behovet for å levere prosjektet i tide.

A: Gjennomføre et kort møte for å forbedre samarbeidet
   og lage en tydelig plan frem mot prototypefristen.

B: Prioritere utviklingsarbeidet og utsette
   samarbeidsproblemene til etter leveransen.
""")

valg3 = input("Hva velger du (A/B): ").strip().upper()

while valg3 != "A" and valg3 != "B":
    print("ugyldig valg. Vennligst velg A eller B.")
    valg3 = input("Hva velger du (A/B): ").strip().upper()

if valg3 == "A":
        print("""Erling samler prosjektgruppen til et kort møte. Teamet diskuterer utfordringene og lager en tydelig plan for arbeidet frem mot prototypefristen. Dette styrker motivasjonen og skaper en felles retning, men møtet tar noe tid fra utviklingsarbeidet.""")
        poeng += 1
elif valg3 == "B":
        print("""Erling bestemmer at teamet skal konsentrere seg om å ferdigstille prototypen. Utviklingsarbeidet fortsetter uten avbrudd, men de uløste samarbeidsproblemene skaper økende frustrasjon. Motivasjonen svekkes, og prosjektet risikerer forsinkelser.""")

print("Du fikk", poeng, "poeng!")
if poeng == 3:
           print("Teamet gjenoppretter tilliten og går videre mot norming-fasen.")
elif poeng >= 1:
           print("Teamet har fortsatt noen utfordringer, men samarbeidet forbedres gradvis.")
else:
           print("Teamet har fortsatt betydelige samarbeidsproblemer, og prosjektet risikerer forsinkelser.")

print("\nTakk for at du spilte!")
