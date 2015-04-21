#Light Skeleton
#@author akkey
#

#
#※メッシュを「Mesh」グループ直下に配置してください。上から順にボタンを押してください。
#

import maya.cmds as cmds
import re

#UI
def joint_UI():
    #メッセージ
    cmds.inViewMessage( amg='<hl>「ジョイント設置」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
    
    windowName= cmds.window(title='LightSkeleton')
    
    form = cmds.formLayout()
    cmds.columnLayout()
    cmds.setParent('..')
    addJointButton = cmds.button(label='ジョイント設置', command='joint_add()')
    copyJointButton = cmds.button(label='左側にジョイントコピー', command='joint_left_add()')
    footIKButton = cmds.button(label='足のIK設置', command='set_knee_IK()')
    fingerButton =  cmds.button(label='指のコントローラー設置', command='set_finger_controller()')
    closeButton = cmds.button(label='バインド', command=('bind_mesh()'))
    animImportButton = cmds.button(label='アニメーションをインポート', command=('import_anim()'))
    bakeButton = cmds.button(label='モーションをベイク', command=('motion_bake()'))
    
    cmds.formLayout(form, edit=True,\
        attachForm=[(addJointButton, 'top', 10),\
            (addJointButton, 'left', 10),\
            (addJointButton, 'bottom', 190),\
            (addJointButton, 'right', 10),\
            
            (copyJointButton, 'top', 40),\
            (copyJointButton, 'left', 10),\
            (copyJointButton, 'bottom', 160),\
            (copyJointButton, 'right', 10),\
            
            (footIKButton, 'top', 70),\
            (footIKButton, 'left', 10),\
            (footIKButton, 'bottom', 130),\
            (footIKButton, 'right', 10),\
            
            (fingerButton, 'top', 100),\
            (fingerButton, 'left', 10),\
            (fingerButton, 'bottom', 100),\
            (fingerButton, 'right', 10),\
            
            (closeButton, 'top', 130),\
            (closeButton, 'left', 10),\
            (closeButton, 'bottom', 70),\
            (closeButton, 'right', 10),\
            
            (animImportButton, 'top', 160),\
            (animImportButton, 'left', 10),\
            (animImportButton, 'bottom', 40),\
            (animImportButton, 'right', 10),\
            
            (bakeButton, 'top', 190),\
            (bakeButton, 'left', 10),\
            (bakeButton, 'bottom', 10),\
            (bakeButton, 'right', 10)])
            
    #cmds.formLayout( form, edit=True, attachForm=[(b1, 'top', 5), (b1, 'left', 5), (b2, 'left', 5), (b2, 'bottom', 5), (b2, 'right', 5), (column, 'top', 5), (column, 'right', 5) ], attachControl=[(b1, 'bottom', 5, b2), (column, 'bottom', 5, b2)], attachPosition=[(b1, 'right', 5, 75), (column, 'left', 0, 75)], attachNone=(b2, 'top') )
    
    cmds.showWindow()

#ジョイント生成
def joint_add():
    #メッセージ
    cmds.inViewMessage( amg='ジョイント位置を調整後、<hl>「左側にジョイントコピー」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
    
    #メインと腰コントローラー設置
    cmds.circle( c=(0, 0, 0), nr=(0, 1, 0), r=6, n='main_controller')
    
    #ジョイント生成
    cmds.joint('main_controller', n='Root_M', p=(0, 11, 0))
    cmds.joint('Root_M', n='BackA_M', r=True, p=(0, 2, 0) )
    cmds.joint('BackA_M', n='Chest_M', r=True, p=(0, 2, 0) )
    
    cmds.joint('Chest_M', n='Scapula_R', r=True, p=(-1.0, 1.7, -1.0), ay=-2.0, az=3.0 )
    cmds.joint('Scapula_R', n='Shoulder_R', r=True, p=(-2.0, 0, 0), ay=2.0, az=2.0 )
    cmds.joint('Shoulder_R', n='Elbow_R', r=True, p=(-3.0, 0, 0), ay=1.0 )
    cmds.joint('Elbow_R', n='Wrist_R', r=True, p=(-3.5, 0, 0), az=-1.0 )
    cmds.joint('Wrist_R', n='Finger1_R', r=True, p=(-2.0, 0, 0), az=1.5 )
    cmds.joint('Finger1_R', n='Finger2_R', r=True, p=(-1.0, 0, 0), az=2.0 )
    cmds.joint('Finger2_R', n='Finger3_R', r=True, p=(-1.0, 0, 0), az=2.0 )
    cmds.joint('Finger3_R', n='Finger4_R', r=True, p=(-1.0, 0, 0) )
    '''
    cmds.joint('Wrist_R', n='ThumbFinger1_R', r=True, p=(-.8, -.8, .8), ay=2.0, az=4.5 )
    cmds.joint('ThumbFinger1_R', n='ThumbFinger2_R', r=True, p=(-.8, 0, 0), ay=-1.0 )
    cmds.joint('ThumbFinger2_R', n='ThumbFinger3_R', r=True, p=(-.8, 0, 0) )
    cmds.joint('ThumbFinger3_R', n='ThumbFinger4_R', r=True, p=(-.8, 0, 0) )
    '''
    
    cmds.joint('Root_M', n='Hip_R', r=True, p=(-1.5, -1.0, 0) )
    cmds.joint('Hip_R', n='Knee_R', r=True, p=(0, -4.0, .5) )
    cmds.joint('Knee_R', n='Ankle_R', r=True, p=(0, -4.0, -1.7) )
    cmds.joint('Ankle_R', n='MiddleToe1_R', r=True, p=(0, -1.0, .8) )
    cmds.joint('MiddleToe1_R', n='MiddleToe2_R', r=True, p=(0, -.7, 3.0) )
    
    cmds.joint('Chest_M', n='Neck_M', r=True, p=(0, 2.0, -.5), ax=2.0 )
    cmds.joint('Neck_M', n='Head_M', r=True, p=(0, 1.5, 0), ax=-2.0 )
    cmds.joint('Head_M', n='Chin_M', r=True, p=(0, -1.0, 1.0) )
    
#左側にミラー
def joint_left_add():
    #メッセージ
    cmds.inViewMessage( amg='<hl>「足のIK設置」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
    cmds.mirrorJoint('Hip_R', myz=True, mb=True, sr=('_R', '_L'));
    cmds.mirrorJoint('Scapula_R', myz=True, mb=True, sr=('_R', '_L'));

#足のIK設置
def set_knee_IK():
    #メッセージ
    cmds.inViewMessage( amg='<hl>「指のコントローラー設置」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
    #座標取得
    positionR = cmds.xform('Knee_R', q=True, ws=True, t=True)
    locatorNameR = 'Knee_R_Locator'
    #ロケーター設置
    cmds.spaceLocator(p=(positionR[0], positionR[1], positionR[2]+3.8), n=locatorNameR)
    knee_ik_add('Hip_R', 'Ankle_R', 'Knee_R_Effector', positionR, locatorNameR)
    
    #座標取得
    positionL = cmds.xform('Knee_L', q=True, ws=True, t=True)
    locatorNameL = 'Knee_L_Locator'
    #ロケーター設置
    cmds.spaceLocator(p=(positionL[0], positionL[1], positionL[2]+3.8), n=locatorNameL)
    knee_ik_add('Hip_L', 'Ankle_L', 'Knee_L_Effector', positionL, locatorNameL)
    
    #つま先のIK実行
    toe_ik_add('Ankle_R', 'MiddleToe2_R', 'Ankle_R_Effector')
    toe_ik_add('Ankle_L', 'MiddleToe2_L', 'Ankle_L_Effector')
    
    #足のコントローラー、　座標取得
    toePositionR = cmds.xform('MiddleToe1_R', q=True, ws=True, t=True)
    toePositionL = cmds.xform('MiddleToe1_L', q=True, ws=True, t=True)
    foot_controller('foot_R_controller', toePositionR[0])
    foot_controller('foot_L_controller', toePositionL[0])
    
    #コントローラー内にエフェクター移動
    cmds.parent('Ankle_L_Effector', 'foot_L_controller')
    cmds.parent('Knee_L_Effector', 'foot_L_controller')
    cmds.parent('Ankle_R_Effector', 'foot_R_controller')
    cmds.parent('Knee_R_Effector', 'foot_R_controller')

    #親子関係移動
    cmds.parent('Knee_R_Locator', 'Knee_L_Locator', 'foot_R_controller', 'foot_L_controller', 'main_controller')
    
    
#指のコントローラー設置
def set_finger_controller():
    #メッセージ
    cmds.inViewMessage( amg='「Mesh」グループを作成してメッシュをその中に入れてください。続いて<hl>「バインド」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
    
    #4本指のコントローラー、　座標取得
    fingerPositionR = cmds.xform('Finger2_R', q=True, ws=True, t=True)
    fingerPositionL = cmds.xform('Finger2_L', q=True, ws=True, t=True)
    controllerSize = 2
    finger_controller('finger_R_controller', fingerPositionR, controllerSize)
    finger_controller('finger_L_controller', fingerPositionL, controllerSize)
    
    #4本指のコントローラー移動
    cmds.parent('finger_R_controller', 'Wrist_R')
    cmds.parent('finger_L_controller', 'Wrist_L')
    
    #4本指のセットドリブン R
    for n in range(0, 3):
        finger_first_driven_add('Finger'+str(n+1)+'_R', 'finger_R_controller', 'Z')
        
    cmds.setAttr('finger_R_controller.finger_action', 10)
        
    for n in range(0, 3):
        finger_second_driven_add('Finger'+str(n+1)+'_R', 'finger_R_controller', 'Z', 70)
        
    #4本指L
    for n in range(0, 3):
        finger_first_driven_add('Finger'+str(n+1)+'_L', 'finger_L_controller', 'Z')
        
    cmds.setAttr('finger_L_controller.finger_action', 10)
        
    for n in range(0, 3):
        finger_second_driven_add('Finger'+str(n+1)+'_L', 'finger_L_controller', 'Z', 70)
    
    '''
    #親指のコントローラー、　座標取得
    thumbFingerPositionR = cmds.xform('ThumbFinger1_R', q=True, ws=True, t=True)
    thumbFingerPositionL = cmds.xform('ThumbFinger1_L', q=True, ws=True, t=True)
    controllerSize = 1
    finger_controller('thumbFinger_R_controller', thumbFingerPositionR, controllerSize)
    finger_controller('thumbFinger_L_controller', thumbFingerPositionL, controllerSize)
    
    #親指のコントローラー移動
    cmds.parent('thumbFinger_R_controller', 'Wrist_R')
    cmds.parent('thumbFinger_L_controller', 'Wrist_L')
    
    #親指のセットドリブン R
    for n in range(0, 3):
        finger_first_driven_add('ThumbFinger'+str(n+1)+'_R', 'thumbFinger_R_controller', 'Y')
        
    cmds.setAttr('thumbFinger_R_controller.finger_action', 10)
        
    for n in range(0, 3):
        finger_second_driven_add('ThumbFinger'+str(n+1)+'_R', 'thumbFinger_R_controller', 'Y', -50)
        
    #親指L
    for n in range(0, 3):
        finger_first_driven_add('ThumbFinger'+str(n+1)+'_L', 'thumbFinger_L_controller', 'Y')
        
    cmds.setAttr('thumbFinger_L_controller.finger_action', 10)
        
    for n in range(0, 3):
        finger_second_driven_add('ThumbFinger'+str(n+1)+'_L', 'thumbFinger_L_controller', 'Y', -50)
    '''

#足のIK実行
def knee_ik_add(startJointName, endJointName, effectorName, position, locatorName):
    cmds.ikHandle(sol='ikRPsolver', sj=startJointName, ee=endJointName, n=effectorName, p=.2, w=0.5 )
    cmds.move(locatorName, spr=True)
    move_locator(locatorName, position, effectorName)
    
#ロケーター位置調整、　極ベクトル設置
def move_locator(locatorName, addPosition, effectorName):
    sel = cmds.ls(locatorName)

    #ピボットポイントをオブジェクトのバウンディングボックスの中心に設定
    cmds.xform(locatorName, cp=True)
    locator = cmds.spaceLocator(n='Dummy_Locator')
    cmds.move(addPosition[0], addPosition[1], addPosition[2], ws=True)
    cmds.delete('Dummy_Locator')
    
    #極ベクトル
    cmds.poleVectorConstraint(locatorName, effectorName)
    
    cmds.select(locatorName, deselect=True)
    
#つま先のIK実行
def toe_ik_add(startJointName, endJointName, effectorName):
    cmds.ikHandle(sol='ikRPsolver', sj=startJointName, ee=endJointName, n=effectorName, p=.2, w=0.5 )
    
#足のコントローラー
def foot_controller(footControllerName, xPosition):
    cmds.circle( c=(0, 0, 0), nr=(0, 1, 0), n=footControllerName)
    cmds.scale(2, 0, 3, footControllerName)
    cmds.move(xPosition, 0, 0, footControllerName)
    
#指のコントローラー
def finger_controller(fingerControllerName, xyPosition, controllerSize):
    cmds.circle( c=(0, 0, 0), nr=(0, 1, 0), n=fingerControllerName)
    cmds.scale(controllerSize, 0, controllerSize, fingerControllerName)
    cmds.move(xyPosition[0], xyPosition[1]+1, -1, fingerControllerName)
    
    cmds.addAttr(fingerControllerName, longName='finger_action', at='double', defaultValue=0.0, minValue=0.0, maxValue=10)
    cmds.setAttr(fingerControllerName + '.finger_action', keyable=True)
    
#腰のコントローラー
def other_controller(parentControllerName, controllerName, xyPosition, controllerSize):
    cmds.circle(parentControllerName, c=(0, 0, 0), nr=(0, 1, 0), n=controllerName)
    cmds.scale(controllerSize, 0, controllerSize, controllerName)
    cmds.move(xyPosition[0], xyPosition[1], xyPosition[2], controllerName)

#指のセットドリブン
def finger_first_driven_add(fingerName, fingerControllerName, rotatePoint):
    cmds.setDrivenKeyframe(fingerName+'.rotate'+rotatePoint, cd=fingerControllerName+'.finger_action')
    
def finger_second_driven_add(fingerName, fingerControllerName, rotatePoint, rotateVal):
    cmds.setAttr(fingerName+'.rotate'+rotatePoint, rotateVal)
    cmds.setDrivenKeyframe(fingerName+'.rotate'+rotatePoint, cd=fingerControllerName+'.finger_action')

#バインド
def bind_mesh():
    #メッセージ
    cmds.inViewMessage( amg='ウエイト調整後、<hl>「アニメーションをインポート」</hl>を押し、animデータを選択して下さい。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )
        
    cmds.select('Root_M', add=True, hi=True)
    
    #正規表現、_controllerのジョイントを省く
    deselectObj = cmds.ls(sl=True)
    
    count = 0
    matchTxtEnd = re.compile("(_)(.*?)(controller)(.*)")
    
    for n in deselectObj:
        matchTrueEnd = matchTxtEnd.search(deselectObj[count])
       
        if matchTrueEnd != None:
            cmds.select(deselectObj[count], deselect=True)
            
        count += 1
        
    cmds.select('Mesh', add=True, hi=True)
    cmds.select('Mesh', deselect=True)

    cmds.skinCluster(maximumInfluences=3, dropoffRate=4, tsb=True)
    
#アニメーションをインポート
def import_anim():
    #メッセージ
    #cmds.inViewMessage( amg='<hl>「モーションをベイク」</hl>を押してください。', pos='midCenter', fade=True, fit=1,fst=4000,fts=20 )

    cmds.select('Root_M')
    cmds.select('foot_R_controller', add=True)
    cmds.select('foot_L_controller', add=True)
    cmds.select('Knee_R_Locator', add=True)
    cmds.select('Knee_L_Locator', add=True)

    fileName = cmds.fileDialog( dm='*.anim' )
    cmds.file(fileName, ra=True, pr=True, typ='animImport', i=True)
    
def motion_bake():
    #モーションをベイク Root_M以下
    endTime = cmds.playbackOptions(q=True,max=True)
    cmds.select('Root_M', hi=True)
    cmds.select('Knee_R_Locator', hi=True, add=True)
    cmds.select('Knee_L_Locator', hi=True, add=True)
    cmds.select('foot_R_controller', hi=True, add=True)
    cmds.select('foot_L_controller', hi=True, add=True)
    cmds.bakeResults(simulation=True, t=(1, endTime), sb=1, at=["rx","ry","rz"] )
    
    cmds.parent('Root_M', world=True)
    
    if cmds.objExists('main_controller'):
        cmds.select('main_controller', hi=True)
        cmds.delete()
    
    if cmds.objExists('Knee_R_Locator'):
        cmds.select('Knee_R_Locator', hi=True)
        cmds.delete()
        
    if cmds.objExists('Knee_L_Locator'):
        cmds.select('Knee_L_Locator', hi=True)
        cmds.delete()
        
    if cmds.objExists('foot_R_controller'):
        cmds.select('foot_R_controller', hi=True)
        cmds.delete()
        
    if cmds.objExists('foot_L_controller'):
        cmds.select('foot_L_controller', hi=True)
        cmds.delete()
        
    #全選択
    cmds.select(ado=True)
    cmds.select(hi=True)
    deleteObj = cmds.ls(sl=True)
    
    count = 0
    matchTxtDeleteCont = re.compile("(_)(.*?)(controller)(.*)")
    matchTxtDeleteEffec = re.compile("(_)(.*?)(effector)(.*)")
    
    for n in deleteObj:
        matchTrueDeleteCont = matchTxtDeleteCont.search(deleteObj[count])
        matchTrueDeleteEffec = matchTxtDeleteEffec.search(deleteObj[count])
       
        if matchTrueDeleteCont != None:
            print deleteObj[count]
            #cmds.delete(deleteObj[count])
            
        if matchTrueDeleteEffec != None:
            cmds.delete(deleteObj[count])
            
        count += 1
    
joint_UI()
