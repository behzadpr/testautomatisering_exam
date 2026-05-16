# Exam template

Detta är ett repo för en app som används för andra delen av examinationen i kursen "Testautomatisering och testverktyg".

## Läslistan

Denna webbsida ska testas med Python, Playwright och behave.

Länk till uppgiftsbeskrivningen hittar du i kursens veckoschema.

Appen är publicerad med GitHub Pages. Använd den här länken för att köra dina tester: [https://tap-ht25-testverktyg.github.io/exam/](https://tap-ht25-testverktyg.github.io/exam/)

---

## Köra testerna

### Förutsättningar

- Python 3.x installerat
- `pip` tillgängligt i terminalen

### 1. Installera beroenden

Installera alla Python-paket från `requirements.txt`:

```bash
pip install -r frontend/requirements.txt
```

Installera sedan Playwright-webbläsarna:

```bash
playwright install
```

### 2. Kör alla tester

Kör testerna från **projektets rotkatalog** (`testautomatisering_exam/`):

```bash
behave
```

Behave läser konfigurationen från `behave.ini` och kör automatiskt alla `.feature`-filer i `frontend/src/features/`.

### 3. Kör en specifik feature-fil

```bash
behave frontend/src/features/katalog.feature
```
---

## Köra enhetstester (backend)

Kör från **projektets rotkatalog** (`testautomatisering_exam/`):

```bash
python -m pytest backend/tests/
```

Kör en specifik testfil:

```bash
python -m pytest backend/tests/test_bookstore.py
python -m pytest backend/tests/test_integration.py
```

---

## Projektstruktur (frontend-tester)

```
frontend/
├── requirements.txt          # Python-beroenden
└── src/
    └── features/
        ├── environment.py    # Playwright setup/teardown (5s timeout)
        ├── katalog.feature   # Feature-fil: Katalog
        ├── lagg_till_bok.feature  # Feature-fil: Lägg till bok
        ├── mina_bocker.feature    # Feature-fil: Mina böcker
        ├── statistik.feature      # Feature-fil: Statistik
        ├── pages/            # Page Object-klasser
        │   ├── main_page.py
        │   ├── katalog_page.py
        │   ├── lagg_till_bok_page.py
        │   ├── mina_bocker_page.py
        │   └── statistik_page.py
        └── steps/            # Step-implementationer
            ├── common_steps.py
            ├── katalog_steps.py
            ├── lagg_till_bok_steps.py
            ├── mina_bocker_steps.py
            └── statistik_steps.py
```

---

## Test Coverage

### Frontend BDD-tester (Behave)
- **katalog.feature**: Katalogvyn 
- **lagg_till_bok.feature**: Lägg till bok-vyn 
- **mina_bocker.feature**: Mina böcker-vyn 
- **statistik.feature**: Statistik-vyn 

### Backend Unit-tester (pytest)
- `test_bookstore.py`: Bookstore-klassens funktionalitet
- `test_favoritebooks.py`: FavoriteBooks-klassens funktionalitet  
- `test_integration.py`: Integrationstest mellan komponenter

