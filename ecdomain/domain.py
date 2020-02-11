

""" EC-domain
    Read the README-md
    """


class Domains:
    """
    Pluralis - contains a number of 'Domain'
    """

    # Class Attribute
    maintainer = 'EC-software'

    # Initializer / Instance Attributes
    def __init__(self):
        self._data = dict()

    def make_dom(self, name):
        """ Creates a new (empty) domain by name 'name'.
        :return: Return None if domain all ready exists, otherwise returns the Domain.
        """
        if name not in self._data.keys():
            self._data[name] = Domain(name)
            return self._data[name]
        else:
            return None

    def get_dom(self, name):
        """ Returns the domain with name 'name'
        :return: Return None if domain doesn't exist.
        """
        if name in self._data.keys():
            return self._data[name]
        else:
            return None

    def del_dom(self, name):
        """ Delete the domain named 'name'.
        :return: Return True on success and False otherwise.
        """
        if name in self._data.keys():
            del self._data[name]
            return True
        else:
            return False


class Domain:
    """
    Singularis - contains a single 'Domain'
    """

    # Class Attribute
    maintainer = 'EC-software'

    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name
        self._data = dict()
        self._alia = dict()

    def set_kv(self, k, v):
        """ Insert the kv (key-value pair) in the domain
        :param k: key
        :param v: value
        :return: N/A
        """
        self._data[k] = v

    def set_alias(self, k, a):
        """ Insert an alias for key. Create k=k if k dosn't exist
        :param k: key
        :param a: alias
        :return: N/A
        """
        if k not in self._data.keys():
            self._alia[k] = k  # We don't want alias for non-existing key
        if k not in self._alia.keys():  # Create alias list, if not exist
            self._alia[k] = list()
        if a not in self._alia[k]:  # See if alias all-ready exist
            self._alia[k].append(a)

    @staticmethod
    def raw_read_and_clean_file(file_name):
        with open(file_name, 'r') as fil_in:
            lst_in = fil_in.readlines()
        lst_in = [tok.split('#')[0].strip() for tok in lst_in]  # Remove anything after any #
        lst_in = [tok for tok in lst_in if tok != '']  # Remove empty lines
        return lst_in

    def read_file(self, file_name, header=True):
        """ Read the file and try use the values as k,v to fill the domain.
        :param file_name: file-name to to the input
        :param header: If header is True the first line is disregarded - this is default.
        :return: Return number of objects created.
        """
        # Read data
        lst_in = self.raw_read_and_clean_file(file_name)
        # lst_ec = [tok for tok in lst_in if tok[:10].lower() == 'ec-domain:']  # get all lines starting with 'ec-domain:'
        # lst_ec = [tok.split(':', 1)[1].strip() for tok in lst_ec]  # Remove the 'ec-domain:' precursor
        # if len(lst_ec) > 0:
        #     for tok_ec in lst_ec:
        #         if tok_ec[4].lower() == 'ver.':
        #             print(f"version: {tok_ec[:4].strip()}")
        #         if tok_ec[3].lower() == 'rex':
        #             print("It's a 'Reverse EXtender'")
        lst_in = [tok for tok in lst_in if tok[:10].lower() != 'ec-domain:']  # Remove all lines starting with 'ec-domain:'
        # Insert data
        num_inserted = 0  # Initialise return object
        if file_name.endswith('.scsv'):
            sep = ';'  # Semi Colon Separated Values
        elif file_name.endswith('.csv'):
            sep = ','  # Comma Separated Values
        else:
            sep = ','  # default column separator
        if header:
            lst_in = lst_in[1:]  # skip the first token
        lst_kv = [(tok[0].strip(), tok[1].strip()) for tok in [itm.split(sep) for itm in lst_in] if len(tok) > 1]  # make list of tuples of k,v
        for k, v in lst_kv:
            self.set_kv(k, v)
            num_inserted += 1
        return num_inserted

    def get_val(self, k):
        """ Get the value that match the key
        :return: Returns a value, if not exit return None
        """

    def get_key(self, v):
        """ Get the key that match the value
        :return: Returns a key, if not exit return None
        """

    def dominise(self, kc):
        """ Given a kc (key-candidate) return the real key if possible, otherwise return None.
        kc is searched for in keys, aliases and values - in that order.
        :return: Return key if possible, otherwise None.
        """

    def find(self, kc, all_hist=True):
        """ Given a kc (key-candidate) return a list of keys if possible, otherwise returns empty list.
        First run dominise(kc), but if that returns None, find will search for keys, aliases and values
        the are not identical to, but contains kc. The search order is like dominise.
        There may be multiple hits. If parameter all_hits is True, all results is returned as a list - this is default.
        Otherwise only first result is returned, in a list.
        If no results, an empty list is returned.
        :param kc: key-candidate
        :param all_hist: Boolean: if true, return all hits, if False only returns first hit. Default is True
        :return: Return-object is always a list.
        """

    def __str__(self):
        """ Return string with k: v for each key in Domain, sorted in key order. """
        return '\n'.join([f"{k}: {self._data[k]}" for k in sorted(self._data.keys())])
        # Consider writing Aliases also XXX


test = Domain('test')
test.read_file('dom_boolean.scsv')
print(f"DOM_1:\n{test}")
test.read_file('dom_boolean_rex.scsv')
print(f"DOM_2:\n{test}")
