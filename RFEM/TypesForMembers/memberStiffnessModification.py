from RFEM.initModel import *
from RFEM.enums import SetType

class MemberStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Stiffness Modification
        clientObject = clientModel.factory.create('ns0:smember_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Stiffness Modification No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Stiffness Modification to client model
        clientModel.service.set_member_stiffness_modification(clientObject)