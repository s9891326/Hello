import statsd

c = statsd.StatsClient('192.168.223.127', 8125)
c.incr('foo')  # Increment the 'foo' counter.
c.incr('foo.root.called')
c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.



