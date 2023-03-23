from package import Package
from address import Address
from bill import Bill
from deliver import Deliver
from person import Person
from package2 import StandardPackage
from package2 import OverWeigthPackage

Box = Package(123456, 5.6, "Mouse", 500000)
Client = Person(1007983300,"Martin","Marbello")
AOC =Address("23/03/2023","07:11","Karla","Martin","Laquito","Turbaco","+573136900268","Mouse","Pumarejo","Calle #12","Turbaco","Quinta Avenida",1113001)
Delivery = Deliver("23/03/2023","07:11","Karla","Martin","Laquito","Turbaco","+573136900268","Mouse")
Oweigth = OverWeigthPackage(123456,0.09,"Mouse",230000,1)
Standard = StandardPackage(123456,0.09,"Mouse",230000,1)

print("******* Summary of data and results *******")
print("")

print("*** Client ***")
print(Client)
print("")

print("*** Delivery address ***")
print(AOC)
print("")

print("*** Package details ***")
print(Box)
print("")

print("*** Delivery details ***")
print(Delivery)
print("")

print("*** Cost ***")
print(Standard.calculate())
print("")