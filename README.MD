# Symmetrische Encryptie Applicatie

Een Python applicatie voor het veilig versleutelen en ontsleutelen van tekst met AES-256-GCM

## Installatie

```bash
pip install cryptography
```

## Gebruik

Start de applicatie:

```bash
python cli.py
```

### Menu Opties

1. **Genereer nieuwe sleutel** - Maakt een veilige 256-bit sleutel
2. **Versleutel tekst** - Versleutel je bericht met een sleutel
3. **Ontsleutel tekst** - Ontsleutel een bericht met de juiste sleutel
4. **Exit** - Sluit de applicatie

## Technische Details

- **Algoritme**: AES-256-GCM (Authenticated encryption)
- **Sleutellengte**: 256 bits (32 bytes)
- **Mode**: Galois/counter mode met authenticatie
- **Library**: Python cryptography

## Bestanden

- `cli.py` - Command line interface
- `crypto_utils.py` - encryptie functionaliteiten
- `test_crypto.py` - Unit tests
- `README.md` - Dit bestand

## Kerckhoffs's Principe

Deze applicatie volgt Kerckhoffs's principe: de veiligheid ligt volledig in de geheime sleutel, niet in het algoritme. Alle code is openbaar, alleen de sleutel moet geheim blijven.

## Veiligheid

**Belangrijk**:

- Bewaar sleutels veilig
- Deel sleutels alleen via veilige kanalen
- Zonder de juiste sleutel is decryptie onmogelijk

## Tests

Run de tests:

```bash
python test_crypto.py
```

## Auteur

Caner Kümür
