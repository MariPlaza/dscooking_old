import requests
import re
from bs4 import BeautifulSoup

def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

class Tasty(object):
    """Recipes presented at the webpage https://tasty.co/. Tasty objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A dictionary with the ingredients lists.
        steps: A dictionary with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
    """
    language = 'en'
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link #https://tasty.co/recipe/stars-and-stripes-smores-cups
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        base_divs = soup.find_all("div", class_="content-wrap")[1].find_all("div", class_="recipe-content")[0].find_all("div", class_="ingredients-prep")
        recipe_divs = base_divs[0].findChildren()
        self.servings = int(find_between(recipe_divs[2].text, "for ", " "))
        ing_list = recipe_divs[0].find_all('li')
        for ing in ing_list:
            self.ingredients.append(ing.text)
        prep_divs = soup.find_all("div", class_="content-wrap")[1].find_all("div", class_="recipe-content")[0].find_all("div", class_="ingredients-prep")[0].find_all("div", class_="prep")
        step_lists = prep_divs[0].find_all('li')
        for step in step_lists:
            self.steps.append(step.text) 
        return self.name

class Ich_Koche(object):
    """Recipes presented at the webpage https://www.ichkoche.at/. Ich_Koche objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A dictionary with the ingredients lists.
        steps: A dictionary with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
    """
    language = 'de'
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link #https://www.ichkoche.at/eiersalat-mit-erdaepfeln-rezept-194521
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("div[class*=portionArea]")
        if len(portion)>0:
            self.servings = int(find_between(portion[0].text, "Portionen: ", "\n"))
        ingredients_div = soup.select("div[class*=ingredients]") 
        ingredient_li = ingredients_div[0].find_all('li')
        for ing in ingredient_li:
            int_list = []
            for span in ing.find_all('span'):
                int_list.append(span.text)
            self.ingredients.append(' '.join(int_list))
        steps_div = soup.select("div[class*=description]")
        steps_p = steps_div[0].find_all(['p', 'h3'])
        for step in steps_p:
            if step.text =='Tipp':
                break
            if step.text != ' ':
                self.steps.append(step.text)
        return self.name
