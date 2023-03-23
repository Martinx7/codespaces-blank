from deliver import Deliver

class Address(Deliver):
  """
  Class used to represent a Address
  """
  def __init__(self, date: str = "00/00/2023", time: str = "00:00", sender: str = "Person", recive: str = "Person", sender_add: str = "Address", recive_add: str = "Address", contac: str = "+999999999999", items: str = "Package", neighborhood: str = "Neighborhood", street: str = "Street", city: str = "City", avenue: str = "Avenue", postal_code: int = 000000):
    """ 
    Address constructor Deliver.
    
    :Param neighborhood: neighborhood of Address.
    :Type neighborhood: str
    :Param street: street of package.
    :Type street: str
    :Param description: description of package.
    :Type description: str
    :Param cost: cost of package.
    :Type cost: float
    :Peturns: Package object.
    :rtype: object
    """
    
    super().__init__(date, time, sender, recive, sender_add, recive_add, contac, items)
    self._neighborhood = neighborhood
    self._street = street
    self._city = city
    self._avenue = avenue
    self._postal_code = postal_code
  
  @property
  def neighborhood(self) -> str:
    return self._neighborhood
  
  @neighborhood.setter
  def neighborhood(self, neighborhood: str):
    """ 
    The neighborhood of the Address.
    :param neighborhood: neighborhood of Address.
    :type: str
    """
    self._neighborhood = neighborhood

  @property
  def street(self) -> str:
    return self._street
  
  @street.setter
  def street(self, street: str):
    """
    The street of the Address.
    :param street: street of Address.
    :type: str
    """
    self._street = street

  @property
  def city(self) -> str:
    return self._city
  
  @city.setter
  def city(self, city: str):
    """
    The city of the Address.
    :param city: city of Address.
    :type: str
    """
    self._city = city

  @property
  def avenue(self) -> str:
    return self._avenue
  
  @avenue.setter
  def avenue(self, avenue: str):
    """ 
    The avenue of the Address.
    :param avenue: avenue of Address.
    :type: str
    """
    self._avenue = avenue

  @property
  def postal_code(self) -> str:
    return self._postal_code
  
  @postal_code.setter
  def postal_code(self, postal_code: int):
    """ 
    The postal_code of the Address.
    :param postal_code: postal_code of Address.
    :type: str
    """
    self._postal_code = postal_code
    
  
  def __str__(self):
    """ 
    Returns str of address.
    :returns: sting address
    :rtype: str
    """
    return '({0}, {1}, {2}, {3}, {4}'.format(self._neighborhood, self._street, self._city,self._avenue, self._postal_code)







