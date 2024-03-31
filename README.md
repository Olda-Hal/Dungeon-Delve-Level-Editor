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
The level structure is written in .DDS file format. 
this format is a simple text format that can be written in any text editor. it has the following structure:
every level is built from many code blocks. These code blocks are just a word followed with a colon and then the value of the code block. There are many possibilities for the value of the code block. this values is in a specific format:
```DDS
NAMEOFBLOCK: value
. example:
METADATA: "This is a simple level"
```
this values may be one of the following types:
1. string: a simple string. (this string is in a format of "string")
2. int: a simple integer. (this integer is in a format of 0)
3. float: a simple float. (this float is in a format of 0.0)
4. bool: a simple boolean. (this boolean is in a format of T or F)
5. list: a simple list. (this list is in a format of [value1, value2, value3, ...])
6. NONE: a simple none value. (this value is in a format of ---)
7. another code block with some subattributes. This codeblock has the same format as the main code block.

The format is as follows:
1. Header
    - every level file must have the LEVEL code block.
    - the LEVEL code block must have the following attributes:
        - METADATA: the metadata of the level. (string)
        - NAME: the name of the level. (string)
        - BACKGROUND: the background image of the level. (string)
        - BGTRANSPARENT: the background transparency. (bool)
        - SIZE: the size of the level. this has two subatributes:
            - X: the width of the level. (int)
            - Y: the height of the level. (int)
        - POS: the position of the level. this has two subatributes:
            - X: the x-coordinate of the level. (int)
            - Y: the y-coordinate of the level. (int)
        - MOVABLE: if the level is movable. (bool)
        - MENUS: the menus of the level. (list or NONE)



