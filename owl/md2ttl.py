import os,sys,re

""" simple script to bootstrap ttl from markdown 
	we require all content to be enclosed by ``` in a single line, everything else will be ignored

	note that we don't validate he Turtle
"""

help=False
verbose=False
args=[] 

for a in sys.argv[1:]:
	if os.path.exists(a):
		args.append(a)
	elif re.match("^\\-+[hH?].*",a):
		help=True
	elif re.match("^\\-+[vV].*",a):
		verbose=True
	else:
		args.append(a)

if len(args)==0:
	help=True
	sys.stderr.write("reading Markdown from stdin\n")
	sys.stderr.flush()
	args.append(sys.stdin)

if help:
	sys.stderr.write("""
	synopsis: md2ttl.py [-h] [-v] [FILE[1..n]]
		-h    display this dialog
		-v    enable verbose mode, i.e., spit out all original Markdown as TTL comments
		FILEi Markdown file to be read from, we export everything enclosed by ``` as Turtle
		      if no file is provided, we read from stdin\n""")
	sys.stderr.flush()

enforce_EOL=False
for input in args:
	if isinstance(input,str):
		input=open(input,"rt", errors="ignore")
	ttl_mode=False
	for line in input:
		line=re.sub(r"```"," ``` ",line).strip()
		if not ttl_mode and verbose:
			sys.stdout.write("# ")
		for tok in line.split():
			if tok=="```":
				ttl_mode=not ttl_mode
				sys.stdout.write("\n")
				if not ttl_mode and verbose:
					sys.stdout.write("# ")
			else:
				if verbose or ttl_mode:
					sys.stdout.write(tok+" ")
					enforce_EOL=True
		if enforce_EOL or verbose:
			sys.stdout.write("\n")
		sys.stdout.flush()
		enforce_EOL=False
