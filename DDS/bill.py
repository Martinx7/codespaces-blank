from person import Person
from address import Address
from package import Package



class Bill(object):
  """
  Class used to represent a bill
  """
  def __init__(self, package_information: object = Package, package_address: object = Address, package_person: object = Person, total_paid: float = 1.5, card_type: str = "Debit/Credit", type_of_financing: str = "Dues"):
    """ 
    bill constructor object.

    :param package_information: package_information of bill.
    :type package_information: object
    :param package_address: package_address of bill.
    :type package_address: object
    :param package_person: package_person of bill.
    :type package_person: object
    :param total_paid: total_paid of bill.
    :type total_paid: float
    :param card_type: card_type of bill.
    :type card_type: str
    :param type_of_financing: type_of_financing of bill.
    :type type_of_financing: str
    :returns: Bill object.
    :rtype: object
    
    """
    def __init__(package_information, package_address, package_person):
      self._total_paid = total_paid
      self._card_type = card_type
      self._type_of_financing = type_of_financing
  
  @property
  def total_paid(self) -> float:
    return self._total_paid
  
  @total_paid.setter
  def total_paid(self, total_paid: float):
    """ 
    The total_paid of the bill.
    :param total_paid: total_paid of bill.
    :type: float
    """
    self._total_paid = total_paid

  @property
  def card_type(self) -> str:
    return self._card_type
  
  @card_type.setter
  def card_type(self, card_type: str):
    """ 
    The card_type of the bill.
    :param card_type: card_type of bill.
    :type: str
    """
    self._card_type = card_type

  @property
  def type_of_financing(self) -> str:
    return self._type_of_financing
  
  @type_of_financing.setter
  def type_of_financing(self, type_of_financing: str):
    """ 
    The type_of_financing of the bill.
    :param type_of_financing: type_of_financing of bill.
    :type: str
    """
    self._type_of_financing = type_of_financing

  @property
  def package_information(self) -> object:
    return self._package_information

  @package_information.setter
  def package_information(self, package_information: object):
    """ 
    The package_information of the bill.
    :param package_information: package_information of bill.
    :type: object
    """
    self._package_information = package_information

  @property
  def package_address(self) -> object:
    return self._package_address

  @package_address.setter
  def package_address(self, package_address: object):
    """ 
    The package_address of the bill.
    :param package_address: package_address of bill.
    :type: object
    """
    self._package_address = package_address

  @property
  def package_person(self) -> object:
    return self._package_person

  @package_person.setter
  def package_person(self, package_person: object):
    """ 
    The package_person of the bill.
    :param package_person: package_person of bill.
    :type: object
    """
    self._package_person = package_person



  def __str__(self):
    """ 
    Returns str of bill.
    :returns: sting bill
    :rtype: str
    """
    return '({0}, {1}, {2}, {3}, {4}, {5}'.format(self._package_information, self._package_address, self._package_person, self._total_paid, self._card_type, self._type_of_financing)