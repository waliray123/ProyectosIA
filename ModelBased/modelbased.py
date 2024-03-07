class World:

    def __init__(self):
        self.status = {"no-coin","yes-coin","c1-served","c2-served","c3-served"}
        self.rules = {
            "no-coin":"ask-for-coin",
            "yes-coin":"ask-for-code",
            "c1-served":"serve-c1-wait",
            "c2-served":"serve-c2-wait",
            "c3-served":"serve-c3-wait"
        }
        self.model = [
            ('no-coin', 'ask-for-coin', 'coin', 'yes-coin'),
            ('yes-coin', 'ask-for-code', 'c1', 'c1-served'),
            ('yes-coin', 'ask-for-code', 'c2', 'c2-served'),
            ('yes-coin', 'ask-for-code', 'c3', 'c3-served'),
            ('c1-served', 'serve-c1-wait', 'served', 'no-coin'),
            ('c2-served', 'serve-c2-wait', 'served', 'no-coin'),
            ('c3-served', 'serve-c3-wait', 'served', 'no-coin'),
            ('yes-coin', 'ask-for-code', 'coin', 'yes-coin'),
            #('c1-served', 'serve-c1-wait', 'coin', 'yes-coin'),
        ]
        self.actions = {"ask-for-coin": "Ask for coin",
        	"ask-for-code": "Ask for code",
        	"serve-c1-wait": "Serving soda 1 & wait",
        	"serve-c2-wait": "Serving soda 2 & wait",
        	"serve-c3-wait": "Serving soda 3 & wait"
        }
    
    def updateStatus(self,presentStatus,presentAction,perception):
        newStatus = self.existInModel(presentStatus,presentAction,perception)
        if(newStatus == None):
            return 'no-coin'
        else:
            return newStatus
        
    
    def existInModel(self,presentStatus,presentAction,perception):
        patern = (presentStatus,presentAction,perception)
        for transition in self.model:
            if transition[:3] == patern:
                return transition[3]
            
        return None

    
world = World()

presentStatus = 'no-coin'
presentAction = 'ask-for-coin'
textToPrint = world.actions[presentAction]
print(textToPrint) 

while(True):
    print("Insert a perception")
    perception = input()
    presentStatus = world.updateStatus(presentStatus,presentAction,perception)
    presentAction = world.rules[presentStatus] #Two steps in one: regla = reglas[estado]; accion = regla;
    textToPrint = world.actions[presentAction]

    #print("Status:" + presentStatus)
    #print("Action:" + presentAction)
    print(textToPrint)



    