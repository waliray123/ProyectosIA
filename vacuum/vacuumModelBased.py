class Vacuum:

    def __init__(self):
        self.status = {'vc1-c1clean-c2clean','vc1-c1dirt-c2clean','vc1-c1clean-c2dirt','vc1-c1dirt-c2dirt','vc2-c1clean-c2clean','vc2-c1dirt-c2clean','vc2-c1clean-c2dirt','vc2-c1dirt-c2dirt'}
        self.rules = {
            'vc1-c1clean-c2clean': "ask-for-action",
            'vc1-c1dirt-c2clean': "ask-for-action",
            'vc1-c1clean-c2dirt': "ask-for-action",
            'vc1-c1dirt-c2dirt': "ask-for-action",
            'vc2-c1clean-c2clean': "ask-for-action",
            'vc2-c1dirt-c2clean': "ask-for-action",
            'vc2-c1clean-c2dirt': "ask-for-action",
            'vc2-c1dirt-c2dirt': "ask-for-action"
            ''
        }
        self.model = [
            ('vc1-c1clean-c2clean', 'ask-for-action', 'left', 'vc1-c1clean-c2clean'),
            ('vc1-c1clean-c2clean', 'ask-for-action', 'right', 'vc2-c1clean-c2clean'),
            ('vc1-c1clean-c2clean', 'ask-for-action', 'clean', 'vc1-c1clean-c2clean'),
            ('vc1-c1clean-c2clean', 'ask-for-action', 'dirt1', 'vc1-c1dirt-c2clean'),
            ('vc1-c1clean-c2clean', 'ask-for-action', 'dirt2', 'vc1-c1clean-c2dirt'),    

            ('vc1-c1dirt-c2clean', 'ask-for-action', 'left', 'vc1-c1dirt-c2clean'),
            ('vc1-c1dirt-c2clean', 'ask-for-action', 'right', 'vc2-c1dirt-c2clean'),
            ('vc1-c1dirt-c2clean', 'ask-for-action', 'clean', 'vc1-c1clean-c2clean'),
            ('vc1-c1dirt-c2clean', 'ask-for-action', 'dirt1', 'vc1-c1dirt-c2clean'),
            ('vc1-c1dirt-c2clean', 'ask-for-action', 'dirt2', 'vc1-c1dirt-c2dirt'),

            ('vc1-c1clean-c2dirt', 'ask-for-action', 'left', 'vc1-c1clean-c2dirt'),
            ('vc1-c1clean-c2dirt', 'ask-for-action', 'right', 'vc2-c1clean-c2dirt'),
            ('vc1-c1clean-c2dirt', 'ask-for-action', 'clean', 'vc1-c1clean-c2dirt'),
            ('vc1-c1clean-c2dirt', 'ask-for-action', 'dirt1', 'vc1-c1dirt-c2dirt'),
            ('vc1-c1clean-c2dirt', 'ask-for-action', 'dirt2', 'vc1-c1clean-c2dirt'),

            ('vc1-c1dirt-c2dirt', 'ask-for-action', 'left', 'vc1-c1dirt-c2dirt'),
            ('vc1-c1dirt-c2dirt', 'ask-for-action', 'right', 'vc2-c1dirt-c2dirt'),
            ('vc1-c1dirt-c2dirt', 'ask-for-action', 'clean', 'vc1-c1clean-c2dirt'),
            ('vc1-c1dirt-c2dirt', 'ask-for-action', 'dirt1', 'vc1-c1dirt-c2dirt'),
            ('vc1-c1dirt-c2dirt', 'ask-for-action', 'dirt2', 'vc1-c1dirt-c2dirt'),

            ('vc2-c1clean-c2clean', 'ask-for-action', 'left', 'vc1-c1clean-c2clean'),
            ('vc2-c1clean-c2clean', 'ask-for-action', 'right', 'vc2-c1clean-c2clean'),
            ('vc2-c1clean-c2clean', 'ask-for-action', 'clean', 'vc2-c1clean-c2clean'),
            ('vc2-c1clean-c2clean', 'ask-for-action', 'dirt1', 'vc2-c1dirt-c2clean'),
            ('vc2-c1clean-c2clean', 'ask-for-action', 'dirt2', 'vc2-c1clean-c2dirt'),

            ('vc2-c1dirt-c2clean', 'ask-for-action', 'left', 'vc1-c1dirt-c2clean'),
            ('vc2-c1dirt-c2clean', 'ask-for-action', 'right', 'vc2-c1dirt-c2clean'),
            ('vc2-c1dirt-c2clean', 'ask-for-action', 'clean', 'vc2-c1dirt-c2clean'),
            ('vc2-c1dirt-c2clean', 'ask-for-action', 'dirt1', 'vc2-c1dirt-c2clean'),
            ('vc2-c1dirt-c2clean', 'ask-for-action', 'dirt2', 'vc2-c1dirt-c2dirt'),

            ('vc2-c1clean-c2dirt', 'ask-for-action', 'left', 'vc1-c1clean-c2dirt'),
            ('vc2-c1clean-c2dirt', 'ask-for-action', 'right', 'vc2-c1clean-c2dirt'),
            ('vc2-c1clean-c2dirt', 'ask-for-action', 'clean', 'vc2-c1clean-c2clean'),
            ('vc2-c1clean-c2dirt', 'ask-for-action', 'dirt1', 'vc2-c1dirt-c2dirt'),
            ('vc2-c1clean-c2dirt', 'ask-for-action', 'dirt2', 'vc2-c1clean-c2dirt'),

            ('vc2-c1dirt-c2dirt', 'ask-for-action', 'left', 'vc1-c1dirt-c2dirt'),
            ('vc2-c1dirt-c2dirt', 'ask-for-action', 'right', 'vc2-c1dirt-c2dirt'),
            ('vc2-c1dirt-c2dirt', 'ask-for-action', 'clean', 'vc2-c1dirt-c2clean'),
            ('vc2-c1dirt-c2dirt', 'ask-for-action', 'dirt1', 'vc2-c1dirt-c2dirt'),
            ('vc2-c1dirt-c2dirt', 'ask-for-action', 'dirt2', 'vc2-c1dirt-c2dirt'),
            

            #('c1-served', 'serve-c1-wait', 'coin', 'yes-coin'),
        ]
        self.actions = {"ask-for-action": "Ask for Action",
        	"left": "Moving Left",
        	"right": "Moving Right",
            "clean": "Cleaning the room",
        	"dirt1": "Dirtying 1",
        	"dirt2": "Dirtying 2"
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

    
        
def printModel(status):
    textToReturn = ''
    if ('vc1' in status):
        textToReturn += '|*| |'
    elif ('vc2' in status):
        textToReturn += '| |*|'
    
    textToReturn += '\n'

    if ('c1clean' in status):
        textToReturn += '|0|'
    elif ('c1dirt' in status):
        textToReturn += '|1|'

    if ('c2clean' in status):
        textToReturn += '0|'
    elif ('c2dirt' in status):
        textToReturn += '1|'

    return textToReturn    
    
vacuum = Vacuum()

presentStatus = 'vc1-c1dirt-c2dirt'
presentAction = 'ask-for-action'
#textToPrint = vacuum.actions[presentAction]
textToPrint = printModel(presentStatus)
print(textToPrint) 

while(True):
    print("Insert a perception")
    perception = input()
    presentStatus = vacuum.updateStatus(presentStatus,presentAction,perception)
    presentAction = vacuum.rules[presentStatus] #Two steps in one: regla = reglas[estado]; accion = regla;

    textToPrint = printModel(presentStatus)

    #textToPrint = vacuum.actions[presentAction]

    #print("Status:" + presentStatus)
    #print("Action:" + presentAction)
    print(textToPrint)



    