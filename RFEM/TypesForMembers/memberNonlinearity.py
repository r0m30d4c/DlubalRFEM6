from RFEM.initModel import *
from RFEM.enums import SetType

class MemberNonlinearity():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Nonlinearity
        clientObject = clientModel.factory.create('ns0:member_nonlinearity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Nonlinearity No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Nonlinearity to client model
        clientModel.service.set_member_nonlinearity(clientObject)