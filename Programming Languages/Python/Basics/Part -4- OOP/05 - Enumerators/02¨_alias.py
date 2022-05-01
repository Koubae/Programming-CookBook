import enum

class Status(enum.Enum):
    ready = 'ready'
    
    running = 'running'
    busy = 'running'
    processing = 'running'
    
    ok = 'ok'
    finished_no_error = 'ok'
    ran_ok = 'ok'
    
    errors = 'errors'
    finished_with_errors = 'errors'
    errored = 'errors'


print(list(Status))

# [<Status.ready: 'ready'>,
#  <Status.running: 'running'>,
#  <Status.ok: 'ok'>,
#  <Status.errors: 'errors'>]
print(Status.__members__)

print(Status['busy'])
#<Status.running: 'running'>
print(Status['processing'])
#<Status.running: 'running'>

@enum.unique
class Status(enum.Enum):
    ready = 1
    done_ok = 2
    errors = 3


try:
    @enum.unique
    class Status(enum.Enum):
        ready = 1
        waiting = 1
        done_ok = 2
        errors = 3
except ValueError as ex:
    print(ex)

# duplicate values found in <enum 'Status'>: waiting -> ready