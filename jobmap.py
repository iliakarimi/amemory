class JobMap():
    '''
    ## Job Map
    This class can add A map to agent when it want to do A job.
    
    ### methods:
    * addjob:
        Agent should sort a map before do A job like:\n
            a>b>c>... 
    
    * usejob:
        It's A simple method that return one job after calling it and then remove used jobs.

    for more information checkout **A-memory** docs. 
    '''

    def __init__(self):
        self.WORDS = ''
        self.SYMBOL = '>'
        self.job = []

    def addjob(self, data:str=None) -> str:


        raw_data = data+self.SYMBOL

        for j in raw_data:
        
            if self.SYMBOL not in j:
                self.WORDS+=j

            elif self.SYMBOL in j:
                self.job.append(self.WORDS)
                self.WORDS=''

            else:
                raise ValueError("Wrong Type of symbol. Use '>' symbol.")

    def usejob(self):
        try:
            self.job.reverse()

            return self.job.pop()

        except IndexError:
            return "JOB ENDED"

        except Exception as e:
            return f"An Unexpected error: {e}"
