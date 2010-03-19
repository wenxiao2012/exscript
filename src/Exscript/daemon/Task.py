class Task(object):
    def __init__(self, name, actions, tasks):
        self.name    = name
        self.actions = actions
        self.tasks   = tasks
        #print self.__class__.__name__, actions, tasks

    def call(self, conn):
        #print "Task called:", self.name
        for action in self.actions:
            name = action[0]
            if name == 'connect':
                conn.open()
            elif name == 'autologin':
                conn.open()
                conn.authenticate(wait = True)
                conn.auto_authorize(wait = True)
            elif name == 'sendline':
                conn.send(action[1] + '\r')
            elif name == 'execline':
                conn.execute(action[1])
            elif name == 'expect':
                conn.expect(action[1])
            elif name == 'set-prompt':
                conn.set_prompt(action[1])
            elif name == 'invoke-task':
                self.tasks[action[1]].call(conn, *action[2])
            elif name == 'invoke-script':
                print name, action[1:]
                #FIXME
            else:
                raise Exception('BUG: invalid action %s' % name)