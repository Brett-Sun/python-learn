class __Plugin(object):
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        if(len(args) > 0):
            self.name = args[0]

    def addCommands(self, *commands):
        for command in commands:
            self.__dict__[command] = "Calling %s" %command

class __PluginTree(object):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def addPlugin(self, iPlugin):
        self.__dict__[iPlugin.name] = iPlugin

__pluginTree = __PluginTree()

for name in ["A", "B", "C", "D", "E"]:
    iPI = __Plugin(name)
    iPI.addCommands("Copy", "Paste", "Cut", "Delete")
    __pluginTree.addPlugin(iPI)

# print(__pluginTree.A.name)
locals().update(__pluginTree.__dict__)