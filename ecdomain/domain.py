

""" EC-domain
    Read the README-md
    """
import logging

logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="ecdomain.log",
    filemode="w",
    level=logging.WARNING)
log = logging.getLogger(__name__)


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
    """ Singular - contains a single 'Domain'
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
        log.info(f"set_vk: {k}, {v}")
        self._data[k] = v

    def set_alias(self, k, a):
        """ Insert an alias for key. Create k=k if k doesn't exist
        :param k: key
        :param a: alias
        :return: N/A
        """
        log.info(f"set_alias: {k}, {a}")
        if k not in self.keys():
            self._data[k] = k  # We don't want alias for non-existing key
        if k not in self._alia.keys():  # Create alias list, if not exist
            self._alia[k] = list()
        if a not in self._alia[k]:  # See if alias all-ready exist
            self._alia[k].append(a)

    @staticmethod
    def _raw_read_and_clean_file(file_name):
        with open(file_name, 'r') as fil_in:
            lst_in = fil_in.readlines()
        lst_in = [tok.split('#')[0].strip() for tok in lst_in]  # Remove anything after any #
        lst_in = [tok for tok in lst_in if tok != '']  # Remove empty lines
        return lst_in

    def read_file(self, file_name, header=True):
        """ Read the file and try use the values as k,v or aliases to fill the domain.
        :param file_name: file-name to to the input
        :param header: If header is True the first line is disregarded - this is default.
        :return: Return number of objects created.
        """
        # Read data
        log.info(f"reading file: {file_name}")
        lst_in = self._raw_read_and_clean_file(file_name)
        lst_ec = [tok for tok in lst_in if tok[:10].lower() == 'ec-domain:']  # get all lines starting with 'ec-domain:'
        lst_ec = [tok.split(':', 1)[1].strip() for tok in lst_ec]  # Remove the 'ec-domain:' precursor
        bol_ecdomain_rex = False  # Assume False until proven True
        if len(lst_ec) > 0:
            for tok_ec in lst_ec:
                if tok_ec[:4].lower() == 'ver.':
                    str_ecdomain_version = tok_ec[4:].strip()
                    log.info(f"ec-domain version: {str_ecdomain_version}")
                if tok_ec[:3].lower() == 'rex':
                    bol_ecdomain_rex = True
                    log.info("ec-domain It's a 'Reverse EXtender'")
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
            lst_in = lst_in[1:]  # skip the first token, if header
        if bol_ecdomain_rex:  # k,v or rex/alias file?
            for rex in lst_in:
                if isinstance(rex, str):
                    lst_rex = [tok.strip() for tok in rex.split(sep)]
                    if len(lst_rex) > 1:
                        str_keya = lst_rex[0]  # First token is the key
                        lst_ali = lst_rex[1:]  # all other tokens are aliases
                        for str_ali in lst_ali:
                            self.set_alias(str_keya, str_ali)
                            num_inserted += 1
        else:
            lst_kv = [(tok[0].strip(), tok[1].strip()) for tok in [itm.split(sep) for itm in lst_in] if len(tok) > 1]  # make list of tuples of k,v
            for k, v in lst_kv:
                self.set_kv(k, v)
                num_inserted += 1
        log.info(f"Added {num_inserted} items")
        log.info(f"status count: keys: {len(self._data)}, rex: {sum([len(self._alia[k]) for k in self._alia.keys()])}")
        return num_inserted

    def keys(self):
        """ Sorted list of keys in Domain
        :return: a list
        """
        return sorted(self._data.keys())

    def get_val(self, k):
        """ Get the value that match the key
        :return: Returns a value, if not exit return None
        """
        if k in self.keys():
            return self._data[k]
        else:
            return None

    def get_key(self, v):
        """ Get the key(s) that match the value
        :return: Returns list of keys, if none exit return None
        """
        lst_reverse_hits = [k for k in self.keys() if self._data[k] == v]
        if len(lst_reverse_hits) > 0:
            return lst_reverse_hits
        else:
            return None

    def get_ali(self, k):
        """ Get the list of aliases for key, if any exists.
        :param k: key
        :return: list of aliases for key k, if exists. Otherwise returns empty list
        """
        if k in self._alia.keys():
            return self._alia[k]
        else:
            return list()

    def dominise(self, kc, all_hits=True):
        """ Given a kc (key-candidate) return the real key if possible, otherwise return None.
        kc is searched for in keys, aliases and values - in that order.
        There may be multiple hits. If parameter all_hits is True, all results is returned as a list - this is default.
        Otherwise only first result is returned, in a list.
        If no results, an empty list is returned.
        :return: Return key if possible, otherwise None.
        """
        lst_ret = list()  # Initialise return object
        lst_ret.extend([k for k in self.keys() if k not in lst_ret and k == kc])  # Look in keys, no duplicates
        lst_ret.extend([k for k in self.keys() if k not in lst_ret and self._data[k] == kc])  # Look through values
        for key_good in self.keys():
            if key_good not in lst_ret:
                if any([itm == kc for itm in self.get_ali(key_good)]):  # Look through aliases
                    lst_ret.append(key_good)
        if all_hits:
            return lst_ret
        else:
            return lst_ret[:1]

    def find(self, kc, all_hits=True):
        """ Given a kc (key-candidate) return a list of keys if possible, otherwise returns empty list.
        First run dominise(kc), AND IN ADDITION 'find' will search for keys, aliases and values
        the are not identical to, but contains kc. The search order is as dominise().
        There may be multiple hits. If parameter all_hits is True, all results is returned as a list - this is default.
        Otherwise only first result is returned, in a list.
        If no results, an empty list is returned.
        :param kc: key-candidate
        :param all_hits: Boolean: if true, return all hits, if False only returns first hit. Default is True
        :return: Return-object is always a list.
        """
        lst_ret = self.dominise(kc, all_hits)  # First run dominise() to get full length matches
        if (not all_hits) and len(lst_ret) > 0:  # If only first hit requested, and hit already found.
            return lst_ret
        else:  # look for additional hits
            lst_ret.extend([k for k in self.keys() if k not in lst_ret and kc in k])  # Look in keys, no duplicates
            lst_ret.extend([k for k in self.keys() if k not in lst_ret and kc in self._data[k]])  # Look through values
            for key_good in self.keys():
                if key_good not in lst_ret:
                    if any([kc in itm for itm in self.get_ali(key_good)]):  # Look through aliases
                        lst_ret.append(key_good)
            if all_hits:
                return lst_ret
            else:
                return lst_ret[:1]

    def __str__(self):
        """ Show the Domain as string
        Return string with k: v for each key in Domain, sorted in key order.
        and list of aliases for each key, if any exist """
        str_ret = str()  # Initialise the return object
        str_ret += '\n'.join([f"{k}: {self._data[k]}" for k in self.keys()])
        if len(self._alia) > 0:
            str_ret += '\n' + '\n'.join([f"rex: {itm}: {self._alia[itm]}" for itm in sorted(self._alia)])
        return str_ret


if __name__ == "__main__":
    pass
