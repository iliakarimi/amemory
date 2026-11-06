import base64

class GoalsMem():
    '''
    ## Goals Memory
    This Class store Chat goals and and facts
    #### Methods:
    * set_goals:</br>
        This method can just Store goals and facts in chat
    
    * resault:</br>
        This methed can return Stored data
    
    for more information checkout **A-memory** docs.
    '''

    def __init__(self):
        self.context_goals = []
        self.recent_goal = None
        self.active_goal = None
        self.chat_facts = []
        self.cn = 0
        self.fn = 0

    # This method set and store goals in list 
    def set_goals(self, contextgoals=None, recentgoal=None, 
            activegoal=None, chatfacts=None) -> str:

        if activegoal:
            self.active_goal = activegoal

        if recentgoal:
            self.recent_goal = recentgoal

        if contextgoals:
            self.context_goals.append(f"number{self.cn}: "+contextgoals)
            self.cn+=1

        if chatfacts:
            self.chat_facts.append(f"number{self.fn}: "+chatfacts)
            self.fn=+1

    # The resault methed return data stored in lists
    def resault(self, cg:bool | False, ag:bool | False, 
            rg:bool | False, cf:bool | False, al:bool | False):
        resu = []

        if cg == True:
            resu.append(self.context_goals)

        if ag == True:
            resu.append(self.active_goal)

        if rg == True:
            resu.append(self.recent_goal)

        if cf == True:
            resu.append(self.chat_facts)

        if al == True:
            return f"Active Goal: {self.active_goal}\nRecent Goal: {self.recent_goal}\nContaxt Goals: {self.context_goals}\nChat Facts: {self.chat_facts}"
        if resu!=None:
            return resu


class ShortMem():
    '''
    ## Short Memory
    This class is A **Short-term-Memory** for agents Store **Agent** and **user** chat.

    ### methods:
    * add_rag_base:
        Add **system text** with this method.

    * store_messages:</br>
        this method store agent and user messages and remove 
        first old messages after 8 message betwinn user and agent.
    
    * remind_messages:</br>
        This method just return stored messages.
    
    * clear_messages:</br>
        This method clear entire messages excpet the system_text.

    for more information checkout **A-memory** docs.
    '''

    def __init__(self, m_delete: int=3, alwayskeep: int=0):
        self.messages = []
        self.rag_text = []
        self.systemtxt = None
        self.message_number = 0
        self.rm_messages_num = m_delete
        self.alwayskeep = alwayskeep


    def add_rag_base(self, text:str = None):
        self.rag_text.append(text)
        self.messages.append({"role": "developer", "content": self.rag_text[0]})


    # Storing messages with 8 limit and forget first and old message after add new message
    def store_messages(self, role:str | None, message:str | None) -> str:
        # Add new messages
        if self.message_number != 10:
            self.messages.append({"role": role, "content": message})
            self.message_number+=1
        # Remove old message after 8 message
        else:
            for r in range(self.rm_messages_num):
                self.messages.pop(self.alwayskeep)

            self.message_number = 0
            self.messages.append({"role": role, "content": message})

    # Return all stored Messages
    def remind_messages(self):
        return self.messages

    # Clear entir memory
    def clear_messages(self):
            self.messages.clear()

            if self.messages == []:
                self.messages.append({"role": "developer", "content": self.rag_text[0]})

class StoreImage():
    def __init__(self, idelete:int=2):
        self.idelete = idelete
        self.image_storage = []

    def storeimage(self, path:str=None, uri:bool=True, direct:bool=False,
                   url:bool=False, decode_method:str="utf-8", ):
        '''
        ## Store Image
        **storeimage** use for store and remember Images.

        usage:
        * **path**:</br>
            This parameter's get image path or URL
        \n
        * **direct**(bool):</br>
        This parameter's 

        '''

        # 1
        if self.idelete == True:    # try to figure out which function do I put this
            for ir in range(self.idelete):
                self.image_storage.pop()
        try:
            if uri == True:
                with open(path, "r") as image_file:
                    if decode_method:
                        imagecode = base64.b64decode(image_file.read()).decode(decode_method)
                    else:
                        imagecode = base64.b64decode(image_file.read())

                    self.image_storage.append(imagecode)

            elif url == True:
                self.image_storage.append(path)

            elif direct == True:
                self.image_storage.append(f"file://{path}")

            else:
                return None
        
        except None:
            raise ValueError("Use **direct**, **uri** or **url** to specify the Image store method.").with_traceback
        


    def attachimage(self, attach:str=None, 
                    uri:bool=False, url:bool=False):
        pass

    def remindimage(self) -> None:
        
        #2
        if self.idelete == True:    
            for ir in range(self.idelete):
                self.image_storage.pop()
