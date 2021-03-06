from RFEM.initModel import *
from RFEM.enums import SetType

class Instersection():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Intersection
        clientObject = clientModel.factory.create('ns0:intersection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Intersection No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Intersection to client model
        clientModel.service.set_intersection(clientObject)