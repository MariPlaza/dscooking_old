# Natural Language Processing (NLP) for Recipes

## Motivation

In order to have a reliable training set, the database should contain several recipes. One of the best approaches to include several recipes is from the web using webscrapping and natural language processing (NLP) on recipes. 

## Required Implementation

The goal is being able to store recipes (with its corresponded link to the original source) into the database in order to use it as training set for the recommendation system to be implemented through Networks. 

It is important to have several sources, including several languages and recipes from several countries, in order to create a robust training set that allow to learn from different cultures. 

The following diagram represents the required implementation and the coding blocks to implement in order to achieve this goal:

![NLP Recipes Process](https://github.com/MariPlaza/dscooking/blob/master/NLP/NLP_Process.png)

For each recipe, the parser must recognized the following elements:

- Recipe's Name
- Servings or Portions
- Ingredients including name, quantity and unit of the ingredient. 
- Steps including name of the technique, ingredients involved, time that would take. 

Nutrition and total time of preparation are going to be calculated directly into the database. 

## Challenges

There are several previous experiences on the field (see resources), nonetheless, there are several challenges on it, specially when try to approach recipes that are not in english. 

- Language of the recipes e.g English, Spanish, German....
- Unstandard usage of ingredient names e.g. in german Paradiser or Tomaten, in spanish frutilla or fresa. 
- Unstandard usage of tecniques names
- Imprecise measures e.g. "bunch of", "pinch of"
- Units Standarization e.g. Oz vs grams. 
- Correct tagging ingredient or recipe name

## Approaches to deal with these challenges

For dealing with languages differences, 2 approaches are going to be considered:
1.- Translation from the language to english. 
2.- Direct training of the NLP models in the native language of the recipe. 

In order to have an accurate NLP each source is going to be treated like a class in Python and custom code would be developed to process the source with the higher possible accuracy. 

## Libraries

|Software   | Library Name| Usage  | 
|---|---|---|
|Python|NLTK|NLP techniques like Part of Speech (POS), entity detection, tokenization|
|Python|Beautifoul Soup|WebScrapping the sources|
|Python|sqlalchemy|Upload information in the database|
|Python|pandas|Information transformation for preparing to the structure into the database|
|Python|mtranslate|Translation from the original language to english|

## Resources

- [Graphical Recipe Automation](https://skemman.is/bitstream/1946/22240/1/kristinn_report.pdf)
- [Natural Language Processing in the kitchen](http://datadesk.latimes.com/posts/2013/12/natural-language-processing-in-the-kitchen/)
- [Chef Watson by KitchenPC](https://blog.kitchenpc.com/2011/07/06/chef-watson/)
