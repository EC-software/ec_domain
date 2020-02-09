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
When shown to the user, the Country name me be used as a lable, 
thereby camouflaging the two-letter values that is actually stored.  
 
## ec-dom
ec-dom is an ECsoftware class for working with domains.

###### Domains 
Domains hold a number of domains

**make_dom**(name)  Creates a new (empty) domain by name 'name'. 
Return None if domain all ready exists.

**get_dom**(name)  Returns the domain with name 'name'
Return None if domain dosn't exist.

**del_dom**(name)  Delete the domain named 'name'.
Return True on succes and False otherwise.

###### Domain
A single domain, holds one domain
 
**set_kv**(k,v)  Insert the kv (key-value pair) in the domain

**set_alias**(k,a)  Insert an alias for key. Create k=k if k 
dosn't exist 

**read_file**(file_name, header=True)  Read the file and try use the values
as k,v to fill the domain. If header is True the first line is 
disregarded - this is default. Return number of k,v created.

**get_val**(k)  Given a key returns a value, if not exit return None

**get_key**(v)  Given a value returns a key, if not exit return None 

**dominise**(kc)  Given a kc (key-candidate) return the real key if 
posible, otherwise return None. 
kc is searched for in keys, aliases and values - in that order. 

**find**(kc, all=True)  First run dominise(kc), but if that returns 
None, find will search for keys, aliases and values the are not 
identical to, but contains kc. The search order is like dominise.
There may be multiple hits. If parameter all is True, all results
is returned as a list - this is default. 
Otherwise only first result is returned in a list.
If no results, an empty list is returned. 
Return-object is always a list.