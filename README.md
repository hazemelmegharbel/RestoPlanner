# Vancouver Business Planner
This program is designed to help guide entrepeneurs that plan to establish a new amenity in the Vancouver region. 

_Refer to the header comment of any file to see a short description of its purpose._

## Run the program
While in the root directory, run the following command: 
```
python3 main.py
```
The prompts will guide you on the necessary inputs as you go along.
* Note: when entering the full name of an amenity, include the underscore used to join words.<br/>
(e.g. type `fast_food` as opposed to `fast food`)

### Sample input sequence:
1. Prompt: `Please enter the number of your choice:` <br/>
Input: `3`
2. Prompt: `Input your search phrase:` <br/>
Input: `ar`
3. Prompt: `Please enter one amenity/business that you would like to open:` <br/>
Input: `restaurant`
4. Prompt: `Enter latitude:` <br/>
Input: `49.26076`
4. Prompt: `Enter longitude:` <br/>
Input: `-123.1154`

## Run the models
While in the root directory, run the following commands: 
```
python3 human_model.py
python3 computer_model_forest.py
```
The cluster graphs will be output in the same directory.

## Pre-generated files
The `/generate_datasets` directory contains CSV files generated by us beforehand, so that they do not have to be processed repeatedly when the program is run multiple times. Here is a list of the outputs generated by each file:

- `main.py` : calls on `densities.py`, `feature_eng.py`, and `food_chains.py` <br/>
    Outputs:
    - `amenity_densities.csv`
    - `computer_model_data.csv`
    - `restaurant_data.csv`
    - `wiki_foodchains.csv`
- `tripadvisor_ratings.py` : uses Spark to process `dataset_tripadvisor.json` <br/>
    Outputs:
    - `dataset_tripadvisor_clean.csv`

### How the files are generated
While in the `generate_datasets` directory, run the following commands: 
```
spark-submit tripadvisor_ratings.py
python3 main.py
```
