from RFEM.initModel import *
from RFEM.enums import SetType

class LineMeshRefinements():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Line Mesh Refinement
        clientObject = clientModel.factory.create('ns0:line_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Mesh Refinement to client model
        clientModel.service.set_line_mesh_refinement(clientObject)