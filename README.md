# Exam template

Detta är ett repo för en app som används för andra delen av examinationen i kursen "Testautomatisering och testverktyg".

Den som är intresserad av JavaScript och React är välkommen att ta del av koden, men det kommer inte hjälpa dig att lösa uppgiften. Använd i stället webbläsarens utvecklarläge och inspektera elementen på webbsidan, för att se vilka `testid` som används.

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

Behave läser konfigurationen från `.behaverc` och kör automatiskt alla `.feature`-filer i `frontend/src/features/`.

### 3. Kör en specifik feature-fil

```bash
behave frontend/src/features/katalog.feature
behave frontend/src/features/mina_bocker.feature
```

### 4. Kör ett specifikt scenario med taggar

Tagga ett scenario i din `.feature`-fil med t.ex. `@wip` och kör:

```bash
behave --tags @wip
```

### 5. Kör med verbose-utskrift

```bash
behave --format pretty
```

---

## Köra enhetstester (backend)

Kör från **projektets rotkatalog** (`testautomatisering_exam/`):

```bash
python -m pytest backend/tests/
```

Kör med verbose-utskrift:

```bash
python -m pytest backend/tests/ -v
```

Kör en specifik testfil:

```bash
python -m pytest backend/tests/test_bookstore.py
python -m pytest backend/tests/test_favoritebooks.py
python -m pytest backend/tests/test_integration.py
```

---

## Projektstruktur (frontend-tester)

```
frontend/
├── requirements.txt          # Python-beroenden
├── .behaverc                 # Behave-konfiguration
└── src/
    └── features/
        ├── environment.py    # Playwright setup/teardown
        ├── katalog.feature   # Feature-fil: Katalog
        ├── mina_bocker.feature # Feature-fil: Mina böcker
        ├── pages/            # Page Object-klasser
        │   ├── main_page.py
        │   ├── katalog_page.py
        │   └── mina_bocker_page.py
        └── steps/            # Step-implementationer
            ├── common_steps.py
            ├── katalog_steps.py
            └── mina_bocker_steps.py
```
