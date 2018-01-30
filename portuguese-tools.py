# import necessary modules
import pandas as pd
import numpy as np

# list endings for regular verbs
present_indicative = {"name": "present_indicative",
                      "ar": ["o", "amos", "as", "ais", "a", "am"],
                      "er": ["o", "emos", "es", "eis", "e", "em"],
                      "ir": ["o", "imos", "es", "is", "e", "em"]}
preterit_perfect = {"name": "preterit_perfect",
                    "ar": ["ei", "ámos", "aste", "astes", "ou", "aram"],
                    "er": ["i", "emos", "es", "eis", "e", "em"],
                    "ir": ["i", "imos", "iste", "istes", "iu", "iram"]}

# dictionary of irregular forms of various verbs
present_indicative_irregulars = {"estar": {"eu": "estou", "tu": "estás", "ele": "está", "eles": "estão"},
                                 "dar": {"eu": "dou", "tu": "dás", "ele": "dá", "eles": "dão"},
                                 "querer": {"ele": "quer"},
                                 "subir": {"tu": "sobes", "ele": "sobe", "eles": "sobem"},
                                 "ser": {"eu": "sou", "tu": "és", "ele": "é", "nós": "somos", "vós": "sois", "eles": "são"} }
preterit_perfect_irregulars = {"estar": {"eu": "estive", "tu": "estiveste", "ele": "esteve", "nós": "estivemos", "vós": "estivestes", "eles": "estiveram"},
                               "dar": {"tu": "deste", "ele": "deu", "nós": "demos", "vós": "destes", "eles": "deram"},
                               "querer": {"eu": "quis", "tu": "quiseste", "ele": "quis", "nós": "quisemos", "vós": "quisestes", "eles": "quiseram"},
                               "ser": {"eu": "fui", "tu": "foste", "ele": "foi", "nós": "fomos", "vós": "fostes", "eles":"foram"}}

# combine all irregulars into a common dictionary  for simplicity
irregulars = {"present_indicative": present_indicative_irregulars,
              "preterit_perfect": preterit_perfect_irregulars}

# define a function to remove the -ar/-er/-ir from end of verb and replace it with its appropriate endings
def conjugate(verb, endings):
    stem = ''.join([*verb][0:len(verb)-2])
    kind = ''.join([*verb][len(verb)-2:len(verb)])
    endings = endings[kind]
    output = []
    for i in range(0, len(endings)):
        output.append(stem + endings[i])
    return(output)

# take conjugated verb and place it in a pandas dataframe, along with an index for each verb form
def to_dataframe(conjugated):

    conjugated = np.array(conjugated)
    conjugated = pd.DataFrame(conjugated, index = ["eu", "nós", "tu", "vós", "ele", "eles"])
    return(conjugated)

# function to replace an irregular verbs irregular forms where appropriate
def irregular(verb, x, y, my_dict):
    if (verb in my_dict):
        x.loc[y.index] = y
    return(x)

# accept user's input of a verb, as well as the set of endings to be conjugated
def take_input(verb, endings):
    dict_of_irregs = irregulars[endings["name"]]
    conjugated = conjugate(verb, endings)
    conjugated = to_dataframe(conjugated)
    conjugated = conjugated.rename(index=str, columns={0: verb})
    # check for excepts of regular conjugations and swap with irregular forms
    if (verb in dict_of_irregs):
        find_verb = pd.DataFrame(pd.DataFrame(dict_of_irregs)[verb])
        find_verb = find_verb.dropna()
        conjugated = irregular(verb, conjugated, find_verb, dict_of_irregs)
    return(conjugated)

# examples of usage
print(take_input("ser", preterit_perfect))
print(take_input("estar", present_indicative))
