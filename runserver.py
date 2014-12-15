from tbFinder import app
import optparse

def main(options):
	if options.debug == True:
		if options.port == "-1":
			app.run(debug=True)
		else:
			app.run(debug=True, port=int(options.port))
	else:
		if options.port == "-1":
			app.run(debug=False)
		else:
			app.run(debug=False, port=int(options.port))


if __name__ == "__main__":
	optparser = optparse.OptionParser()
	optparser.add_option('-d', '--debug', action="store_true", default=False,
							 dest="debug", help="runs app in debug mode")
	optparser.add_option('-p', '--setport', action="store", default="-1",
							 dest="port", help="controls which port the local server runs on")
	options, args = optparser.parse_args()
	main(options)
