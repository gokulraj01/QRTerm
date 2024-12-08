import qrcode
from . import qr_tk, log, args

code = qrcode.QRCode(
    error_correction=args.error_correction,
    box_size=5,
    border=2,
)

def qr_to_file():
    img = code.make_image(fill_color="black", back_color="white")
    try:
        img.save(args.output)
    except IOError:
        log.error("Could not save the file %s", args.output)

def qr_to_console():
    code.print_ascii(tty=True, invert=args.invert)

def main():
    # Choose the data source
    if args.input is None and args.data is None:
        qr_tk.runGUIInput(code)
    elif args.input is not None:
        log.info("Using input file - %s", args.input)
        try:
            with open(args.input, "rb") as f:
                code.add_data(f.read())
        except IOError:
             log.error("Could not open the file %s", args.input)
    else:
        log.info("Using data from console argument")
        code.add_data(args.data)
        
    # Case 1: Output to a file
    if args.output is not None:
        qr_to_file()
    # Case 2: Output to screen
    elif args.screen:
        qr_tk.display_fullscreen_image(code)
    # Case 3: Output to console
    else:
        qr_to_console()    

if __name__ == '__main__':
    main()