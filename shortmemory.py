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
        if self.message_number != 10:
            self.messages.append({"role": role, "content": message})
            self.message_number+=1
        # Remove old message after 8 message
        else:
            for r in range(self.rm_messages_num):
                self.messages.pop(self.alwayskeep)

            self.message_number = 0
            self.messages.append({"role": role, "content": message})

    def store_images(self, path:str=None, uri:bool=False, direct:bool=False,
                   url:bool=False, decode_method:str="utf-8"):
        '''
        ## store_images
        **storeimage** use for store and remember Images.

        usage:
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
            if self.image_number <= 10:    # try to figure out which function do I put this
                
                if uri == True and uri != False:
                    with open(path, "rb") as image_file:
                        if decode_method:
                            imagecode = base64.b64encode(image_file.read()).decode(decode_method)
                        
                        elif decode_method == None:
                            imagecode = base64.b64encode(image_file.read())

                        self.image_storage.append(f"data:image/png;base64,{imagecode}")

                elif url == True and url != False:
                    self.image_storage.append(path)

                elif direct == True and direct != False:
                    self.image_storage.append(f"file://{path}")

                elif direct == False and uri == False or url == False:
                    raise ValueError

            else:
                for ir in range(self.image_delete):
                    self.image_storage.pop()
        
        except:
            if ValueError:
                raise ValueError("Use 'direct', 'uri' or 'url' to specify the Image store method.")

    # Return all stored Messages
    def remind_messages(self) -> None:
        '''
        ## remind_messages
        **remind_messages** return stored messages.
        \n
        for more information checkout **A-memory** docs.
        '''

        return self.messages

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






# class StoreImage():
#     '''
#     ## StoreImage

#     **StoreImage** is a **Short-term-Image-Memory** class for store **Models** and **user** Images.
#     \n
#     Methods:
#     \n
#     **storeimage**(self, path:str, uri:bool, direct:bool, url:bool, decode_method:str):
#     \n
#         this method use for store images in chat.
#     \n
#     **remindimage**(self):
#     \n
#         This method just return stored images.
#     \n
#     for more information checkout **A-memory** docs.
#     '''

#     def __init__(self, image_delete:int=2):
#         self.attached = []
#         self.image_storage = []
#         self.image_number = 0
#         self.image_delete = image_delete

#     def storeimage(self, path:str=None, uri:bool=False, direct:bool=False,
#                    url:bool=False, decode_method:str="utf-8"):
#         '''
#         ## storeimage
#         **storeimage** use for store and remember Images.

#         usage:
#         * **path**(str):</br>
#             This parameter's get image path or URL.
#         \n
#         #### store method:
#         * **uri**(bool):</br>
#         If you want store base64 Encoded Image, make this parameter 'True'.
#         \n
#         * **direct**(bool):</br>
#         If you want store Image directly with path, make this parameter 'True'.
#         \n
#         * **url**(bool):</br>
#         If you want store Image with **URL**, make this parameter 'True'.
#         \n
#         * **decode_method**(str):
#         If you want store Images with decode, you can add values like 'utf-8' to this parameter.
#         \n
#         for more information checkout **A-memory** docs.
#         '''

#         try:
#             if self.image_number <= 10:    # try to figure out which function do I put this
                
#                 if uri == True and uri != False:
#                     with open(path, "rb") as image_file:
#                         if decode_method:
#                             imagecode = base64.b64encode(image_file.read()).decode(decode_method)
                        
#                         elif decode_method == None:
#                             imagecode = base64.b64encode(image_file.read())

#                         self.image_storage.append(f"data:image/png;base64,{imagecode}")

#                 elif url == True and url != False:
#                     self.image_storage.append(path)

#                 elif direct == True and direct != False:
#                     self.image_storage.append(f"file://{path}")

#                 elif direct == False and uri == False or url == False:
#                     raise ValueError

#             else:
#                 for ir in range(self.image_delete):
#                     self.image_storage.pop()
        
#         except:
#             if ValueError:
#                 raise ValueError("Use 'direct', 'uri' or 'url' to specify the Image store method.")

#     def attachimage(self, attach:str=None, direct:bool=False, uri:bool=False, 
#                     url:bool=False, decode_method:str="utf-8", clear_attach=None):
#         '''
#         ## attachimage
#         **attachimage** use for attach Images and use for like showing images to models.

#         usage:
#         * **attach**(str):</br>
#             This parameter's get and attach image or image URL.
#         \n
#         #### store method:
#         * **uri**(bool):</br>
#         If you want store base64 Encoded Image, make this parameter 'True'.
#         \n
#         * **direct**(bool):</br>
#         If you want store Image directly with path, make this parameter 'True'.
#         \n
#         * **url**(bool):</br>
#         If you want store Image with **URL**, make this parameter 'True'.
#         \n
#         * **decode_method**(str):
#         If you want store Images with decode, you can add values like 'utf-8' to this parameter.
#         \n
#         for more information checkout **A-memory** docs.
#         '''

#         try:
#             if uri == True and uri != False:
#                 with open(attach, "rb") as image_file:
#                     if decode_method:
#                         attached_image = base64.b64encode(image_file.read()).decode(decode_method)

#                     else:
#                         attached_image = base64.b64encode(image_file.read())

#                 self.attached.append(attached_image)

#             if url == True and url != False:
#                 self.attached.append(attached_image)

#             if direct == True and direct != False:
#                 self.attached.append(f"file://{attach}")

#             if clear_attach == True:
#                 self.attached.clear()
#                 self.attached.
#             if direct == False and uri == False or url == False:
#                 raise ValueError


#         except:
#             if ValueError:
#                 raise ValueError("Use 'direct', 'uri' or 'url' to specify the Image store method.")
        
#     def remindimage(self) -> bool:
#         '''
#         ## remindimage
#         **remindimage** return stored Images.

#         # usage:
#         # * **memory**(bool):</br>
#         # If you want return stored memory(Not Attached Image), make this parameter 'True'
#         # \n
#         # * **attached**(bool):</br>
#         # If you want return attached image, make this parameter 'True'
#         \n
#         for more information checkout **A-memory** docs.
#         '''
#         try:
#             if memory == True:
#                 return self.image_storage

#             if attached == True:
#                 return self.attach

#             if memory == False and attached == False:
#                 raise ValueError

#             if type(memory) == str or type(memory) == int:
#                 raise TypeError

#         except Exception as e:
#             print(e)
#             if ValueError:
#                 raise ValueError("You Should Make At least 1 parameter's 'True'.")

#             if TypeError:
#                 raise TypeError("Use boolian(True/False) for Argoment.")
