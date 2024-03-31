# Dungeon Delve Level Compiler
This is a simple compiler for the Dungeon Delve Level format. You will have to write the level structure in .DDS file format and then compile it using this compiler. The compiler will generate a .json file which can be used in the game.

## How to use
1. Write the level structure in .DDS file format.
2. Build the compiler using the following command:
```bash
pip install pyinstaller
pyinstaller --onefile compiler.py
```
3. Run the compiler using the following command:
```bash
./dist/compiler <input_file> <output_file>
```
4. The output file will be generated in the same directory.

## Level Structure
The level structure is written in .DDS file format. The format is as follows:



