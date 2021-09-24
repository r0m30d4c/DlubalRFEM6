#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import math
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.lineLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.material import *
from RFEM.initModel import *
from RFEM.dataTypes import *
from RFEM.enums import *

# Import der Bibliotheken
#from RFEM.window import *

if __name__ == '__main__':

    # die Parametrisierung der Pilzdecke 

    no_cols_X = int(input('Number of columns in the X direction: '))
    col_spacing_X = float(input('Spacing of columns in the X direction in m: '))
    no_cols_Y = int(input('Number of columns in the Y direction: '))
    col_spacing_Y = float(input('Spacing of columns in the Y direction in m: '))
    story_height = float(input('Height of building story in m: '))
    X_Pattern, Y_Pattern, Perimeter_Cols = [], [], ' '

    # Sperren der Benutzeroberfläche von RFEM

    clientModel.service.begin_modification('new')

    # Knotenerzeugung

    for i in range(0,no_cols_X): X_Pattern.append(i*col_spacing_X)
    for j in range(0,no_cols_Y): Y_Pattern.append(j*col_spacing_Y)

    node_num = 0
    for x in X_Pattern:
        for y in Y_Pattern:
            node_num += 1
            Node(node_num, x, -y, 0, 'EG')
            NodalSupport(node_num, str(node_num) , NodalSupportType.FIXED)
            node_num += 1
            Node(node_num, x, -y, -story_height, '1OG')
    
    # Stäbe

    Material(1, 'C25/30')
    Section(1, 'SQ_M1 250')

    member_num = 0
    for k in range(1,node_num+1,2):
        member_num += 1
        Member(member_num, MemberType.TYPE_BEAM, k, k+1, 0.0, 1, 1)

    for l in range(1,no_cols_Y+1): Perimeter_Cols += str(l) + ' ' # Erste Reihe von Stäbe
    if no_cols_X > 2 or no_cols_Y > 2:
        for m in range(1, no_cols_X-1): Perimeter_Cols += str(1+m*no_cols_Y) + ' ' + str(no_cols_Y+m*no_cols_Y) + ' '
    else:
        pass
    for n in range((no_cols_X-1)*no_cols_Y+1, member_num+1): Perimeter_Cols += str(n) + ' ' # Letzte Reihe von Stäbe

    Perimeter_Cols = Perimeter_Cols.lstrip().rstrip()

    # Linien

    nodes_str_line_1 = str(2) + ' ' + str(no_cols_Y*2)
    nodes_str_line_2 = str(no_cols_Y*2) + ' ' + str(no_cols_X*no_cols_Y*2)
    nodes_str_line_3 = str(no_cols_X*no_cols_Y*2) + ' ' + str(no_cols_Y*2*(no_cols_X-1)+2)
    nodes_str_line_4 = str(no_cols_Y*2*(no_cols_X-1)+2) + ' ' + str(2)

    Line(member_num+1, nodes_str_line_1, '')
    Line(member_num+2, nodes_str_line_2, '')
    Line(member_num+3, nodes_str_line_3, '')
    Line(member_num+4, nodes_str_line_4, '')

    # Fläche
    slab_boundary = str(member_num+1) + ' ' + str(member_num+2) + ' ' + str(member_num+3) + ' ' + str(member_num+4)
    Thickness(1, 'Konstant', 1, 0.18, '')
    Surface (1, slab_boundary, 1)

    # Lasten

    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    LoadCase(1, 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)

    SurfaceLoad(1, 1, '1', 1000.0, '')

    LineLoad(1, 1, str(member_num+1) + ' ' + str(member_num+2) + ' ' + str(member_num+3) + ' ' + str(member_num+4),
             LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 2500, '')

    MemberLoad(1, 1, Perimeter_Cols,
                LoadDirectionType.LOAD_DIRECTION_LOCAL_X, -500, '')

    # Alles berechnen

    Calculate_all()
    print('Ready!')

    # Freigeben der Benutzeroberfläche von RFEM
    clientModel.service.finish_modification()