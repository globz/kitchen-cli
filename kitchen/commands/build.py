"""kitchen-cli / user action: build"""


from json import dumps

from .base import Base


class Build(Base):
    

    def run(self):
        print 'You walk into your kitchen...'
        print 'The room is empty.'
        print 'You can build the following objects : kitchen,freezer,table,oven'
        print 'usage : kitchen build kitchen'

