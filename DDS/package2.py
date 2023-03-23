from package import Package

class StandardPackage(Package):
  """
  Class used to represent a Package
  """

  def __init__(self, id_package: int = 0, weight: float = 0.5 , description: str = "DescriptionOfProduct" , cost: float = 1.5, fixed_fee: float = 1.0):
    """ 
    standard package constructor object.

    :param fixed_fee: fixed_fee of standard package.
    :type fixed_fee: float
    :returns: StandardPackage Package.
    :rtype: Package
    """
    super().__init__(id_package, weight, description, cost)
  
    self._fixed_fee = fixed_fee
  
  @property
  def fixed_fee(self) -> float:
    return self._fixed_fee
  
  @fixed_fee.setter
  def fixed_fee(self, fixed_fee: float):
    """ 
    The fixed_fee of the standard package.
    :param fixed_fee: fixed_fee of standard package.
    :type: float
    """
    self._fixed_fee = fixed_fee

  def calculate(self):
    print("The cost of sending the package is $"f"{((self._fixed_fee + self._weight ) * self._cost)}")
  
  def __str__(self):
    """ 
    Returns str of package.
    :returns: sting package
    :rtype: str
    """
    return '({0})'.format(self.fixed_fee)

class OverWeigthPackage(Package):
  """
  Class used to represent a Package
  """

  def __init__(self, id_package: int = 0, weight: float = 0.5 , description: str = "DescriptionOfProduct" , cost: float = 1.5, over_weigth: float = 0.5):
    """ 
    standard package constructor object.

    :param over_weigth: over_weigth of standard package.
    :type over_weigth: float
    :returns: OverWeigthPackage Package.
    :rtype: Package
    """
    
    def calculate(self):
      
      print("The cost of sending the package is $"f"{((self._over_weigth + self._weight ) * self._cost)}")

    super().__init__(id_package, weight, description, cost)
    self.over_weigth = over_weigth

    @property
    def over_weigth(self) -> float:
      return self._over_weigth
    
    @over_weigth.setter
    def over_weigth(self, over_weigth: float):
        """ 
        The over_weigth of the standard package.
        :param over_weigth: over_weigth of over weigth package.
        :type: float
        """
        self._over_weigth = over_weigth
  