1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
- **Enhetstester** testar en liten del av koden - ofta en funktion eller en klass. Vi testar en sak åt gången.
- **Integrationstest** är en nivå större än enhetstest och testar om flera delar jobbar tillsammans bra. Vi testar att olika komponenter i systemet fungerar tillsammans korrekt.
- **Regressionstest** används när en ny version av koden kommer ut då kör vi gamla tester igen för att säkerställa att vi inte bröt något som fungerade innan. Alla tidigare tester är regressionstest när vi kör dem igen.
- **Prestandatest** testar om systemet är snabbt nog genom att mäta tid, minne, osv. Till exempel: "Kan systemet hantera många användare samtidigt utan att bli långsamt?"

---

2. Beskriv hur det går till när man arbetar med TDD.

   TDD betyder Test Driven Development. Det går så här:
- **Steg 1:** Vi skriver ett tester för funktionalitet som inte finns än. Tester failar eftersom koden inte finns
- **Steg 2:** Vi skriver logik med kod för att testet ska passa
- **Steg 3:** Sedan vi kan refactorera koden med tanke att vi vet att testet fortfarande passar eftersom vi kan köra det igen
- Vi upprepar dessa tre steg för varje ny funktion

---
3. Beskriv hur BDD skiljer sig från TDD.

   **BDD** betyder Behavior Driven Development.
   BDD fokuserar på vad systemet gör ur användarens perspektiv genom att beskriva vad som ska hända. BDD tester är på ett språk som alla kan förstå egentligen använder ofta Gherkin-språk (Given-When-Then)
   medan **TDD** fokuserar på hur koden fungerar i teknisk nivå och skrivs av utvecklare för utvecklare.

---
4. Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

   Jag skulle använda en blandning av alla dessa tester för att få en tillräcklig bra täckning från flera nivåer.
   För det första skulle jag använda **enhetstester** för att testa varje funktion i koden. Enhetstester är väldigt snabba och enkla att köra och vi behöver veta att grundfunktionaliteten fungerar innan vi testar något större. Vi testar att varje enskild funktion på backend/frontend gör precis vad den ska.
   För det andra skulle jag använda **integrationstester**. Integrationstester testar att olika delar av systemet arbetar tillsammans korrekt. Enhetstester räcker inte - vi behöver veta att de olika delarna av systemet fungerar tillsammans och inte bara var för sig.
   För det tredje skulle jag använda **BDD-tester** på frontend-sidan. Dessa tester fokuserar på användarflödet och testar det som är viktigt för användaren. BDD använder ett språk som alla förstår och det säger vad användaren kan göra och det är det viktigaste.
   Sista delen är **regressionstest** som innebär att vi kör alla tester varje gång vi gör en ändring i koden. Med flera ändringar är det lätt att förstöra något gammalt så regressionstest säkerställer att vi inte bröt något.

