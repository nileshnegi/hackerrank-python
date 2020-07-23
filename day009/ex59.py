"""
Set .add()

The first line contains an integer ```N```, the total number of country stamps.
The next ```N``` lines contains the name of the country where the stamp is from.
"""
if __name__ == "__main__":
    country = set()

    for _ in range(int(input())):
        country.add(input())
    
    print(len(country))