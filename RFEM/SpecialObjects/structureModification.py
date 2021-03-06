from RFEM.initModel import *
from RFEM.enums import SetType

class StructureModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Structure Modification
        clientObject = clientModel.factory.create('ns0:structure_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Structure Modification No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Structure Modification to client model
        clientModel.service.set_structure_modification(clientObject)