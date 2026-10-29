print("HJELP ERLING MED Å VELGE")

print("....................................................")

print("\nErling jobber som prosjektleder for utviklingen av kommunens nye digitale medborgerportal. "
    "Prosjektgruppen består av mennesker fra syv ulike grupper: Erling, Sivert og Elias, Silje, Hamdi, "
    "Marcia, Noa, Hallgeir og Jabir. De har jobbet god sammen i seks uker men nå har prosjektet gått inn "
    "i storming-fasen og gruppen står overfor konflikter. Du skal nå hjelpe Erling med å velge hva han "
    "skal gjøre i de ulike konfliktene.")

poeng = 0

# ........ Situasjon 1 ........

print("....................................................")

print("\nSituasjon 1: Silje og Elias er uenige om teknologivalg og design og uenighet har utviklet seg "
    "fra en sakskonflikt til en personkonflikt. \n"
    "Erling kan enten ta opp konflikten i individuelle samtaler eller i felles møte. \n")

situasjon1 = input("Skal Erling ta det opp i individuelle samtaler (individuelt) eller i plenum (plenum): ")

if situasjon1 == "individuelt":
    print(f"\nVed å velge {situasjon1} kan Erling få en forståelse av begge sider men strategien har en risko "
        "for at gruppen ikke leverer prototypen i tide.")

elif situasjon1 == "plenum":
    print(f"\nVed å ha en {situasjon1} møte kan det øke åpen kommunikasjon og høy effektivitet men det "
         "kan også ha negativ effekt på gruppemedlemmens motivasjon og trivsel i arbeidet.")
    poeng += 1 

else:
    print("\nDu har skrevet noe feil, start programmet på nytt.")

# ........ Situasjon 2 ........

print("....................................................")

print("\nSituasjon 2: Hamdi og Hallgeir er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. " 
    "Erling merker at frustrasjonen vokser selv om uenigheten er lavmælt. Første prototype skal være klar om tre uker. " 
    "Erling kan ha en felles samtale med Hamdi og Hallgeir eller håpe at de løser uenigheten selv. ")

situasjon2 = input("\nSkal Erling ha en felles samtale (felles samtale) eller vente og se hva som skjer (vente)...: ")

if situasjon2 == "felles samtale":
    print(f"\nVed å ha en {situasjon2} kan begge forklare sine synspunkter men møtene krever mer tid.")
    poeng += 1

elif situasjon2 == "vente":
    print(f"\nVed å velge å {situasjon2} kan gruppen spare tid men det øker en risiko for at konflikten utvikler seg videre.")

else:
    print("\nDu har skrevet noe feil, start programmet på nytt.")

# ........ Situasjon 3 ........

print("....................................................")

print("\nSituasjon 3: Konfliktene har påvirket motivasjonen i hele gruppen og stemningen er spente. Erling kan bestemme " 
     "å ha et felles møte der gruppen avklarer utfordringer i samarbeidet eller utsette samarbeidsproblemene og "
     "konsentrere innsatsen om å ferdigstille prototypen. ")
      
situasjon3 = input("\nSkal Erling fokusere å forbedre samarbeidet (samarbeid) eller prioritere fremdrift (fremdrift): ")

if situasjon3 == "samarbeid":
    print(f"\nVed å velge å fokusere på {situasjon3} kan gruppen styrke motivasjon og forståelse av hva de skal prioritete "
        "men møtet tar tid og kan bringe flere uenigheter. ")
    poeng += 1

elif situasjon3 == "fremdrift":
    print(f"\nVed å velge {situasjon3} har gruppen mer tid til utvikling av prototypen men uløste konfliktene kan "
        "forsterkes og svekke både tilliten og produktiviteten. ")

else:
    print("\nDu har skrevet noe feil, start programmet på nytt.")

# ........ Resultatene ........

print("....................................................")

print("\nResultatene:")

print(f"\nDu fikk: {poeng}/3")

if poeng == 3:
    print("\nProsjektgruppen løser konfliktene og går videre mot norming-fasen.")

elif poeng >= 1:
    print("\nProsjektgruppen har fortsatt noen uenigheter og utfordringer med motivasjon "
        "men de jobber sammen til å bli klar med prototypen.")

else:
    print("\nProsjektgruppen har fortsatt konfliktene og prosjektet forsinkes.")