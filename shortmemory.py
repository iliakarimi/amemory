class GoalsMem():
    '''
    ## Goals Memory
    This Class store Chat goals and and facts
    #### Methods:
    * set_goals:\n
        This method can just Store goals and facts in chat
    
    * resault:\n
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

    * store_messages:\n
        this method store agent and user messages and remove 
        first old messages after 8 message betwinn user and agent.
    
    * remind_messages:\n
        This method just return stored messages.
    
    * clear_messages:
        This method clear entire messages excpet the system_text.

    for more information checkout **A-memory** docs.
    '''

    def __init__(self, m_delete: int=3, always_keep: int=0):
        self.messages = []
        self.rag_text = []
        self.systemtxt = None
        self.message_number = 0
        self.rm_messages_num = m_delete
        self.keep_always = always_keep


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
                self.messages.pop(self.keep_always)

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
