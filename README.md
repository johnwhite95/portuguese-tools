
# Portuguese Tools


A verb is conjugated by removing its last two letters and replacing them with the appropriate ending form.
```python
def conjugate(verb, endings): 
    return(list(map(lambda x: ''.join([*verb][0:len(verb) - 2]) + x,
           endings[''.join([*verb][len(verb) - 2:len(verb)])])))
```

A conjugated verb is passed to a function that converts it into a pandas dataframe along with an index indicating the person for each verb
```python
nominative_pronouns = ["eu", "nós", "tu", "vós", "ele", "eles"]
def to_dataframe(conjugated): return(pd.DataFrame(np.array(conjugated), index = nominative_pronouns))
```

Next, a function is defined to take an irregular verb, search the dictionary for that verb, and replace the regular forms. This function is designed so that only forms that need to be replaced are replaced. This prevents the redundancy of needing to also input regular conjugations for each irregular verb.

```python
def irregular(verb, x, y, my_dict):
    if (verb in my_dict):
        x.loc[y.index] = y
    return(x)
```

The following function combines the previous ones together, accepting a verb along with the set of conjugations

```python
def user_in(verb, endings):

    # bring in a dictionary of irregular verbs for the chosen tense
    dict_of_irregs = irregulars[endings["name"]]

    #create dataframe of conjugated verb
    framed = to_dataframe(conjugate(verb, endings)).rename(index=str, columns = {0:verb})

    # if the verb is found to be in the dictionary of irregulars, call the irregular() function to
    # replace the irregular forms and redefine the dataframe of conjugations
    if (verb in dict_of_irregs):
        find_verb = pd.DataFrame(pd.DataFrame(dict_of_irregs)[verb]).dropna()
        framed = irregular(verb, to_dataframe(conjugate(verb, endings)).rename(index = str, columns = {0:verb}),
                           find_verb, dict_of_irregs)

    # print the name of the chosen tense
    print(endings["name"])
    # return the conjugations
    return(framed)

```

A couple of examples of irregular verbs that have some regular and some irregular endings.

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

