import argparse

# Vytvoření parseru
parser = argparse.ArgumentParser(description='Kompilace souboru.')

# Přidání argumentu
parser.add_argument('file', type=str, help='Soubor k kompilaci')

# Zpracování argumentů
args = parser.parse_args()

# Nyní můžete použít args.file pro přístup k názvu souboru
print(f'Kompilace souboru {args.file}')