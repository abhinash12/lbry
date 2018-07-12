import logging
from twisted.internet.task import LoopingCall


log = logging.getLogger(__name__)


class Watchdog:

    def __init__(self, delay=0.05):
        self.delay = delay
        self.loop_call = LoopingCall.withCount(self.watch)

    def start(self):
        self.loop_call.start(self.delay)

    def watch(self, count):
        if count > 1:
            log.warning('Reactor was blocked for %s seconds' % (count * self.delay))

    def stop(self):
        return self.loop_call.stop()
