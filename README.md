# Domain
## The concept...

Domain is, fundamentally, a key-val list, e.g like this:

    Country_Code; Country name
    AD; Andorra
    AE; United Arab Emirates
    AF; Afghanistan
    AG; Antigua and Barbuda
    AI; Anguilla
    AL; Albania
    ...

Country_Code is the key, and must be unique in the list.
Country name is the value, also called the description.
 
Often used in data base structures or other data structures, where a 
given field should only hold values from a limited set of values. 
In the example above a country field should only hold values from the 
Country_code list. 
When shown to the user, the Country name may be used as a lable, 
thereby camouflaging the two-letter values that is actually stored.  
 
## ec-dom
ec-dom is an ECsoftware class for working with domains.

###### Domains 
Domains hold a number of 'Domain'

**make_dom**(name)

**get_dom**(name)

**del_dom**(name)

###### Domain
A single domain, holds one domain
 
**set_kv**(k,v)

**set_alias**(k,a)

**read_file**(file_name, header=True)

**keys**()

**get_val**(k)

**get_key**(v)

**get_ali**(k)

**dominise**(kc, all_hits=True)

**find**(kc, all_hits=True)