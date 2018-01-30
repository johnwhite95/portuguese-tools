

```python
import pandas as pd
import numpy as np
```


```python
#figure out how to load a file as a dictionary
present_indicative = {"name": "present_indicative",
                      "ar": ["o", "amos", "as", "ais", "a", "am"],
                      "er": ["o", "emos", "es", "eis", "e", "em"],
                      "ir": ["o", "imos", "es", "is", "e", "em"]}
preterit_perfect = {"name": "preterit_perfect",
                    "ar": ["ei", "ámos", "aste", "astes", "ou", "aram"],
                    "er": ["i", "emos", "es", "eis", "e", "em"],
                    "ir": ["i", "imos", "iste", "istes", "iu", "iram"]}
present_indicative_irregulars = {"estar": {"eu": "estou", "tu": "estás", "ele": "está", "eles": "estão"},
                                 "dar": {"eu": "dou", "tu": "dás", "ele": "dá", "eles": "dão"},
                                 "querer": {"ele": "quer"},
                                 "subir": {"tu": "sobes", "ele": "sobe", "eles": "sobem"},
                                 "ser": {"eu": "sou", "tu": "és", "ele": "é", "nós": "somos", "vós": "sois", "eles": "são"} }
preterit_perfect_irregulars = {"estar": {"eu": "estive", "tu": "estiveste", "ele": "esteve", "nós": "estivemos", "vós": "estivestes", "eles": "estiveram"},
                               "dar": {"tu": "deste", "ele": "deu", "nós": "demos", "vós": "destes", "eles": "deram"},
                               "querer": {"eu": "quis", "tu": "quiseste", "ele": "quis", "nós": "quisemos", "vós": "quisestes", "eles": "quiseram"},
                               "ser": {"eu": "fui", "tu": "foste", "ele": "foi", "nós": "fomos", "vós": "fostes", "eles":"foram"}}

irregulars = {"present_indicative": present_indicative_irregulars,
              "preterit_perfect": preterit_perfect_irregulars}
```


```python
irregulars
```




    {'present_indicative': {'dar': {'ele': 'dá',
       'eles': 'dão',
       'eu': 'dou',
       'tu': 'dás'},
      'estar': {'ele': 'está', 'eles': 'estão', 'eu': 'estou', 'tu': 'estás'},
      'querer': {'ele': 'quer'},
      'ser': {'ele': 'é',
       'eles': 'são',
       'eu': 'sou',
       'nós': 'somos',
       'tu': 'és',
       'vós': 'sois'},
      'subir': {'ele': 'sobe', 'eles': 'sobem', 'tu': 'sobes'}},
     'preterit_perfect': {'dar': {'ele': 'deu',
       'eles': 'deram',
       'nós': 'demos',
       'tu': 'deste',
       'vós': 'destes'},
      'estar': {'ele': 'esteve',
       'eles': 'estiveram',
       'eu': 'estive',
       'nós': 'estivemos',
       'tu': 'estiveste',
       'vós': 'estivestes'},
      'querer': {'ele': 'quis',
       'eles': 'quiseram',
       'eu': 'quis',
       'nós': 'quisemos',
       'tu': 'quiseste',
       'vós': 'quisestes'},
      'ser': {'ele': 'foi',
       'eles': 'foram',
       'eu': 'fui',
       'nós': 'fomos',
       'tu': 'foste',
       'vós': 'fostes'}}}




```python
def conjugate(verb, endings):
    stem = ''.join([*verb][0:len(verb)-2])
    kind = ''.join([*verb][len(verb)-2:len(verb)])
    endings = endings[kind]
    output = []
    for i in range(0, len(endings)):
        output.append(stem + endings[i])
    return(output)
```


```python
def to_dataframe(conjugated):

    conjugated = np.array(conjugated)
    conjugated = pd.DataFrame(conjugated, index = ["eu", "nós", "tu", "vós", "ele", "eles"])

    return(conjugated)
```


```python
def irregular(verb, x, y, my_dict):
    if (verb in my_dict):
        x.loc[y.index] = y
    return(x)
```


```python
#keys = list(irregulars.keys())
```


```python
def take_input(verb, endings):

    dict_of_irregs = irregulars[endings["name"]]
    bob = conjugate(verb, endings)
    bob = to_dataframe(bob)
    bob = bob.rename(index=str, columns={0: verb})
    if (verb in dict_of_irregs):
        find_verb = pd.DataFrame(pd.DataFrame(dict_of_irregs)[verb])
        find_verb = find_verb.dropna()
        bob = irregular(verb, bob, find_verb, dict_of_irregs)
    return(bob)

```


```python
take_input("ser", preterit_perfect)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ser</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>eu</th>
      <td>fui</td>
    </tr>
    <tr>
      <th>nós</th>
      <td>fomos</td>
    </tr>
    <tr>
      <th>tu</th>
      <td>foste</td>
    </tr>
    <tr>
      <th>vós</th>
      <td>fostes</td>
    </tr>
    <tr>
      <th>ele</th>
      <td>foi</td>
    </tr>
    <tr>
      <th>eles</th>
      <td>foram</td>
    </tr>
  </tbody>
</table>
</div>




```python
take_input("estar", present_indicative)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>estar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>eu</th>
      <td>estou</td>
    </tr>
    <tr>
      <th>nós</th>
      <td>estamos</td>
    </tr>
    <tr>
      <th>tu</th>
      <td>estás</td>
    </tr>
    <tr>
      <th>vós</th>
      <td>estais</td>
    </tr>
    <tr>
      <th>ele</th>
      <td>está</td>
    </tr>
    <tr>
      <th>eles</th>
      <td>estão</td>
    </tr>
  </tbody>
</table>
</div>
