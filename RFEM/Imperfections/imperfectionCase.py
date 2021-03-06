from RFEM.initModel import *
from RFEM.enums import SetType

class ImperfectionCase():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Imperfection Case
        clientObject = clientModel.factory.create('ns0:imperfection_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Imperfection Case No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imperfection Case to client model
        clientModel.service.set_imperfection_case(clientObject)