from sss_lib.sharing import shares_to_secret
from parser import parse_args


def main():
    threshold = parse_args()
    shares = []

    print(f'Enter {threshold} shares separated by newlines:')
    for i in range(threshold):
        share = input(f'Share [{i + 1}/{threshold}]: ')
        shares.append(share)

    secret = shares_to_secret(shares)
    print(f'Reassembled secret: {secret}')


if __name__ == "__main__":
    main()
