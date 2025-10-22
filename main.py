import argparse
from modules import port_scanner, brute_forcer, banner_grabber

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("-m", "--module", help="Module to run (scanner/brute/banner)", required=True)
    parser.add_argument("-t", "--target", help="Target IP or URL", required=True)
    parser.add_argument("-p", "--port", help="Port number (for scanner/banner)", type=int)
    parser.add_argument("-u", "--username", help="Username (for brute-forcer)")
    parser.add_argument("-w", "--wordlist", help="Path to password wordlist (for brute-forcer)")

    args = parser.parse_args()

    if args.module.lower() == "scanner":
        port_scanner.scan_target(args.target)
    elif args.module.lower() == "brute":
        brute_forcer.brute_force(args.target, args.username, args.wordlist)
    elif args.module.lower() == "banner":
        banner_grabber.grab_banner(args.target, args.port)
    else:
        print("Invalid module. Choose from: scanner, brute, banner")

if __name__ == "__main__":
    main()
