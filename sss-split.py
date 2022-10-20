from sss_lib.consts import MAX_SECRET_LENGTH
from sss_lib.sharing import secret_to_shares
from parser import parse_args


def main():
    threshold, shares_num = parse_args()
    secret = input(f'Enter the secret, at most '
                   f'{MAX_SECRET_LENGTH} ASCII characters: ')

    shares = secret_to_shares(secret, threshold, shares_num)
    [print('\n' + share) for share in shares]


if __name__ == "__main__":
    main()
