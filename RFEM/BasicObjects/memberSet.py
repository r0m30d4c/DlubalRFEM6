from RFEM.initModel import *
from RFEM.enums import SetType

class MemberSet():
    def __init__(self,
                 no: int = 1,
                 members_no: str = '1 4 5 8 9 12 13 16 17 20 21 24',
                 member_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Member Set
        clientObject = clientModel.factory.create('ns0:member_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Set No.
        clientObject.no = no

        # Members number
        clientObject.members = ConvertToDlString(members_no)

        # Member Set Type
        clientObject.set_type = member_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Set to client model
        clientModel.service.set_member_set(clientObject)

    def ContinuousMembers(self,
                          no: int = 1,
                          members_no: str = '1 4 5 8 9 12 13 16 17 20 21 24',
                          member_set_type = SetType.SET_TYPE_CONTINUOUS,
                          comment: str = '',
                          params: dict = {}):

        # Client model | Member Set
        clientObject = clientModel.factory.create('ns0:member_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Set No.
        clientObject.no = no

        # Members number
        clientObject.members = ConvertToDlString(members_no)

        # Member Set Type
        clientObject.set_type = member_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Set to client model
        clientModel.service.set_member_set(clientObject)

    def GroupOfmembers(self,
                       no: int = 1,
                       members_no: str = '1 4 5 8 9 12 13 16 17 20 21 24',
                       member_set_type = SetType.SET_TYPE_GROUP,
                       comment: str = '',
                       params: dict = {}):

        # Client model | Member Set
        clientObject = clientModel.factory.create('ns0:member_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Set No.
        clientObject.no = no

        # Members number
        clientObject.members = ConvertToDlString(members_no)

        # Member Set Type
        clientObject.set_type = member_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Member Set to client model
        clientModel.service.set_member_set(clientObject)
