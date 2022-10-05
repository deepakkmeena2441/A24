from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


class school:
    parents="padam kumar jain"


    def __init__(self,name,rollno,classes):
        self.rollno=rollno
        self.name=name
        self.classes=classes

arpit=school("arpit jain",200014,12)
print(school.parents)

    