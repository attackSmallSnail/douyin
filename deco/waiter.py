

def check(func):
    def wrapper(self,*args,**kwargs):
        if kwargs.get('toDB') and not self.db.connected:
            self.db.connect()
        return func(self,*args,**kwargs)
    return wrapper