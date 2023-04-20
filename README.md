# sandwich-generator
A sandwich generator

![](https://raw.githubusercontent.com/psibir/demonstrations/main/sandwich-generator%20demo.gif)


## Description
This is a Python program that generates a sandwich recipe by randomly selecting ingredients from a CSV file. The program ensures that only a specific number of each ingredient type can be added to the sandwich.

## Business Use Case
This program could be used by restaurants or cafes to generate unique sandwich recipes for their menu. By selecting ingredients at random, it ensures that each sandwich is different and can provide customers with a unique experience.

## Prerequisites
To run this program, you will need:

* Python 3.x
* A CSV file containing sandwich ingredients

### CSV Specifications
The ```ingredients.csv``` file used by the program requires four columns with specific headers: "Cheeses", "Meats", "Vegetables", and "Condiments". These columns should contain a list of ingredients for each category, with each ingredient listed on a separate row. The program will read this file to generate a random sandwich containing a maximum of two cheeses, two meats, two vegetables, and one condiment. It is important to note that the headers must be spelled and capitalized exactly as shown, and the columns must be in the order specified for the program to work correctly. Additionally, each ingredient should only be listed once in the file, as the program will automatically filter out any duplicates.

## Installation

1. Clone the repository:
```
git clone https://github.com/psibir/sandwich-generator.git
```

2. Change directory:
```
cd sandwich-generator
```

3. Place your CSV file in the project directory and name it ```ingredients.csv```.


## Usage

Run ```main.py```:
```
python3 main.py
```
