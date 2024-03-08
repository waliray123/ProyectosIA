class Vacuum:

    def __init__(self):
        self.status = {'vc1','vc2','vc1-right','vc2-left','vc1-dirty','vc2-dirty','vc1-cleaning','vc2-cleaning'}
        self.rules = {
            'vc1': "ask-for-action-1",
            'vc2': "ask-for-action-2",
            'vc1-right':"moving-right",
            'vc2-left':"moving-left",
            'vc1-dirty':"vc1-is-dirty",
            'vc2-dirty':"vc2-is-dirty",
            'vc1-cleaning':"vc1-is-cleaning",
            'vc2-cleaning':"vc2-is-cleaning",
        }
        self.model = [            
            ('vc1', 'ask-for-action-1', 'is-clean', 'vc1-right'),
            ('vc1', 'ask-for-action-1', 'is-dirty', 'vc1-dirty'),
            ('vc1-right', 'moving-right', 'move-complete', 'vc2'),
            ('vc1-dirty', 'vc1-is-dirty', 'clean', 'vc1-cleaning'),
            ('vc1-cleaning', 'vc1-is-cleaning', 'finish-clean', 'vc1'),
            
            ('vc2', 'ask-for-action-2', 'is-clean', 'vc2-left'),
            ('vc2', 'ask-for-action-2', 'is-dirty', 'vc2-dirty'),
            ('vc2-left', 'moving-left', 'move-complete', 'vc1'),
            ('vc2-dirty', 'vc2-is-dirty', 'clean', 'vc2-cleaning'),
            ('vc2-cleaning', 'vc2-is-cleaning', 'finish-clean', 'vc2')
        ]
        self.actions = {"ask-for-action-1": "In room 1 waiting for action",
            "ask-for-action-2": "In room 2 waiting for action",
        	"moving-left": "Moving Left",
        	"moving-right": "Moving Right",
            "vc1-is-dirty": "Room 1 is dirty",
            "vc2-is-dirty": "Room 2 is dirty",
            "vc1-is-cleaning": "Cleaning the room 1",
            "vc2-is-cleaning": "Cleaning the room 2"
        }
    
    def updateStatus(self,presentStatus,presentAction,perception):
        newStatus = self.existInModel(presentStatus,presentAction,perception)
        if(newStatus == None):
            return presentStatus
        else:
            return newStatus
        
    
    def existInModel(self,presentStatus,presentAction,perception):
        patern = (presentStatus,presentAction,perception)
        for transition in self.model:
            if transition[:3] == patern:
                return transition[3]
            
        return None
 
    
vacuum = Vacuum()

presentStatus = 'vc1'
presentAction = 'ask-for-action-1'
textToPrint = vacuum.actions[presentAction]
#textToPrint = printModel(presentStatus)
print(textToPrint) 

while(True):
    print("Insert a perception")
    perception = input()
    presentStatus = vacuum.updateStatus(presentStatus,presentAction,perception)
    presentAction = vacuum.rules[presentStatus] #Two steps in one: regla = reglas[estado]; accion = regla;

    textToPrint = vacuum.actions[presentAction]
    print(textToPrint)



    