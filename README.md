# DATA SCIENCE AND COOKING PROJECT


## MOTIVATION


Since the age of 6 I learnt to cook with my family and since then it has become my main hobby and passion. With the time I have developed curiosity about the diverse perspectives involved in the topic. As Production Engineer, I am also interested in the whole food production system and as a mom, I want to cook healthy and nutritious meals for my family. Combining my passion with my Data Science skills, I came up with this idea of analyzing cooking through the Data Science perspective. 

The data available allows different perspectives, but this concrete project focuses on creating two recommendation systems:

- **Healthy menus** that accomplish these criteria: affordable, nutritious, time manageable and into the taste preference of the person.
- **Recipe improver**  this could cover adapting a specific recipe to make it more nutritious, adapted to be suitable for any intolerance or allergy or personal preference (such as vegan or vegetarian)

## DATA SOURCES

The whole project has it owns database consolidating information from several open data sources. These data sources are disconnected, but the DB for the project built connections between them using criteria allowing a multiperspective analysis on Cooking and the food production system.  

These connections allow analysing factors like Cooking Techniques, Biology of Molecules, Economy - Costs, Personal Health, General Health and Analysis at a National Level. 

![Data Base Architecture](https://github.com/MariPlaza/dscooking/blob/master/Database_Architecture.png "Data Base Architecture")


For detail information on the architecture of the database and its sources refer to the [Data Sources Document](https://github.com/MariPlaza/dscooking/blob/master/DataSources.md)

## DATA SCIENCE APPROACHES USED INTO THE PROJECT: 

- **Natural Language Processing**: this technique is used in order to increase the numbers of recipes in the database which are going to be used as the training data to create the recommendation system. Although there are several libraries that help on this topic, the food context has several challenges. Please review the details [here](https://github.com/MariPlaza/dscooking/blob/master/Recipes_NLP.md)
- **Network Analysis**: this technique is used to analyse the recipes and to create a recommendation system for menus and recipe improvement. Please see the details [here](https://github.com/MariPlaza/dscooking/blob/master/Network_Analysis.md)

## COLLABORATORS:

This is a community project lead by [Mari Plaza](https://www.linkedin.com/in/maria-ines-plaza-schwarck-9825962/) as part of the **Data Science Cafe** of the [Vienna's Data Science Group](https://viennadatasciencegroup.at/). If you want to join it, please contact me through LinkedIn to include you in the SLACK Channel of the project. 

If you are a domain knowledge expert, please feel free to join as well, regardless of your experience in Data Science or technical fields. 

## RESOURCES: 

### DOMAIN KNOWLEDGE RESOURCES

Main Source:
- [Wageningen University & Research Edx courses](https://www.edx.org/school/wageningenx)
 
Specially for introductory concepts: 
- [Nutrition and Health: Macronutrients and Overnutrition](https://www.edx.org/course/nutrition-and-health-macronutrients-and-overnutrition)
- [Nutrition and Health: Micronutrients and Malnutrition](https://www.edx.org/course/nutrition-and-health-micronutrients-and-malnutrition)

Other Sources: 
- [Child Nutrition and Cooking from Standford University](https://www.coursera.org/learn/childnutrition)
- [Science and Cooking from Hardvard](https://www.edx.org/course/science-cooking-from-haute-cuisine-to-soft-matter-science-chemistry)
- [The Ethics of Eating from Cornell](https://www.edx.org/course/ethics-eating-cornellx-phil1440x)

### PREVIOUS PAPERS ON THE FIELD:

- [Flavor network and the principles of food pairing](https://www.nature.com/articles/srep00196)

### COMPANIES WORKING WITH DATA SCIENCE AND FOOD:

- [Food Integrity Studio](http://www.foodintegritystudio.com/)
- [Food Pairing](https://www.foodpairing.com/en/home)
- [Gracipe](http://www.gracipe.com/)

### GitHub Repositories: 

- [Flavor-Network](https://github.com/lingcheng99/Flavor-Network)
- [KitchenPC](https://github.com/KitchenPC/core)
