import argparse
import decompositor
# Vytvoření parseru
parser = argparse.ArgumentParser(description='Dungeon Delve Script Compiler')

# Přidání argumentu
parser.add_argument('file', type=str, help='File to compile')

# Zpracování argumentů
args = parser.parse_args()

if args.file is None:
    print('File for compilation not specified. Exiting.')
    exit(1)
else:
    decompositor.main(args)


# Nyní můžete použít args.file pro přístup k názvu souboru
print(f'Kompilace souboru {args.file}')