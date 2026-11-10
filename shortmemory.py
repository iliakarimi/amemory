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
            self.cn += 1

        if chatfacts:
            self.chat_facts.append(f"number{self.fn}: "+chatfacts)
            self.fn += 1

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


class ShortMemory():
    '''
    ## StoreMessage
    **StoreMessage** is A **Short-term-Messages-Memory** class for Store **Models** and **user** Messages chat.

    ### methods:
    * add_rag_base:
        Add **system text** with this method.
    \n
    * store_messages:</br>
        this method store agent and user messages and remove first old messages after 8 message betwinn user and agent.
    \n
    * remind_messages:</br>
        This method just return stored messages.
    \n
    * clear_messages:</br>
        This method clear entire messages excpet the system_text.
    \n
    **store_images**(self, path:str, uri:bool, direct:bool, url:bool, decode_method:str):</br>
        this method use for store images in chat.
    \n
    **remind_image**(self):</br>
        This method just return stored images.
    \n
    for more information checkout **A-memory** docs.
    '''

    def __init__(self, message_delete:int=3, alwayskeep:int=0, message_limit:int=10):
        self.images = None
        self.messages = []
        self.rag_text = []
        self.image_storage = []
        self.systemtxt = None
        self.message_number = 0
        self.message_limit = message_limit
        self.rm_messages_num = message_delete
        self.alwayskeep = alwayskeep


    def add_rag_base(self, text:str = None):
        self.rag_text.append(text)
        self.messages.append({"role": "developer", "content": self.rag_text[0]})


    # Storing messages with 8 limit and forget first and old message after add new message
    def store_messages(self, role:str | None, message:str | None) -> str:
        '''
        ## store_messages
        **store_messages** use for store and remember text messages.

        usage:
        * **role**(str):</br>
            This parameter's get message role like "developer", "assistant" and "user".
        \n
        * **message**(bool):</br>
            This parametes's get message text.
        \n
        for more information checkout **A-memory** docs.
        '''

        # Add new messages
        if self.message_number != self.message_limit:
            self.messages.append({"role": role, "content": message})
            self.message_number+=1
        # Remove old message after 8 message
        else:
            for r in range(self.rm_messages_num):
                self.messages.pop(self.alwayskeep)

            self.message_number = 0
            self.messages.append({"role": role, "content": message})

    def store_images(self, role:str=None, path:str=None, uri:bool=False, direct:bool=False,
                   url:bool=False, decode_method:str="utf-8"):
        '''
        ## store_images
        **storeimage** use for store and remember Images.

        usage:
        * **role**(str):</br>
            set message role with this parameter like "developer", "assistant" and "user".
        \n
        * **path**(str):</br>
            This parameter's get image path or URL.
        \n
        #### store method:
        * **uri**(bool):</br>
        If you want store base64 Encoded Image, make this parameter 'True'.
        \n
        * **direct**(bool):</br>
        If you want store Image directly with path, make this parameter 'True'.
        \n
        * **url**(bool):</br>
        If you want store Image with **URL**, make this parameter 'True'.
        \n
        * **decode_method**(str):
        If you want store Images with decode, you can add values like 'utf-8' to this parameter.
        \n
        for more information checkout **A-memory** docs.
        '''

        try:
            if self.message_number <= self.message_limit:

                # Check for storage method and Store new image.
                if uri == True and uri != False:
                    with open(path, "rb") as image_file:
                        if decode_method:
                            imagecode = base64.b64encode(image_file.read()).decode(decode_method)
                        
                        elif decode_method == None:
                            imagecode = base64.b64encode(image_file.read())

                        self.images = f"data:image/png;base64,{imagecode}"
                        self.messages.append(f"data:image/png;base64,{imagecode}")
                        self.image_storage.append({"role": role, "content": f"data:image/png;base64,{imagecode}"})

                elif url == True and url != False:
                    self.images = path
                    self.messages.append(path)
                    self.image_storage.append({"role": role, "content": path})

                elif direct == True and direct != False:
                    self.images = f"file://{path}"
                    self.messages.append({"role": role, "content": f"file://{path}"})
                    self.image_storage.append({"role": role, "content": f"file://{path}"})

                # Raise Error when all of mthods False
                elif direct == False and uri == False or url == False:
                    raise ValueError("Use 'direct', 'uri' or 'url' to specify the Image store method.")

            # Remove old message after 8 message
            else:
                for ir in range(self.image_delete):
                    self.image_storage.pop(self.alwayskeep)
                    self.messages.pop(self.alwayskeep)
                
                self.message_number = 0
                self.messages.append({"role": role, "content": self.images})
        
        except Exception as e:
            print(e.with_traceback)

    # Return all stored Messages
    def remind_messages(self) -> None:
        '''
        ## remind_messages
        **remind_messages** return all stored messages.
        \n
        for more information checkout **A-memory** docs.
        '''

        return self.messages

    # Return all stored Images
    def remind_images(self) -> None:
        '''
        ## remind_image
        **remind_image** return stored Images.
        \n
        for more information checkout **A-memory** docs.
        '''

        return self.image_storage

    # Clear entir memory
    def clear_messages(self):
            
            self.messages.clear()

            if self.messages == []:
                self.messages.append({"role": "developer", "content": self.rag_text[0]})
