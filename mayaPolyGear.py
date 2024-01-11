import maya.cmds as cmds

def select_every_other_face_cylinder():
    # Create a polygon cylinder.  Modify the next line to change the look of the gear
    # changing the subdivisionAxis to an odd number will yield strange results
    cylinder = cmds.polyCylinder(radius=5, height=2, subdivisionsHeight=1, subdivisionsAxis=21, name="myCylinder")[0]

    # Get the total number of faces
    total_faces = cmds.polyEvaluate(cylinder, face=True)

    # Select every other face excluding caps
    selected_faces = ['{}.f[{}]'.format(cylinder, i) for i in range(2, total_faces-2, 2)]  # Exclude cap faces
    
    if selected_faces:
        cmds.select(selected_faces)
        print("Every other face on the cylinder (excluding caps) selected.")
        
        # Extrude the selected faces along normals
        cmds.polyExtrudeFacet(localTranslateZ=1.52016, divisions=1, constructionHistory=True)
        
    else:
        print("No faces to select. Check the cylinder geometry.")

# Run the function to select every other face on the cylinder
select_every_other_face_cylinder()

#you may now use the scale tool to change the appearance of the gear teeth
