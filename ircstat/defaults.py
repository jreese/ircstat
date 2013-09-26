# Copyright 2013 John Reese
# Licensed under the MIT license

# the regex to parse data from irc log filenames.
# must contain two named matching groups:
#   channel: the name of the channel
#   date: the date of the conversation
filename_regex = r'(?P<channel>#?[a-z]+)_(?P<date>\d{8}).log'

# the format of the date content in the matched filename.
# must follow python's datetime.strptime() format, as defined at
# http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
filename_date_format = r'%Y%m%d'

# character encoding used by the log files
# 'latin1' is the default, but 'utf-8' is probably a good fallback
log_encoding = 'latin1'

# a regex component to match a timestamp
# only required by the default log_*_regex values
timestamp_regex = r'^\[(?P<time>\d\d:\d\d:\d\d)\]'

# a regex component to match a nick
# only required by the default log_*_regex values
nick_regex = r'(?P<nick>\S+)'

# regex to match a line containing a join action
# must contain these named matching groups:
#   time: the timestamp of the action
#   nick: the nick that joined
# may optionally contain these named matching groups:
#   hostmask: the hostmask of the nick that joined
log_join_regex = r'%s \*\*\* Joins: %s \((?P<hostmask>[^)]+)\)' % (timestamp_regex, nick_regex)

# regex to match a line containing a part action
# must contain these named matching groups:
#   time: the timestamp of the action
#   nick: the nick that left
# may optionally contain these named matching groups:
#   hostmask: the hostmask of the nick that left
#   reason: the reason that the nick left
log_part_regex = r'%s \*\*\* Parts: %s \((?P<hostmask>[^)]+)\) \((?P<reason>[^)]*)\)' % (timestamp_regex, nick_regex)

# regex to match a line containing a quit action
# must contain these named matching groups:
#   time: the timestamp of the action
#   nick: the nick that quit
# may optionally contain these named matching groups:
#   hostmask: the hostmask of the nick that quit
#   reason: the reason that the nick quit
log_quit_regex = r'%s \*\*\* Quits: %s \((?P<hostmask>[^)]+)\) \((?P<reason>[^)]*)\)' % (timestamp_regex, nick_regex)

# regex to match a line containing a user /me action
# must contain these named matching groups:
#   time: the timestamp of the action
#   nick: the nick that sent the action
#   action: the contents of the action
log_action_regex = r'%s \* %s (?P<action>.*)' % (timestamp_regex, nick_regex)

# regex to match a line containing a user message
# must contain these named matching groups:
#   time: the timestamp of the message
#   nick: the nick that sent the message
#   message: the contents of the message
log_message_regex = r'%s <%s> (?P<message>.*)' % (timestamp_regex, nick_regex)

# the format of the time content in the matched log timestamp.
# must follow python's datetime.strptime() format, as defined at
# http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
log_timestamp_date_format = r'%H:%M:%S'

# plugins to blacklist from running
# must be an iterable containing strings of plugin names,
# without the 'Plugin' suffix
plugin_blacklist = []
