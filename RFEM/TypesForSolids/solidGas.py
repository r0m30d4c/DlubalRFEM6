from RFEM.initModel import *
from RFEM.enums import SetType

class SolidGas():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Solid Gas
        clientObject = clientModel.factory.create('ns0:solid_gas')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Gas No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Gas to client model
        clientModel.service.set_solid_gas(clientObject)