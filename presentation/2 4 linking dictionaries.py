# Linking dictionaries
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('=c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in 
					 vars(namespace).items() if v}
# one dictionary with some default value for some parameters
# we call argparse and check for some command line arguments which are optional
# we also want to use the os.environ dictionary, to check for the values which are 
# os specific
# the default way to do it
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
# take the dictionary from the defaults
# than do an update on the defaults from the environment variables
# that way you got some standard defaults
# than the environment variables which take precedence over the standard defaults
# than the user specified variables

d = ChainMap(command_line_args, os.environ, defaults)
# python3
# it links them all together
