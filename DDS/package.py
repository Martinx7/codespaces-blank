
from deliver import Deliver

class Package(Deliver):
      
  """
  Class used to represent a Package
  """
  
  W_GR_100 = 1.0
  def __init__(self, id_package: int = 0, weight: float = 0.5 , description: str = "DescriptionOfProduct" , cost: float = 1.5, date: str = "00/00/0000", time: str = "00:00", sender: str = "Person", recive: str = "Person", sender_add: str = "Address", recive_add: str = "Address", contac: str = "+999999999999", items: str = "Package"):
    """ 
    Package constructor object.

    :param id_package: id of package.
    :type id_package: int
    :param weight: weight of package.
    :type weight: float
    :param description: description of package.
    :type description: str
    :param cost: cost of package.
    :type cost: float
    :returns: Package object.
    :rtype: object
    """
    super().__init__(date, time, sender, recive, sender_add, recive_add, contac, items)
    
    self._id_package = id_package
    self._weight = weight
    self._description = description
    self._cost = cost

  @property
  def id_package(self) -> int:
    return self._id_package
  
  @id_package.setter
  def id_package(self, id_package: int):
    """ 
    The id of the package.
    :param id_package: id of package.
    :type: int
    """
    self._id_package = id_package
  
  @property
  def weight(self) -> float:
    return self._weight
  
  @weight.setter
  def weight(self, weight: float):
    """ 
    The wight of the package.
    :param weight: weight of package.
    :type: float
    """
    self._weight = weight
  
  @property
  def description(self) -> str:
    return self._description
  
  @description.setter
  def description(self, description: str):
    """ 
    The description of the package.
    :param description: description of package.
    :type: str
    """
    self._description = description
  
  @property
  def cost(self) -> float:
    return self._cost
  
  @cost.setter
  def cost(self, cost: float):
    """ 
    The cost of the package.
    :param cost: cost of package.
    :type: float
    """
    self._cost = cost
  
  def __str__(self):
    """ 
      Returns str of package.
      :returns: sting package
      :rtype: str
    """
    return '({0}, {1}, {2}, {3})'.format(self._id_package, self._weight, self._description, self._cost)
    