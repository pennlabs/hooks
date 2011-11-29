"""
Installs git precommit hooks in the local .git/hooks directory.
"""

if __name__ == "__main__":
  # Add precommit hook
  if not os.path.exists('.git/hooks/pre-commit'):
    print "No pre-commit hook found..."

    from subprocess import Popen, PIPE

    def run(command):
        p = Popen(command.split(), stdout=PIPE, stderr=PIPE)
        p.wait()
        return p.returncode, p.stdout.read().strip().split(), p.stderr.read()
        
    # add new hook
    hook = "git@github.com:pennappslabs/hooks.git"
    commands = ( 
        'rm -fr .git/hooks',
        'git clone %s .git/hooks' % hook,
        'chmod +x .git/hooks/pre-commit',
        )
    for command in commands:
      exit_code, _, errors = run(command)
      if exit_code != 0:
        print >>sys.stderr, "\r Failed installing hook. \n%s" % errors
        break
    else:
      print "Sucessfully installed git precommit hook from %s" % hook
  else:
    print "Pre-commit hook found."
