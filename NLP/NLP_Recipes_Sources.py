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

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


class Tasty(object):
    """Recipes presented at the webpage https://tasty.co/. Tasty objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
    NLP Challenges:
        There are recipes without the ingredient quantity
        Units in Oz but also include grams
        Time is not always specified. 
        It doesn't have the recipe category
    """
    language = 'en'
    Recipe_Category = 'Undefined'
    Recipe_Region = 'Undefined'
    ID_Source = 31
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
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
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
    NLP Challenges
        Not always have servings or proportions.
        In German
        Time is not always specified
    """
    language = 'de'
    ID_Source = 32
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'
        self.Recipe_Category = 'Undefined'
        self.Recipe_Region = 'Austria'
        
    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("div[class*=portionArea]")
        #category = soup.select("a[itemprop*=recipeCategory]")
        #if len(category)>0:
        #    self.Recipe_Category = category[0].text
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

class Recetas_Gratis(object):
    """Recipes presented at the webpage https://www.recetasgratis.net/. Recetas_Gratis objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
        Region: Country of the recipe
        Category: 
        ID_Source: The equivalent of this source in the database
    NLP Challenges:
        There are recipes without the ingredient quantity
        Language spanish
        Time is not always specified. 
    """
    language = 'es'
    Recipe_Region = 'Undefined'
    ID_Source = 33
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Recipe_Category = 'Undefined'
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("div[class*=properties]")
        self.servings = int(portion[0].select("span[class*=comensales]")[0].text.replace(' comensales',''))
        self.Recipe_Category = portion[0].select("span[class*=para]")[0].text
        ingredients_div = soup.select("div[class*=ingredientes]") 
        ingredient_li = ingredients_div[0].find_all('label')
        for ing in ingredient_li:
            self.ingredients.append(ing.text.replace('\n',''))
        steps_div = soup.select("div[class*=apartado]")
        steps_div = steps_div[:len(steps_div)-2]
        for step in steps_div:
            self.steps.append(step.find('p').text)
        return self.name

class Cookpad_US(object):
    """Recipes presented at the webpage https://cookpad.com/us. Cookpad_US objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
        Region: Country of the recipe
        Category: 
        ID_Source: The equivalent of this source in the database
    NLP Challenges:
        There are recipes without the ingredient quantity
        Units in Oz but also include grams.
        Not always have servings or proportions.    
        Time is not always specified. 
        It doesn't have the recipe category
    """
    language = 'en'
    Recipe_Category = 'Undefined'
    Recipe_Region = 'Undefined'
    ID_Source = 34
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("div[id*=serving_recipe]")
        if hasNumbers(portion[0].text):
            self.servings = int(re.search(r'\d', portion[0].text).group(0))
        ingredients_div = soup.select("div[class*=ingredient-list]") 
        ingredient_li = ingredients_div[0].find_all('li')
        for ing in ingredient_li:
            self.ingredients.append(ing.select("div[class*=ingredient__details]")[0].text.replace('\n',''))
        steps_div = soup.select("div[class*=numbered-list]")
        for step in steps_div:
            self.steps.append(step.find('p').text)
        return self.name

class Cookpad_ES(object):
    """Recipes presented at the webpage https://cookpad.com/es. Cookpad_ES has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
        Region: Country of the recipe
        Category: 
        ID_Source: The equivalent of this source in the database
    NLP Challenges:
        There are recipes without the ingredient quantity
        Language Spanish
        Units in Oz but also include grams.
        Not always have servings or proportions.    
        Time is not always specified. 
        It doesn't have the recipe category
    """
    language = 'es'
    Recipe_Category = 'Undefined'
    Recipe_Region = 'Undefined'
    ID_Source = 35
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("div[id*=serving_recipe]")
        if hasNumbers(portion[0].text):
            self.servings = int(re.search(r'\d', portion[0].text).group(0))
        ingredients_div = soup.select("div[class*=ingredient-list]") 
        ingredient_li = ingredients_div[0].find_all('li')
        for ing in ingredient_li:
            self.ingredients.append(ing.select("div[class*=ingredient__details]")[0].text.replace('\n',''))
        steps_div = soup.select("div[class*=numbered-list]")
        for step in steps_div:
            self.steps.append(step.find('p').text)
        return self.name

class Hoy_que_comemos(object):
    """Recipes presented at the webpage https://yhoyquecomemos.com/. Hoy_que_comemos objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
        Region: Country of the recipe
        Category: 
        ID_Source: The equivalent of this source in the database
    NLP Challenges:
        There are recipes without the ingredient quantity
        Language Spanish
        Not always have servings or proportions.    
        Time is not always specified. 
        It doesn't have the recipe category
    """
    language = 'es'
    Recipe_Category = 'Undefined'
    Recipe_Region = 'Undefined'
    ID_Source = 36
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'

    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        extra_info = soup.select("ul[class*=recipe-cat-info]")
        base_info  = soup.select("div[itemprop*=description]") 
        if hasNumbers(base_info[0].find('h2').text):
            self.servings = int(re.search(r'\d', base_info[0].find('h2').text).group(0))
        ingredient_li = base_info[0].find_all('li')
        for ing in ingredient_li:
            if ing.has_attr('class'):
                continue
            self.ingredients.append(ing.text)
        steps_p = base_info[0].find_all('p')
        steps_p.pop(0)
        for step in steps_p:
            if step.has_attr('img'):
                continue
            if step.has_attr('style'):
                continue
            if len(step.text)>0:
                self.steps.append(step.text)
        return self.name

class Gute_Kueche(object):
    """Recipes presented at the webpage https://www.gutekueche.at/. Gute_Kueche objects has the following properties:
    Attributes:
        name: A string representing the recipe's original name. This correspond to the Recipe_Original_Name into the master_recipe table. 
        link: representing the exact link of the recipe. This corresponds to the Recipe_Link field into the master_recipe table.
        servings: An integer representing the number of portions for this recipe. This corresponds to the Recipe_Portions field into the master_recipe table.
        ingredients: A list with the ingredients lists.
        steps: A list with the recipe steps. 
        Image: Represents the picture of the recipe. It is stored in the field Recipe_Image_Link into the master_recipe table. 
    NLP Challenges
        In German
        Time is not always specified
    """
    language = 'de'
    ID_Source = 37
    def __init__(self, link, servings=1):
        """Return a Tasty object whose link is link, name is the last part of the link 
        and serving is by default 1 but it should be adapted after webscrapping the recipe"""
        self.link = link
        self.name = link 
        self.servings = servings
        self.ingredients = []
        self.steps = []
        self.Image = 'http://www.euforgen.org/fileadmin/templates/euforgen.org/Site/img/picture-not-available.jpg'
        self.Recipe_Category = 'Undefined'
        self.Recipe_Region = 'Austria'
        
    def web_scrapp(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text,'lxml')
        self.name = soup.title.text
        portion = soup.select("input[id*=portions]")
        self.servings = int(portion[0]['value'])
        ingredients_div = soup.select("tr[itemprop*=ingredients]") 
        for ing in ingredients_div:
            self.ingredients.append(re.sub(' +',' ',ing.text.replace('\n',' ')))
        steps_div = soup.select("section[itemprop*=recipeInstructions]")
        for step in steps_div[0].find_all('li'):
            self.steps.append(step.text)
        return self.name

