import argparse, logging

# Configure the logger
logging.basicConfig(level=logging.WARNING, format='[%(name)s] %(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger("qrterm")

parser = argparse.ArgumentParser(
    description="QRTerm is a command-line application that generates QR codes. It takes raw/ASCII data as input and outputs the QR code in various formats, including displaying it directly on the screen, saving it to a file, or printing it to the terminal"
)
parser.add_argument('-o', '--output', help='Output file path. If not specified, the QR code will be printed to the console.')
parser.add_argument('-i', '--input', help='Input file path. If specified, the data will be read from this file.')
parser.add_argument('-s', '--screen', action='store_true', help='Display QR code in full screen')
parser.add_argument('--gui', action='store_true', help='Take the input data from a GUI', default=True)
parser.add_argument('data', nargs="?", metavar="<data>", help='Data to encode in the QR code')
parser.add_argument('-e', '--error-correction', type=int, choices=[0, 1, 2, 3], default=1, help='Error correction level. 0=M, 1=L, 2=H, 3=Q. Default is L.')
parser.add_argument('-x', '--invert', action='store_true', default=True, help='Invert the colors of the QR code')

args = parser.parse_args()

log.debug("Running with arguments %s", args)

if args.output is not None and args.screen is True:
    raise ValueError("Ambiguous output options: --output and --screen cannot be used together.")