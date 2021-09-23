Node
========
.. function:: Node(no, coordinate_X, coordinate_Y, coordinate_Z, comment*, params*)

* Parameters

		* ``no`` *int*: 
		* ``coordinate_X`` *float*: 
		* ``coordinate_Y`` *float*:
		* ``coordinate_Z`` *float*:
		* ``comment`` *str, optional*: Comments
		* ``params`` *dict, optional*: Parameters
		
:label:`Node.Standard` :label:`Node.BetweenTwoNodes` :label:`Node.BetweenTwoPoints` :label:`Node.OnMember` :label:`Node.OnLine`

------------


:func:`Node.Standard`

.. function:: Node.Standard(no, coordinate_system, coordinate_system_type, comment*, params*)

* Parameters

		* ``no`` :mod:`int`: 
		* ``coordinate_system`` (**): 
		* ``coordinate_system_type`` (**): 
		* ``comment`` ( *str, optional*): Comments
		* ``params`` (*dict, optional*): Parameters
------------


:func:`Node.BetweenTwoNodes`

.. function:: Node.BetweenTwoNodes(no, start_node_no, end_node_no, node_reference, length_between_i_and_j, parameters, offset_x, offset_y, offset_z, comment*, params*)

* Parameters

		* ``no`` (*int*): 
		* ``start_node_no`` (*int*): 
		* ``end_node_no`` (*int*): 
		* ``node_reference`` (**):
		* ``length_between_i_and_j`` (*int*):  
		* ``parameters`` (**):
		* ``offset_x`` (*int*):
		* ``offset_y`` (*int*):
		* ``offset_z`` (*int*):
		* ``comment`` ( *str, optional*): Comments
		* ``params`` (*dict, optional*): Parameters
------------


:func:`Node.BetweenTwoPoints`

.. function:: Node.BetweenTwoPoints(no, start_point_x, start_point_y, start_point_z, end_point_x, end_point_y, end_point_z, node_reference, parameters, offset_y, offset_z, comment*, params*)

* Parameters

		* ``no** (*int*): 
		* ``start_point_x`` (*float*): 
		* ``start_point_y`` (*float*):
		* ``start_point_z`` (*float*): 
		* ``end_point_x`` (*float*):
		* ``end_point_y`` (*float*):
		* ``end_point_z`` (*float*):
		* ``node_reference`` (**):
		* ``parameters`` (**):
		* ``offset_y`` (*float*):
		* ``offset_z`` (*float*):
		* ``comment`` ( *str, optional*): Comments
		* ``params`` (*dict, optional*): Parameters
------------


:func:`Node.OnMember`

.. function:: Node.OnMember(no, member_number, node_reference, length_between_i_and_j, parameters, comment*, params*)

* Parameters

		* ``no`` (*int*): 
		* ``member_number`` (*str*): 
		* ``node_reference`` (**):
		* ``length_between_i_and_j`` (*int*):
		* ``parameters`` (**):
		* ``comment`` ( *str, optional*): Comments
		* ``params`` (*dict, optional*): Parameters
------------


:func:`Node.OnLine`

.. function:: Node.OnLine(no, line_number, node_reference, length_between_i_and_j, parameters, comment*, params*)

* Parameters

		* ``no`` (*int*): 
		* ``line_number`` (*str*): 
		* ``node_reference`` (**):
		* ``length_between_i_and_j`` (*int*):
		* ``parameters`` (**):
		* ``comment`` ( *str, optional*): Comments
		* ``params`` (*dict, optional*): Parameters
		
``.. _Carine:``

``:ref:`Carine``` 


