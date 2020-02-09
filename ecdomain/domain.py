

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

    def get_dom(self, name):
        """ Returns the domain with name 'name'
        :return: Return None if domain dosn't exist.
        """

    def del_dom(self, name):
        """ Delete the domain named 'name'.
        :return: Return True on success and False otherwise.
        """


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

    def set_kv(self, k,v):
        """ Insert the kv (key-value pair) in the domain
        :param k:
        :param v:
        :return:
        """

    def set_alias(k,a):
        """ Insert an alias for key. Create k=k if k dosn't exist
        :param a:
        :return:
        """

    def read_file(self, file_name, header=True):
        """ Read the file and try use the values as k,v to fill the domain.
        :param file_name: file-name to to the input
        :param header: If header is True the first line is disregarded - this is default.
        :return: Return number of k,v created.
        """

    def get_val(k):
        """ Get the value that match the key
        :return: Returns a value, if not exit return None
        """

    def get_key(v):
        """ Get the key that match the value
        :return: Returns a key, if not exit return None
        """

    def dominise(kc):
        """ Given a kc (key-candidate) return the real key if possible, otherwise return None.
        kc is searched for in keys, aliases and values - in that order.
        :return: Return key if possible, otherwise None.
        """

    def find(kc, all=True):
        """ Given a kc (key-candidate) return a list of keys if possible, otherwise returns empty list.
        First run dominise(kc), but if that returns None, find will search for keys, aliases and values
        the are not identical to, but contains kc. The search order is like dominise.
        There may be multiple hits. If parameter all is True, all results is returned as a list - this is default.
        Otherwise only first result is returned, in a list.
        If no results, an empty list is returned.
        :param all: Boolean: if true, return all hits, if False only returns first hit. Default is True
        :return: Return-object is always a list.
        """
